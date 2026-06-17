"""CLI-style row input → structured 4×4 board → control (no domain rules here)."""

from __future__ import annotations

from collections.abc import Callable, Sequence

_GRID_SIZE: int = 4


def parse_whitespace_rows_to_board(rows: Sequence[str]) -> list[list[int]]:
    """Parse exactly four whitespace-separated integer rows into a 4×4 grid.

    Args:
        rows: Four strings, each containing four integers separated by ASCII
            whitespace.

    Returns:
        A ``list`` of four rows, each a ``list`` of four ``int`` values.

    Raises:
        ValueError: If the row count is not four or any row does not parse to
            exactly four integers.
    """
    if len(rows) != _GRID_SIZE:
        raise ValueError(f"expected {_GRID_SIZE} rows, got {len(rows)}")
    board: list[list[int]] = []
    for raw in rows:
        parts = raw.split()
        if len(parts) != _GRID_SIZE:
            raise ValueError(
                f"expected {_GRID_SIZE} integers per row, got {len(parts)}"
            )
        board.append([int(p) for p in parts])
    return board


def invoke_control_with_parsed_board_rows(
    rows: Sequence[str],
    *,
    control: Callable[[list[list[int]]], None],
) -> None:
    """Parse UI rows, then invoke ``control`` with only the structured board.

    The control callable receives a single argument: ``board: list[list[int]]``
    shaped 4×4. No other side data is passed on this code path.

    Args:
        rows: Same contract as :func:`parse_whitespace_rows_to_board`.
        control: Use-case entry (Facade or control layer) accepting the board
            only.
    """
    board = parse_whitespace_rows_to_board(rows)
    control(board)
