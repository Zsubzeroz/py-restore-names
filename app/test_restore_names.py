from typing import List, Dict, Any


def restore_names(users: List[Dict[str, Any]]) -> None:
    for user in users:
        if user.get("first_name") is None:
            full_name = user.get("full_name", "")
            if full_name:
                user["first_name"] = full_name.split()[0]


def test_restore_names_with_explicit_none_value() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_with_missing_first_name_key() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"


def test_restore_names_should_not_touch_existing_names() -> None:
    users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "John Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_is_in_place_modification() -> None:
    user: Dict[str, Any] = {"full_name": "Jack Holy"}
    users = [user]
    restore_names(users)
    assert users[0] is user
    assert user["first_name"] == "Jack"


def test_restore_names_empty_list() -> None:
    users: List[Dict[str, Any]] = []
    restore_names(users)
    assert users == []


def test_restore_names_multiple_users() -> None:
    users = [
        {"first_name": None, "full_name": "Alice Wonderland"},
        {"full_name": "Bob Builder"},
        {"first_name": "Charlie", "full_name": "Charles Xavier"}
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Alice"
    assert users[1]["first_name"] == "Bob"
    assert users[2]["first_name"] == "Charlie"


def test_restore_names_single_word_full_name() -> None:
    users = [{"full_name": "Cher"}]
    restore_names(users)
    assert users[0]["first_name"] == "Cher"
