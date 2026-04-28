"""Pure domain rules: no UI, DB, web, or PyQt imports."""

from __future__ import annotations

from magicsquare.constants import (
    EMPTY_CELL_VALUE,
    MATRIX_SIZE,
    MAX_CELL_VALUE,
    MIN_CELL_VALUE,
)


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


def magic_constant() -> int:
    """Return the magic sum for the current ``MATRIX_SIZE``.

    For a normal magic square using values 1..n^2, the constant is:
    M = n(n^2 + 1) / 2.
    """
    n = MATRIX_SIZE
    return (n * (n * n + 1)) // 2


def is_magic_square_complete(board: list[list[int]]) -> bool:
    """Check whether all rows/cols/diagonals sum to the magic constant."""
    target = magic_constant()
    n = MATRIX_SIZE
    if any(len(row) != n for row in board) or len(board) != n:
        return False

    for r in range(n):
        if sum(board[r]) != target:
            return False
    for c in range(n):
        if sum(board[r][c] for r in range(n)) != target:
            return False

    if sum(board[i][i] for i in range(n)) != target:
        return False
    if sum(board[i][n - 1 - i] for i in range(n)) != target:
        return False
    return True


def line_sums(board: list[list[int]]) -> dict[str, list[int]]:
    """Return row, column, and diagonal sums for a square board."""
    n = MATRIX_SIZE
    return {
        "rows": [sum(board[r]) for r in range(n)],
        "cols": [sum(board[r][c] for r in range(n)) for c in range(n)],
        "diags": [
            sum(board[i][i] for i in range(n)),
            sum(board[i][n - 1 - i] for i in range(n)),
        ],
    }


def solve_two_blanks(board: list[list[int]]) -> list[int]:
    """Solve a 4×4 board with exactly two blanks (0).

    Returns the fixed 6-element vector: ``[r1,c1,n1,r2,c2,n2]`` with 1-based
    coordinates. The blank order is row-major (first 0 encountered first).

    This implementation tries the two permutations of the missing numbers and
    accepts the one that yields a completed magic square (all sums equal).
    """
    blanks = find_blank_coords(board)
    if len(blanks) != 2:
        raise ValueError("Exactly two cells must be empty (value 0).")

    n = MATRIX_SIZE
    seen: set[int] = set()
    for r in range(n):
        for c in range(n):
            v = board[r][c]
            if v < MIN_CELL_VALUE or v > MAX_CELL_VALUE:
                raise ValueError("Each cell must be 0 or an integer from 1 to 16.")
            if v == EMPTY_CELL_VALUE:
                continue
            if v in seen:
                raise ValueError("Non-zero values must not repeat.")
            seen.add(v)

    all_values = set(range(1, n * n + 1))
    missing = sorted(all_values - seen)
    if len(missing) != 2:
        raise ValueError("Exactly two cells must be empty (value 0).")

    (r1, c1), (r2, c2) = blanks
    candidates = [
        (missing[0], missing[1]),
        (missing[1], missing[0]),
    ]

    for n1, n2 in candidates:
        filled = [row[:] for row in board]
        filled[r1 - 1][c1 - 1] = n1
        filled[r2 - 1][c2 - 1] = n2
        if is_magic_square_complete(filled):
            return [r1, c1, n1, r2, c2, n2]

    raise ValueError("No valid magic-square completion exists for this grid.")
