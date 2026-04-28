# Magic Square (4×4) — 가상환경 평가 방법·RED 레이아웃 후속 세션 보내기 보고서

**보내기 일자:** 2026-04-28  
**산출물 유형:** Cursor 세션에서 수행한 **`Reporter/21` 보강**, **RED 스텁 ECB 정렬 디렉터리**, **Reporter 아카이브**용 본 보고서  
**선행 보고서:** [`Reporter/21`](21_magic-square-d2-tc-red-branch-github-session-export-report.md) (실습·평가 SoT), [`Reporter/22`](22_magic-square-reporter21-venv-red-phase-follow-up-session-export-report.md) (RED·venv 후속 원안)

---

## 1. 보내기 요약

| 구분 | 내용 |
|------|------|
| **요청 맥락** | 가상환경에서의 **평가(검증) 방법** 안내; RED 테스트를 **boundary / logic / ui**로 나누어도 되는지에 대한 정합 구현; 본 세션 작업의 **Reporter보내기** |
| **문서** | `Reporter/21`에 **§0.3a 가상환경에서 평가(검증) 방법** 추가 — 실행 경로 확인, GREEN·전체 스위트·TC 추적성·RED 스텁·커버리지(선택) 기준 표, 실패 시 제출물 안내, 자기점검 한 줄 요약 |
| **코드** | `tests/red_phase/`를 `logic/`(entity·User 8건 + control 3건), `boundary/`(4건), `ui/`(2건)로 분리; 루트의 단일 `test_user_entity_red.py` 제거; `pytest.fail` 메시지는 콘솔 인코딩 안정을 위해 ASCII 위주 |
| **설정** | `pyproject.toml`의 `red_phase` 마커 설명을 `tests/red_phase/{logic,boundary,ui}` 경로에 맞게 갱신 |
| **검증** | 기본: `pytest tests -q` → **8 passed, 17 deselected**; RED만: `pytest -m red_phase tests/red_phase -q` → **17 failed** (의도적) |

---

## 2. ECB와 폴더 이름의 대응

| 사용자 친화 이름 | ECB 역할(`.cursorrules` 요지) |
|------------------|-------------------------------|
| **`logic/`** | **entity + control** — 순수 도메인 규칙·유스케이스 조합 |
| **`boundary/`** | **boundary** — FR-01·`errorCode`·전문 `message`·외부 계약 |
| **`ui/`** | **boundary의 일부** — 입력·표현 어댑터(얇게; 도메인 규칙 없음) |

공식 패키지 트리가 `entity/`·`control/`·`boundary/`로 갈라지면, 테스트도 동일 이름으로 옮기면 된다. 본 세션의 `logic/`은 교육·탐색용 묶음이다.

---

## 3. 작업 목록(파일 단위)

| 경로 | 작업 |
|------|------|
| [`Reporter/21_magic-square-d2-tc-red-branch-github-session-export-report.md`](21_magic-square-d2-tc-red-branch-github-session-export-report.md) | §0.3a 평가 표·변경 이력; RED 경로 문구를 `logic\|boundary\|ui`로 정리 |
| [`Reporter/22_magic-square-reporter21-venv-red-phase-follow-up-session-export-report.md`](22_magic-square-reporter21-venv-red-phase-follow-up-session-export-report.md) | RED 파일 경로 표를 하위 디렉터리 기준으로 갱신 |
| [`tests/red_phase/__init__.py`](../tests/red_phase/__init__.py) | 레이아웃 docstring(영문) |
| [`tests/red_phase/logic/`](../tests/red_phase/logic/) | `test_user_entity_red.py`, `test_magic_square_control_red.py` |
| [`tests/red_phase/boundary/`](../tests/red_phase/boundary/) | `test_magic_square_boundary_red.py` |
| [`tests/red_phase/ui/`](../tests/red_phase/ui/) | `test_magic_square_ui_red.py` |
| [`pyproject.toml`](../pyproject.toml) | `markers.red_phase` 한 줄 설명 |

*(이전 루트 `tests/red_phase/test_user_entity_red.py`는 삭제됨.)*

---

## 4. 가상환경에서 평가할 때 쓰는 명령(요약)

상세 표는 [`Reporter/21` §0.3a](21_magic-square-d2-tc-red-branch-github-session-export-report.md)를 따른다.

1. `.\.venv\Scripts\Activate.ps1`  
2. `python -c "import sys; print(sys.executable)"` — 경로에 `.venv` 포함 여부  
3. `pytest tests\entity -q` — GREEN  
4. `pytest tests -q` — 전체(기본 설정 시 `red_phase` deselect)  
5. `pytest -m red_phase tests\red_phase -q` — RED 스텁 전부 실패(스켈레톤 유지 시)

---

## 5. 연계·원격

| 항목 | 링크·경로 |
|------|-----------|
| 저장소 | [asul99/MagicSquare_23](https://github.com/asul99/MagicSquare_23) (`https://github.com/asul99/MagicSquare_23.git`) |
| TC 샘플 | [`docs/TC_D2_unit_magic_square_entity_user_sample.md`](../docs/TC_D2_unit_magic_square_entity_user_sample.md) |
| PRD | [`docs/PRD_MagicSquare_4x4_TDD.md`](../docs/PRD_MagicSquare_4x4_TDD.md) |

---

## 6. 후속 권장(선택)

- `README.md` 문서 맵에 **`Reporter/23`** 한 줄 추가.  
- `Reporter/22` §4 표의 “8 실패” 문구는 본 세션 이후 **17건** RED가 되므로, 링크만 `Reporter/23`으로 넘기거나 `Reporter/22` 표를 숫자만 수정한다.

---

## 7. 변경 이력(Reporter)

| 일자 | 내용 |
|------|------|
| 2026-04-28 | 초안: 가상환경 평가 §0.3a·RED `logic/boundary/ui` 분리·`pyproject.toml`·연계 정리 (`Reporter/23`) |
