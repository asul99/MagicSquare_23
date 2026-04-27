"""Domain entity for an application user (MagicSquare context).

This module is entity-layer only: no I/O, frameworks, or UI dependencies.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

# Single source of truth for user field limits (see .cursorrules: no magic numbers).
USER_ID_PATTERN: re.Pattern[str] = re.compile(r"^[A-Za-z0-9_-]+\Z")
USER_ID_MIN_LENGTH: int = 1
USER_ID_MAX_LENGTH: int = 64
DISPLAY_NAME_MIN_LENGTH: int = 1
DISPLAY_NAME_MAX_LENGTH: int = 80


class UserValidationError(ValueError):
    """Raised when ``User`` invariants are violated."""


@dataclass(frozen=True, slots=True)
class User:
    """Immutable identity for a person using MagicSquare.

    Attributes:
        user_id: Stable account identifier (slug-style, ASCII).
        display_name: Human-readable name shown in the app.
    """

    user_id: str
    display_name: str


def validate_user_id(user_id: str) -> None:
    """Validate ``user_id`` against length and character rules.

    Args:
        user_id: Candidate identifier (already normalized if from ``create_user``).

    Raises:
        UserValidationError: If the value is empty, too long, or uses disallowed
            characters.
    """
    if len(user_id) < USER_ID_MIN_LENGTH:
        raise UserValidationError("user_id must not be empty.")
    if len(user_id) > USER_ID_MAX_LENGTH:
        raise UserValidationError(
            f"user_id must be at most {USER_ID_MAX_LENGTH} characters."
        )
    if not USER_ID_PATTERN.match(user_id):
        raise UserValidationError(
            "user_id may contain only letters, digits, underscore, and hyphen."
        )


def validate_display_name(display_name: str) -> None:
    """Validate ``display_name`` length after trimming.

    Args:
        display_name: Candidate display name (caller should strip if needed).

    Raises:
        UserValidationError: If the value is empty or too long.
    """
    if len(display_name) < DISPLAY_NAME_MIN_LENGTH:
        raise UserValidationError("display_name must not be empty.")
    if len(display_name) > DISPLAY_NAME_MAX_LENGTH:
        raise UserValidationError(
            f"display_name must be at most {DISPLAY_NAME_MAX_LENGTH} characters."
        )


def create_user(user_id: str, display_name: str) -> User:
    """Build a ``User`` after normalizing and validating inputs.

    Leading and trailing whitespace is removed from both fields before checks.

    Args:
        user_id: Raw identifier from configuration or boundary layer.
        display_name: Raw display name from configuration or boundary layer.

    Returns:
        A frozen ``User`` value object.

    Raises:
        UserValidationError: If either field violates domain rules.
    """
    normalized_id = user_id.strip()
    normalized_name = display_name.strip()
    validate_user_id(normalized_id)
    validate_display_name(normalized_name)
    return User(user_id=normalized_id, display_name=normalized_name)
