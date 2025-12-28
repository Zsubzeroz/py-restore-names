import pytest
from typing import List, Dict, Any


def restore_names(users: List[Dict[str, Any]]) -> None:
    for user in users:
        if user.get("first_name") is None:
            full_name = user.get("full_name")
            if isinstance(full_name, str) and full_name.strip():
                user["first_name"] = full_name.split()[0]


def test_restore_names_with_explicit_none() -> None:
    users = [{"first_name": None, "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_with_missing_key() -> None:
    users = [{"full_name": "Mike Adams"}]
    restore_names(users)
    assert "first_name" in users[0]
    assert users[0]["first_name"] == "Mike"


def test_restore_names_does_not_overwrite_existing() -> None:
    users = [{"first_name": "Jack", "full_name": "John Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_modifies_in_place() -> None:
    user: Dict[str, Any] = {"full_name": "Alice Wonderland"}
    users = [user]
    restore_names(users)
    assert users[0] is user
    assert user["first_name"] == "Alice"


def test_restore_names_handles_empty_list() -> None:
    users: List[Dict[str, Any]] = []
    restore_names(users)
    assert users == []


@pytest.mark.parametrize("user_data, expected_name", [
    ({"full_name": "  Bob   Builder "}, "Bob"),
    ({"first_name": None, "full_name": "Cher"}, "Cher"),
])
def test_restore_names_parametrized(
    user_data: Dict[str, Any],
    expected_name: str
) -> None:
    users = [user_data]
    restore_names(users)
    assert users[0]["first_name"] == expected_name


def test_restore_names_ignores_empty_full_name() -> None:
    users = [{"full_name": ""}, {"full_name": " "}]
    restore_names(users)
    assert "first_name" not in users[0]
    assert "first_name" not in users[1]
