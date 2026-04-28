"""Pure domain rules: no UI, DB, web, or PyQt imports."""

from __future__ import annotations

from magicsquare.constants import MATRIX_SIZE


def find_blank_coords(board: list[list[int]]) -> list[tuple[int, int]]:
    """Return the two empty cells in row-major order using 1-based coordinates.

    Args:
        board: A ``MATRIX_SIZE``×``MATRIX_SIZE`` grid where ``0`` marks an empty
            cell. Callers should ensure exactly two zeros; behaviour is otherwise
            undefined for this minimal implementation.

    Returns:
        Two ``(row, col)`` pairs, each 1-based, first cell first in row-major scan.
    """
    found: list[tuple[int, int]] = []
    for r in range(MATRIX_SIZE):
        for c in range(MATRIX_SIZE):
            if board[r][c] == 0:
                found.append((r + 1, c + 1))
    return found
