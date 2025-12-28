from typing import List, Dict, Any


def restore_names(users: List[Dict[str, Any]]) -> None:
    for user in users:
        if user.get("first_name") is None:
            full_name = user.get("full_name")
            if full_name:
                parts = full_name.split()
                if parts:
                    user["first_name"] = parts[0]


def test_restore_names_with_none_value() -> None:
    users = [{"first_name": None, "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_with_missing_key() -> None:
    users = [{"full_name": "Mike Adams"}]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_names_does_not_overwrite_valid_name() -> None:
    users = [{"first_name": "Jack", "full_name": "John Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_modifies_objects_in_place() -> None:
    user: Dict[str, Any] = {"full_name": "Jack Holy"}
    users = [user]
    restore_names(users)
    assert users[0] is user
    assert users[0]["first_name"] == "Jack"


def test_restore_names_empty_list() -> None:
    users: List[Dict[str, Any]] = []
    restore_names(users)
    assert users == []


def test_restore_names_with_multiple_records() -> None:
    users = [
        {"first_name": None, "full_name": "Alice Wonderland"},
        {"full_name": "Bob Builder"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"
    assert users[1]["first_name"] == "Bob"


def test_restore_names_with_complex_whitespace() -> None:
    users = [{"full_name": "  Charlie   Brown  "}]
    restore_names(users)
    assert users[0]["first_name"] == "Charlie"
