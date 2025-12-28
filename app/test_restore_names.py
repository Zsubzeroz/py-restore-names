import pytest
from typing import List, Dict, Any


def restore_names(users: List[Dict[str, Any]]) -> None:
    for user in users:
        if user.get("first_name") is None:
            full_name = user.get("full_name", "")
            parts = full_name.split()
            if parts:
                user["first_name"] = parts[0]


def test_restore_names_modifies_in_place() -> None:
    user_dict: Dict[str, Any] = {
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }
    users = [user_dict]
    restore_names(users)
    assert users[0] is user_dict
    assert users[0]["first_name"] == "Jack"


def test_restore_names_preserves_existing_first_name() -> None:
    users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "Johnny Doe",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"


@pytest.mark.parametrize("input_user, expected_first_name", [
    ({"first_name": None, "full_name": "Mike Adams"}, "Mike"),
    ({"full_name": "  Alice   Wonderland  "}, "Alice"),
    ({"full_name": "Cher"}, "Cher"),
    ({"first_name": None, "full_name": "Prince Nelson"}, "Prince"),
])
def test_restore_names_parametrized_success(
    input_user: Dict[str, Any],
    expected_first_name: str
) -> None:
    users = [input_user]
    restore_names(users)
    assert users[0]["first_name"] == expected_first_name


def test_restore_names_handles_empty_list() -> None:
    users: List[Dict[str, Any]] = []
    restore_names(users)
    assert users == []


def test_restore_names_handles_missing_or_empty_full_name() -> None:
    users = [
        {"full_name": ""},
        {"last_name": "Smith"},
        {"first_name": None}
    ]
    restore_names(users)
    assert "first_name" not in users[0]
    assert "first_name" not in users[1]
    assert users[2]["first_name"] is None


def test_restore_names_multiple_users_simultaneously() -> None:
    users = [
        {"first_name": None, "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
        {"first_name": "Existing", "full_name": "Ignore Me"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"
    assert users[2]["first_name"] == "Existing"


def test_restore_names_does_not_mutate_other_keys() -> None:
    user = {"last_name": "Doe", "full_name": "John Doe", "id": 1}
    restore_names([user])
    assert user == {
        "first_name": "John",
        "last_name": "Doe",
        "full_name": "John Doe",
        "id": 1
    }
