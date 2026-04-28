"""RED stubs for ``magic_square.entity.user`` (TDD RED before GREEN).

Maps 1:1 to ``docs/TC_D2_unit_magic_square_entity_user_sample.md`` test-step rows
and ``Reporter/21_magic-square-d2-tc-red-branch-github-session-export-report.md``.

* Default ``pytest`` skips these (``-m "not red_phase"`` in ``pyproject.toml``).
* Run intentional failures: ``pytest -m red_phase`` (from repo root).
* GREEN reference implementation: ``tests/entity/test_user.py``.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.red_phase


def test_create_user_strips_whitespace() -> None:
    pytest.fail("RED: TC - create_user strips user_id and display_name whitespace")


def test_create_user_valid_minimal() -> None:
    pytest.fail("RED: TC - minimal valid create_user returns User")


def test_create_user_rejects_empty_user_id_after_strip() -> None:
    pytest.fail("RED: TC - empty user_id after strip raises UserValidationError")


def test_create_user_rejects_empty_display_name_after_strip() -> None:
    pytest.fail("RED: TC - empty display_name after strip raises UserValidationError")


def test_validate_user_id_rejects_invalid_characters() -> None:
    pytest.fail("RED: TC - invalid user_id characters raise UserValidationError")


def test_validate_user_id_rejects_too_long() -> None:
    pytest.fail("RED: TC - user_id over max length raises UserValidationError")


def test_validate_display_name_rejects_too_long() -> None:
    pytest.fail("RED: TC - display_name over max length raises UserValidationError")


def test_user_is_frozen() -> None:
    pytest.fail("RED: TC - User dataclass must be frozen (no field reassignment)")
