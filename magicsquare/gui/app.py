"""PyQt6 GUI for MagicSquare (Screen layer only).

Business rules must stay in domain; validation/delegation in boundary.
"""

from __future__ import annotations

from typing import Final

from magicsquare.boundary import solve, validate_grid_input
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

    header = QLabel("Enter a 4×4 grid (0 means empty). Exactly two zeros are required.")
    header.setWordWrap(True)
    outer.addWidget(header)

    grid_widget = QWidget()
    grid_layout = QGridLayout(grid_widget)
    cells: list[list[QSpinBox]] = []

    for r in range(MATRIX_SIZE):
        row: list[QSpinBox] = []
        for c in range(MATRIX_SIZE):
            spin = QSpinBox()
            spin.setRange(MIN_CELL_VALUE, MAX_CELL_VALUE)
            spin.setAlignment(Qt.AlignmentFlag.AlignCenter)
            spin.setFixedWidth(70)
            grid_layout.addWidget(spin, r, c)
            row.append(spin)
        cells.append(row)

    outer.addWidget(grid_widget)

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

    def on_solve_clicked() -> None:
        board = read_board()
        try:
            validate_grid_input(board)
            vec = solve(board)
        except ValueError as exc:
            QMessageBox.critical(window, "Input error", str(exc))
            result_label.setText("Result: (error)")
            return
        result_label.setText(f"Result: {vec}")

    solve_button.clicked.connect(on_solve_clicked)

    window.setCentralWidget(root)
    window.resize(520, 360)
    window.show()

    app.exec()

