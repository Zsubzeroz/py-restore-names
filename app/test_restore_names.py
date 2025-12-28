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


def test_restore_names_handles_explicit_none_value() -> None:
    users: List[Dict[str, Any]] = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_handles_missing_first_name_key() -> None:
    users: List[Dict[str, Any]] = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert "first_name" in users[0]
    assert users[0]["first_name"] == "Mike"


def test_restore_names_preserves_existing_first_name() -> None:
    users: List[Dict[str, Any]] = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "Jack Doe",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "John"


def test_restore_names_modifies_list_in_place() -> None:
    user: Dict[str, Any] = {"full_name": "Alice Smith"}
    users: List[Dict[str, Any]] = [user]
    restore_names(users)
    assert users[0] is user
    assert user["first_name"] == "Alice"


def test_restore_names_with_empty_list() -> None:
    users: List[Dict[str, Any]] = []
    restore_names(users)
    assert users == []


def test_restore_names_ignores_empty_or_whitespace_full_name() -> None:
    users: List[Dict[str, Any]] = [
        {"full_name": ""},
        {"full_name": "   "}
    ]
    restore_names(users)
    assert "first_name" not in users[0]
    assert "first_name" not in users[1]


def test_restore_names_ignores_non_string_full_name() -> None:
    users: List[Dict[str, Any]] = [
        {"full_name": None},
        {"full_name": 123}
    ]
    restore_names(users)
    assert "first_name" not in users[0]
    assert "first_name" not in users[1]


def test_restore_names_with_complex_whitespace() -> None:
    users: List[Dict[str, Any]] = [{"full_name": "  Dave   Miller  "}]
    restore_names(users)
    assert users[0]["first_name"] == "Dave"


def test_restore_names_with_multiple_records() -> None:
    users: List[Dict[str, Any]] = [
        {"first_name": None, "full_name": "Alice Smith"},
        {"full_name": "Bob Builder"},
        {"first_name": "Charlie", "full_name": "Charles Xavier"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"
    assert users[1]["first_name"] == "Bob"
    assert users[2]["first_name"] == "Charlie"


@pytest.mark.parametrize("input_data,expected", [
    ({"first_name": None, "full_name": "Jack Holy"}, "Jack"),
    ({"full_name": "Mike Adams"}, "Mike"),
    ({"full_name": "Cher"}, "Cher"),
])
def test_restore_names_parametrized(
    input_data: Dict[str, Any],
    expected: str
) -> None:
    users = [input_data]
    restore_names(users)
    assert users[0]["first_name"] == expected
