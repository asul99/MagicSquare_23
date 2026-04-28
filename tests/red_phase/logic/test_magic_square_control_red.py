"""RED stubs: control layer (use-case orchestration before Facade).

Align with PRD and Reporter/18 TASKs; keep RED-only until implemented.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.red_phase


def test_control_orchestrates_empty_cell_then_missing_then_completion_red() -> None:
    pytest.fail("RED: control - US-003/004 flow FR-02..05 then completion decision")


def test_control_two_attempts_second_only_if_needed_red() -> None:
    pytest.fail("RED: control - FR-05 two attempts; second attempt only when required")


def test_control_no_domain_call_from_boundary_validator_track_red() -> None:
    pytest.fail("RED: control/boundary - Track A validation must not call domain (PRD sec 8)")
