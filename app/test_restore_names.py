from typing import List, Dict, Any


def restore_names(users: List[Dict[str, Any]]) -> None:
    for user in users:
        if user.get("first_name") is None:
            full_name = user.get("full_name")
            if full_name:
                parts = full_name.split()
                if parts:
                    user["first_name"] = parts[0]


def test_restore_names_with_explicit_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_with_missing_first_name_key() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert "first_name" in users[0]
    assert users[0]["first_name"] == "Mike"


def test_restore_names_does_not_overwrite_existing_names() -> None:
    users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "John Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_modifies_list_in_place() -> None:
    user: Dict[str, Any] = {"full_name": "Alice Smith"}
    users = [user]
    restore_names(users)
    assert users[0] is user
    assert user["first_name"] == "Alice"


def test_restore_names_handles_empty_list() -> None:
    users: List[Dict[str, Any]] = []
    restore_names(users)
    assert users == []


def test_restore_names_with_multiple_users() -> None:
    users = [
        {"first_name": None, "full_name": "Bob Builder"},
        {"full_name": "Charlie Brown"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Bob"
    assert users[1]["first_name"] == "Charlie"


def test_restore_names_with_complex_whitespace() -> None:
    users = [{"full_name": "  Dave   Miller  "}]
    restore_names(users)
    assert users[0]["first_name"] == "Dave"
