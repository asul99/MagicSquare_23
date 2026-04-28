"""RED stubs: boundary -- FR-01 board validation, BR-ERR contracts (Track A).

Match full message strings and errorCode to PRD docs/PRD_MagicSquare_4x4_TDD.md and README table.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.red_phase


def test_boundary_invalid_grid_size_error_contract_red() -> None:
    pytest.fail("RED: boundary - INVALID_GRID_SIZE / Grid must be 4x4.")


def test_boundary_invalid_empty_cell_count_error_contract_red() -> None:
    pytest.fail(
        "RED: boundary - INVALID_EMPTY_CELL_COUNT / Exactly two cells must be empty (value 0)."
    )


def test_boundary_no_solution_error_contract_red() -> None:
    pytest.fail("RED: boundary - NO_SOLUTION / No valid magic-square completion exists for this grid.")


def test_boundary_success_int6_vector_contract_red() -> None:
    pytest.fail("RED: boundary - success returns int[6] vector [r1,c1,n1,r2,c2,n2] 1-index (FR-05)")
