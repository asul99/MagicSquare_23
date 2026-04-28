"""RED stubs: UI boundary (forms, prompts, views after entity/control).

Per .cursorrules: UI input is boundary; rules live in entity/control only.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.red_phase


def test_ui_input_adapter_passes_structured_board_to_control_red() -> None:
    pytest.fail("RED: ui - input adapter passes only structured board to Facade/control")


def test_ui_displays_error_message_literal_from_boundary_red() -> None:
    pytest.fail("RED: ui - show boundary message string verbatim (no domain rewording)")
