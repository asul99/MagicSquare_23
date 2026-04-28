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
        "Default board has exactly two blanks (0). "
        "Current sums use the visible 0s; solved-preview sums use the filled values."
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
            spin.setFixedWidth(70)
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

    def read_board() -> list[list[int]]:
        return [[cells[r][c].value() for c in range(MATRIX_SIZE)] for r in range(MATRIX_SIZE)]

    def update_sums_label() -> None:
        board = read_board()
        sums = get_line_sums(board)
        preview_text = "Solved preview: unavailable"
        try:
            vec = solve(board)
        except ValueError:
            pass
        else:
            r1, c1, n1, r2, c2, n2 = vec
            filled = [row[:] for row in board]
            filled[r1 - 1][c1 - 1] = n1
            filled[r2 - 1][c2 - 1] = n2
            preview = get_line_sums(filled)
            preview_text = (
                f"Solved preview rows {preview['rows']} / "
                f"cols {preview['cols']} / diags {preview['diags']}"
            )
        sums_label.setText(
            "Current visible sums: "
            f"rows {sums['rows']} / cols {sums['cols']} / diags {sums['diags']}\n"
            f"{preview_text}"
        )

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

    solve_button.clicked.connect(on_solve_clicked)
    for row in cells:
        for spin in row:
            spin.valueChanged.connect(update_sums_label)
    update_sums_label()

    window.setCentralWidget(root)
    window.resize(520, 360)
    window.show()

    app.exec()

