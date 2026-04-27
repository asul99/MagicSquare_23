"""Tests for ``magic_square.entity.user``."""

import pytest

from magic_square.entity.user import (
    DISPLAY_NAME_MAX_LENGTH,
    USER_ID_MAX_LENGTH,
    User,
    UserValidationError,
    create_user,
    validate_display_name,
    validate_user_id,
)


def test_create_user_strips_whitespace() -> None:
    user = create_user("  alice_1  ", "  Alice  ")
    assert user.user_id == "alice_1"
    assert user.display_name == "Alice"


def test_create_user_valid_minimal() -> None:
    user = create_user("a", "B")
    assert user == User(user_id="a", display_name="B")


def test_create_user_rejects_empty_user_id_after_strip() -> None:
    with pytest.raises(UserValidationError, match="user_id must not be empty"):
        create_user("   ", "Name")


def test_create_user_rejects_empty_display_name_after_strip() -> None:
    with pytest.raises(UserValidationError, match="display_name must not be empty"):
        create_user("valid_id", "  \t  ")


def test_validate_user_id_rejects_invalid_characters() -> None:
    with pytest.raises(UserValidationError, match="letters, digits"):
        validate_user_id("bad id")


def test_validate_user_id_rejects_too_long() -> None:
    too_long = "x" * (USER_ID_MAX_LENGTH + 1)
    with pytest.raises(UserValidationError, match="at most"):
        validate_user_id(too_long)


def test_validate_display_name_rejects_too_long() -> None:
    too_long = "n" * (DISPLAY_NAME_MAX_LENGTH + 1)
    with pytest.raises(UserValidationError, match="at most"):
        validate_display_name(too_long)


def test_user_is_frozen() -> None:
    user = create_user("u1", "One")
    with pytest.raises(AttributeError):
        user.user_id = "u2"  # type: ignore[misc]
