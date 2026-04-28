"""Boundary: input validation and delegation toward domain (no PyQt here)."""

from __future__ import annotations

from typing import Any

from magicsquare.constants import EMPTY_CELL_VALUE, MATRIX_SIZE, SOLUTION_VECTOR_SIZE
from magicsquare.domain import find_blank_coords


def validate_grid_input(grid: Any) -> None:
    """Reject inputs that are not a ``MATRIX_SIZE``×``MATRIX_SIZE`` int grid.

    Args:
        grid: Candidate board structure from UI or adapters.

    Raises:
        ValueError: If the top-level length is not ``MATRIX_SIZE``, any row
            length is not ``MATRIX_SIZE``, or a cell is not an ``int``.
    """
    if not isinstance(grid, list):
        raise ValueError(f"Grid must be {MATRIX_SIZE}x{MATRIX_SIZE}.")
    if len(grid) != MATRIX_SIZE:
        raise ValueError(f"Grid must be {MATRIX_SIZE}x{MATRIX_SIZE}.")
    for row in grid:
        if not isinstance(row, list) or len(row) != MATRIX_SIZE:
            raise ValueError(f"Grid must be {MATRIX_SIZE}x{MATRIX_SIZE}.")
        for cell in row:
            if not isinstance(cell, int):
                raise ValueError(f"Grid must be {MATRIX_SIZE}x{MATRIX_SIZE}.")


def solve(grid: list[list[int]]) -> list[int]:
    """Validate and return an ``int[6]`` placeholder solution vector.

    This MVP implementation only identifies the two blank coordinates (0 cells)
    and returns them in the fixed output shape:
    ``[r1, c1, n1, r2, c2, n2]``.
    The numbers ``n1`` and ``n2`` are currently returned as ``0``.

    Args:
        grid: Candidate grid from UI or adapters.

    Returns:
        A 6-element vector: ``[r1, c1, 0, r2, c2, 0]``.

    Raises:
        ValueError: If the grid is not ``MATRIX_SIZE``×``MATRIX_SIZE`` or does
            not contain exactly two blanks.
    """
    validate_grid_input(grid)
    blanks = find_blank_coords(grid)
    if len(blanks) != 2:
        raise ValueError("Exactly two cells must be empty (value 0).")
    (r1, c1), (r2, c2) = blanks
    result = [r1, c1, EMPTY_CELL_VALUE, r2, c2, EMPTY_CELL_VALUE]
    if len(result) != SOLUTION_VECTOR_SIZE:
        raise ValueError("Internal error: invalid solution vector size.")
    return result
