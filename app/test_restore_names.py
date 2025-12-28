import pytest
from typing import List, Dict, Any


def restore_names(users: List[Dict[str, Any]]) -> None:
    for user in users:
        if user.get("first_name") is None:
            user["first_name"] = user["full_name"].split()[0]


def test_restore_names_with_none_value() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_with_missing_key() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_names_does_not_overwrite_existing() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "Johnny Doe",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_restore_names_single_name_full_name() -> None:
    users = [
        {
            "full_name": "Cher",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Cher"


def test_restore_names_empty_list() -> None:
    users: List[Dict[str, Any]] = []
    restore_names(users)
    assert users == []


def test_restore_names_multiple_entries() -> None:
    users = [
        {"first_name": None, "full_name": "Alice Wonderland"},
        {"full_name": "Bob Builder"},
        {"first_name": "Charlie", "full_name": "Charles Xavier"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"
    assert users[1]["first_name"] == "Bob"
    assert users[2]["first_name"] == "Charlie"


@pytest.mark.parametrize("input_users, expected_first_name", [
    ([{"first_name": None, "full_name": "Anna Smith"}], "Anna"),
    ([{"full_name": "David Miller"}], "David"),
    ([{"first_name": "Mark", "full_name": "Marcus Aurelius"}], "Mark")
])
def test_restore_names_parametrized(
    input_users: List[Dict[str, Any]],
    expected_first_name: str
) -> None:
    restore_names(input_users)
    assert input_users[0]["first_name"] == expected_first_name
