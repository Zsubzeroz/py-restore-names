import pytest
from typing import List, Dict, Any


def restore_names(users: List[Dict[str, Any]]) -> None:
    for user in users:
        if user.get("first_name") is None:
            full_name = user.get("full_name")
            if full_name:
                user["first_name"] = full_name.split()[0]


def test_restore_names_handles_none_value() -> None:
    users: List[Dict[str, Any]] = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_handles_missing_key() -> None:
    users: List[Dict[str, Any]] = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert "first_name" in users[0]
    assert users[0]["first_name"] == "Mike"


def test_restore_names_is_inplace() -> None:
    user: Dict[str, Any] = {"full_name": "Jack Holy"}
    users: List[Dict[str, Any]] = [user]
    restore_names(users)
    assert users[0] is user
    assert user["first_name"] == "Jack"


def test_restore_names_does_not_overwrite() -> None:
    users: List[Dict[str, Any]] = [
        {
            "first_name": "Jack",
            "full_name": "John Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


@pytest.mark.parametrize("user_data,expected", [
    ({"first_name": None, "full_name": "Jack Holy"}, "Jack"),
    ({"full_name": "Mike Adams"}, "Mike"),
])
def test_restore_names_parametrized(user_data: Dict[str, Any], expected: str) -> None:
    users = [user_data]
    restore_names(users)
    assert users[0]["first_name"] == expected


def test_restore_names_empty_list() -> None:
    users: List[Dict[str, Any]] = []
    restore_names(users)
    assert users == []


def test_restore_names_multiple_users() -> None:
    users: List[Dict[str, Any]] = [
        {"first_name": None, "full_name": "Alice Smith"},
        {"full_name": "Bob Builder"},
        {"first_name": "Charlie", "full_name": "Charles Xavier"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"
    assert users[1]["first_name"] == "Bob"
    assert users[2]["first_name"] == "Charlie"
