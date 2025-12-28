from typing import List, Dict, Any


def restore_names(users: List[Dict[str, Any]]) -> None:
    for user in users:
        if user.get("first_name") is None:
            full_name = user.get("full_name")
            if isinstance(full_name, str) and full_name.strip():
                user["first_name"] = full_name.split()[0]


def test_restore_names_handles_explicit_none_value() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_handles_missing_first_name_key() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert "first_name" in users[0]
    assert users[0]["first_name"] == "Mike"


def test_restore_names_preserves_existing_first_name() -> None:
    users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "John Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_performs_in_place_modification() -> None:
    user: Dict[str, Any] = {"full_name": "Alice Smith"}
    users = [user]
    restore_names(users)
    assert users[0] is user
    assert user["first_name"] == "Alice"


def test_restore_names_handles_empty_list() -> None:
    users: List[Dict[str, Any]] = []
    restore_names(users)
    assert users == []


def test_restore_names_handles_whitespace_in_full_name() -> None:
    users = [{"full_name": "  Bob  The  Builder  "}]
    restore_names(users)
    assert users[0]["first_name"] == "Bob"


def test_restore_names_ignores_empty_or_invalid_full_name() -> None:
    users = [
        {"full_name": ""},
        {"full_name": "   "},
        {"first_name": None, "full_name": None}
    ]
    restore_names(users)
    assert "first_name" not in users[0]
    assert "first_name" not in users[1]
    assert users[2]["first_name"] is None
