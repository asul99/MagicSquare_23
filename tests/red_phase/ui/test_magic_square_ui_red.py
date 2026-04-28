"""RED stubs: UI boundary (forms, prompts, views after entity/control).

Per .cursorrules: UI input is boundary; rules live in entity/control only.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.red_phase


def test_ui_input_adapter_passes_structured_board_to_control_red() -> None:
    """GREEN: UI adapter forwards a single structured 4x4 board to control."""
    received: list[list[list[int]]] = []

    def capture_control(board: list[list[int]]) -> None:
        received.append(board)

    from magic_square.ui.input_adapter import invoke_control_with_parsed_board_rows

    rows = [
        "1 2 3 4",
        "5 6 7 8",
        "9 10 11 12",
        "13 14 15 0",
    ]
    invoke_control_with_parsed_board_rows(rows, control=capture_control)

    assert received == [
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    ]


def test_ui_displays_error_message_literal_from_boundary_red() -> None:
    pytest.fail("RED: ui - show boundary message string verbatim (no domain rewording)")
