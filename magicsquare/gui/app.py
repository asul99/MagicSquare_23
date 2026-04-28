"""PyQt6 GUI for MagicSquare (Screen layer only).

Business rules must stay in domain; validation/delegation in boundary.
"""

from __future__ import annotations

from typing import Final

from magicsquare.boundary import get_line_sums, solve, validate_grid_input
from magicsquare.constants import MATRIX_SIZE, MAX_CELL_VALUE, MIN_CELL_VALUE


def main() -> None:
    """Run the GUI application."""
    from PyQt6.QtCore import Qt
    from PyQt6.QtWidgets import (
        QAbstractSpinBox,
        QApplication,
        QGridLayout,
        QHBoxLayout,
        QLabel,
        QMainWindow,
        QMessageBox,
        QPushButton,
        QSpinBox,
        QVBoxLayout,
        QWidget,
    )

    title: Final[str] = f"MagicSquare {MATRIX_SIZE}x{MATRIX_SIZE}"

    app = QApplication([])

    window = QMainWindow()
    window.setWindowTitle(title)

    root = QWidget()
    outer = QVBoxLayout(root)

    header = QLabel(
        "Default board has exactly two blanks (highlighted, value 0). "
        "Click any cell to type a new number (0-16). Click Solve to fill the blanks."
    )
    header.setWordWrap(True)
    outer.addWidget(header)

    grid_widget = QWidget()
    grid_layout = QGridLayout(grid_widget)
    cells: list[list[QSpinBox]] = []

    # A classic 4x4 magic square (sum 34) with two cells hidden as 0.
    # This is UI sample data only; domain rules remain in ``magicsquare.domain``.
    default_board = [
        [16, 2, 3, 13],
        [5, 11, 10, 8],
        [9, 7, 0, 12],
        [4, 14, 15, 0],
    ]

    for r in range(MATRIX_SIZE):
        row: list[QSpinBox] = []
        for c in range(MATRIX_SIZE):
            spin = QSpinBox()
            spin.setRange(MIN_CELL_VALUE, MAX_CELL_VALUE)
            spin.setAlignment(Qt.AlignmentFlag.AlignCenter)
            spin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
            spin.setFixedWidth(64)
            spin.setMinimumHeight(36)
            spin.setReadOnly(False)
            spin.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
            spin.setValue(default_board[r][c])
            grid_layout.addWidget(spin, r, c)
            row.append(spin)
        cells.append(row)

    outer.addWidget(grid_widget)

    sums_label = QLabel("")
    sums_label.setWordWrap(True)
    outer.addWidget(sums_label)

    actions = QWidget()
    actions_layout = QHBoxLayout(actions)
    solve_button = QPushButton("Solve")
    result_label = QLabel("Result: (not solved)")
    result_label.setWordWrap(True)
    actions_layout.addWidget(solve_button)
    actions_layout.addWidget(result_label, stretch=1)
    outer.addWidget(actions)

    base_style = "QSpinBox { font-size: 18px; padding: 2px; }"
    blank_style = (
        "QSpinBox { font-size: 18px; padding: 2px; "
        "background-color: #FFF59D; border: 1px solid #FBC02D; }"
    )

    def read_board() -> list[list[int]]:
        return [[cells[r][c].value() for c in range(MATRIX_SIZE)] for r in range(MATRIX_SIZE)]

    def refresh_cell_styles() -> None:
        for r in range(MATRIX_SIZE):
            for c in range(MATRIX_SIZE):
                spin = cells[r][c]
                spin.setStyleSheet(blank_style if spin.value() == 0 else base_style)

    def format_board_lines(board: list[list[int]], sums: dict[str, list[int]]) -> str:
        n = MATRIX_SIZE
        lines: list[str] = []
        for r in range(n):
            values = board[r]
            expression = " + ".join(str(v) for v in values)
            lines.append(f"  row {r + 1}: {expression} = {sums['rows'][r]}")
        for c in range(n):
            values = [board[r][c] for r in range(n)]
            expression = " + ".join(str(v) for v in values)
            lines.append(f"  col {c + 1}: {expression} = {sums['cols'][c]}")
        diag_main = [board[i][i] for i in range(n)]
        diag_anti = [board[i][n - 1 - i] for i in range(n)]
        lines.append(
            "  diag \\: "
            + " + ".join(str(v) for v in diag_main)
            + f" = {sums['diags'][0]}"
        )
        lines.append(
            "  diag /: "
            + " + ".join(str(v) for v in diag_anti)
            + f" = {sums['diags'][1]}"
        )
        return "\n".join(lines)

    def update_sums_label() -> None:
        board = read_board()
        sums = get_line_sums(board)
        sections: list[str] = ["Current visible board:", format_board_lines(board, sums)]
        try:
            vec = solve(board)
        except ValueError:
            sections.append("Solved preview: unavailable")
        else:
            r1, c1, n1, r2, c2, n2 = vec
            filled = [row[:] for row in board]
            filled[r1 - 1][c1 - 1] = n1
            filled[r2 - 1][c2 - 1] = n2
            preview = get_line_sums(filled)
            sections.append(
                f"Solved preview (fill ({r1},{c1})={n1}, ({r2},{c2})={n2}):"
            )
            sections.append(format_board_lines(filled, preview))
        sums_label.setText("\n".join(sections))

    def on_solve_clicked() -> None:
        board = read_board()
        try:
            validate_grid_input(board)
            vec = solve(board)
        except ValueError as exc:
            QMessageBox.critical(window, "Input error", str(exc))
            result_label.setText("Result: (error)")
            return
        r1, c1, n1, r2, c2, n2 = vec
        cells[r1 - 1][c1 - 1].setValue(n1)
        cells[r2 - 1][c2 - 1].setValue(n2)
        update_sums_label()
        result_label.setText(f"Result: {vec}")

    def on_value_changed(_value: int) -> None:
        update_sums_label()
        refresh_cell_styles()

    solve_button.clicked.connect(on_solve_clicked)
    for row in cells:
        for spin in row:
            spin.valueChanged.connect(on_value_changed)
            spin.lineEdit().selectAll()
    refresh_cell_styles()
    update_sums_label()

    window.setCentralWidget(root)
    window.resize(520, 360)
    window.show()

    app.exec()

