"""Pure domain entities: rules, validation, and value objects."""

from magic_square.entity.user import (
    User,
    UserValidationError,
    create_user,
    validate_display_name,
    validate_user_id,
)

__all__ = [
    "User",
    "UserValidationError",
    "create_user",
    "validate_display_name",
    "validate_user_id",
]
