"""Boundary: input validation and delegation toward domain (no PyQt here)."""

from __future__ import annotations

from typing import Any

from magicsquare.constants import MATRIX_SIZE


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
