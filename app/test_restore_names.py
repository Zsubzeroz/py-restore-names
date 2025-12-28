import pytest
from typing import List, Dict, Any


def restore_names(users: List[Dict[str, Any]]) -> None:
    for user in users:
        if user.get("first_name") is None:
            full_name = user.get("full_name")
            if isinstance(full_name, str):
                parts = full_name.split()
                if parts:
                    user["first_name"] = parts[0]


@pytest.mark.parametrize("users_data, expected_name", [
    ([{"first_name": None, "full_name": "Jack Holy"}], "Jack"),
    ([{"full_name": "Mike Adams"}], "Mike")
])
def test_restore_names_none_and_missing(
    users_data: List[Dict[str, Any]],
    expected_name: str
) -> None:
    restore_names(users_data)
    assert users_data[0]["first_name"] == expected_name


def test_restore_names_inplace_modification() -> None:
    user = {"full_name": "Alice Smith"}
    users = [user]
    restore_names(users)
    assert users[0] is user
    assert user["first_name"] == "Alice"


def test_restore_names_no_overwrite_existing() -> None:
    users = [{"first_name": "John", "full_name": "Jack Doe"}]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_restore_names_empty_list() -> None:
    users: List[Dict[str, Any]] = []
    restore_names(users)
    assert users == []


def test_restore_names_multiple_users() -> None:
    users = [
        {"first_name": None, "full_name": "Alice Smith"},
        {"full_name": "Bob Builder"},
        {"first_name": "Charlie", "full_name": "Charles Xavier"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"
    assert users[1]["first_name"] == "Bob"
    assert users[2]["first_name"] == "Charlie"
