"""Dual-Track commit: L-RED-01 (domain blanks) + U-RED-01 (boundary shape)."""

from __future__ import annotations

import pytest

from magicsquare.boundary import validate_grid_input
from magicsquare.constants import MATRIX_SIZE
from magicsquare.domain import find_blank_coords


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
