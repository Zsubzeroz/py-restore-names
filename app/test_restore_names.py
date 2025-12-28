from typing import List, Dict, Any


def restore_names(users: List[Dict[str, Any]]) -> None:
    for user in users:
        if user.get("first_name") is None:
            full_name = user.get("full_name")
            if full_name:
                parts = full_name.split()
                if parts:
                    user["first_name"] = parts[0]


def test_restore_names_handles_explicit_none() -> None:
    users = [{"first_name": None, "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0].get("first_name") == "Jack"


def test_restore_names_handles_missing_key() -> None:
    users = [{"full_name": "Mike Adams"}]
    restore_names(users)
    assert "first_name" in users[0]
    assert users[0]["first_name"] == "Mike"


def test_restore_names_does_not_overwrite_existing() -> None:
    users = [{"first_name": "John", "full_name": "Jack Doe"}]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_restore_names_modifies_in_place() -> None:
    user_dict: Dict[str, Any] = {"full_name": "Alice Smith"}
    users = [user_dict]
    restore_names(users)
    assert users[0] is user_dict
    assert user_dict["first_name"] == "Alice"


def test_restore_names_handles_empty_list() -> None:
    users: List[Dict[str, Any]] = []
    restore_names(users)
    assert users == []
