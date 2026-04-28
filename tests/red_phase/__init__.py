"""RED-phase TDD stubs (``pytest.mark.red_phase``).

Layout (ECB-aligned; informal folder names):

- ``logic/`` -- entity and control: domain rules and use-case flow (pure logic).
- ``boundary/`` -- external contract, Facade, errorCode, message (e.g. PRD FR-01).
- ``ui/`` -- user input and presentation (thin adapters; no domain rules).

Default ``pytest`` excludes this tree via ``pyproject.toml`` ``-m "not red_phase"``.
"""
