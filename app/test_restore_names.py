from typing import List, Dict, Any


def restore_names(users: List[Dict[str, Any]]) -> None:
    for user in users:
        if user.get("first_name") is None:
            full_name = user.get("full_name")
            if full_name:
                user["first_name"] = full_name.split()[0]


def test_restore_names_handles_none_value() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_handles_missing_key() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert "first_name" in users[0]
    assert users[0]["first_name"] == "Mike"


def test_restore_names_does_not_overwrite_existing() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "Jack Doe",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_restore_names_modifies_in_place() -> None:
    user: Dict[str, Any] = {"full_name": "Alice Smith"}
    users = [user]
    restore_names(users)
    assert users[0] is user
    assert user["first_name"] == "Alice"


def test_restore_names_with_empty_list() -> None:
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


def test_restore_names_with_single_name() -> None:
    users = [{"full_name": "Cher"}]
    restore_names(users)
    assert users[0]["first_name"] == "Cher"
