from typing import List, Dict, Any

def restore_names(users: List[Dict[str, Any]]) -> None:
    for user in users:
        if user.get("first_name") is None:
            full_name = user.get("full_name")
            if isinstance(full_name, str):
                parts = full_name.strip().split()
                if parts:
                    user["first_name"] = parts[0]

def test_restore_names_handles_none_value() -> None:
    users = [{"first_name": None, "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"

def test_restore_names_handles_missing_key() -> None:
    users = [{"full_name": "Mike Adams"}]
    restore_names(users)
    assert "first_name" in users[0]
    assert users[0]["first_name"] == "Mike"

def test_restore_names_modifies_in_place() -> None:
    user = {"full_name": "Alice Smith"}
    users = [user]
    restore_names(users)
    assert users[0] is user
    assert user["first_name"] == "Alice"

def test_restore_names_no_overwrite() -> None:
    users = [{"first_name": "Jack", "full_name": "John Doe"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"

def test_restore_names_empty_full_name() -> None:
    users = [{"full_name": ""}]
    restore_names(users)
    assert "first_name" not in users[0]

def test_restore_names_whitespace_full_name() -> None:
    users = [{"full_name": "   "}]
    restore_names(users)
    assert "first_name" not in users[0]

def test_restore_names_none_full_name() -> None:
    users = [{"full_name": None}]
    restore_names(users)
    assert "first_name" not in users[0]

def test_restore_names_missing_full_name() -> None:
    users = [{"last_name": "Doe"}]
    restore_names(users)
    assert "first_name" not in users[0]

def test_restore_names_invalid_type_full_name() -> None:
    users = [{"full_name": 123}]
    restore_names(users)
    assert "first_name" not in users[0]
