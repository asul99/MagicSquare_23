"""Dual-Track commit: L-RED-01 (domain blanks) + U-RED-01 (boundary shape)."""

from __future__ import annotations

import pytest

from magicsquare.boundary import get_line_sums, solve, validate_grid_input
from magicsquare.constants import MATRIX_SIZE
from magicsquare.domain import find_blank_coords, is_magic_square_complete, magic_constant


def test_l_red_01_find_blank_coords_row_major_two_cells() -> None:
    """L-RED-01: two zeros yield coordinates in row-major order (1-based)."""
    board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 0, 12],
        [13, 14, 15, 0],
    ]
    assert len(board) == MATRIX_SIZE
    assert find_blank_coords(board) == [(3, 3), (4, 4)]


@pytest.mark.parametrize(
    "bad_grid",
    [
        [[1, 2], [3, 4]],
        [[1] * MATRIX_SIZE] * (MATRIX_SIZE - 1),
        [[1] * (MATRIX_SIZE + 1)] * MATRIX_SIZE,
    ],
)
def test_u_red_01_validate_raises_when_not_4x4(bad_grid: list) -> None:
    """U-RED-01: non-``MATRIX_SIZE``×``MATRIX_SIZE`` input raises ``ValueError``."""
    with pytest.raises(ValueError, match=str(MATRIX_SIZE)):
        validate_grid_input(bad_grid)


def test_solve_fills_two_blanks_to_complete_magic_square() -> None:
    board = [
        [16, 2, 3, 13],
        [5, 11, 10, 8],
        [9, 7, 0, 12],
        [4, 14, 15, 0],
    ]
    vec = solve(board)
    assert len(vec) == 6
    r1, c1, n1, r2, c2, n2 = vec
    filled = [row[:] for row in board]
    filled[r1 - 1][c1 - 1] = n1
    filled[r2 - 1][c2 - 1] = n2
    assert magic_constant() > 0
    assert is_magic_square_complete(filled)


def test_default_complete_board_has_equal_row_col_diag_sums() -> None:
    board = [
        [16, 2, 3, 13],
        [5, 11, 10, 8],
        [9, 7, 6, 12],
        [4, 14, 15, 1],
    ]
    sums = get_line_sums(board)
    assert sums == {
        "rows": [34, 34, 34, 34],
        "cols": [34, 34, 34, 34],
        "diags": [34, 34],
    }
