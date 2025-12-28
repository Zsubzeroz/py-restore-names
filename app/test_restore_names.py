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


def test_restore_names_handles_explicit_none() -> None:
    users = [{"first_name": None, "full_name": "Jack Holy"}]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_handles_missing_key() -> None:
    users = [{"full_name": "Mike Adams"}]
    restore_names(users)
    assert "first_name" in users[0]
    assert users[0]["first_name"] == "Mike"


def test_restore_names_does_not_overwrite_existing() -> None:
    users = [{"first_name": "John", "full_name": "Jack Doe"}]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_restore_names_is_inplace_modification() -> None:
    user: Dict[str, Any] = {"full_name": "Alice Smith"}
    users = [user]
    restore_names(users)
    assert users[0] is user
    assert user["first_name"] == "Alice"


def test_restore_names_handles_empty_list() -> None:
    users: List[Dict[str, Any]] = []
    restore_names(users)
    assert users == []


def test_restore_names_handles_complex_whitespace() -> None:
    users = [{"full_name": "  Dave   Miller  "}]
    restore_names(users)
    assert users[0]["first_name"] == "Dave"


def test_restore_names_ignores_invalid_full_names() -> None:
    users = [
        {"full_name": ""},
        {"full_name": "   "},
        {"full_name": None},
        {"first_name": None, "full_name": 123}
    ]
    restore_names(users)
    assert "first_name" not in users[0]
    assert "first_name" not in users[1]
    assert "first_name" not in users[2]
    assert users[3]["first_name"] is None


@pytest.mark.parametrize("user_data, expected", [
    ({"first_name": None, "full_name": "Jack Holy"}, "Jack"),
    ({"full_name": "Mike Adams"}, "Mike"),
])
def test_restore_names_parametrized_cases(
    user_data: Dict[str, Any],
    expected: str
) -> None:
    users = [user_data]
    restore_names(users)
    assert users[0]["first_name"] == expected
