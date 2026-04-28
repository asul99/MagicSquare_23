# Magic Square (4×4) — Reporter/21 보강·가상환경 안내·RED 스텁 후속 세션 보내기 보고서

**보내기 일자:** 2026-04-28  
**산출물 유형:** Cursor 후속 세션에서 수행한 **문서 개정**, **pytest 설정·RED 단계 테스트 코드** 추가, **Reporter 아카이브**용 본 보고서  
**선행 보고서:** [`Reporter/21_magic-square-d2-tc-red-branch-github-session-export-report.md`](21_magic-square-d2-tc-red-branch-github-session-export-report.md) (D2 TC·`red` 브랜치·GitHub 세션 원안 및 실습 가이드 SoT)

---

## 1. 보내기 요약

| 구분 | 내용 |
|------|------|
| **요청 맥락** | `Reporter/21`을 참조한 실습 가능 보강, 가상환경(venv) 기준 실행 안내, TDD **RED** 스켈레톤 테스트, 위 작업 내용의 **Reporter보내기** |
| **문서 변경** | `Reporter/21` — §0 실습 가이드 확장(venv §0.2, pytest §0.3, Git §0.5 등), 복사용 venv 요약 블록, `pytest -m red_phase` 절차, 트러블슈팅·TC↔pytest 표·변경 이력 누적 |
| **코드·설정 변경** | `tests/red_phase/` — TC-MS-ENTITY-001 및 `test_user.py`와 동일한 **8개** 테스트명, 본문은 `pytest.fail`만; `pyproject.toml` — `markers.red_phase`, `addopts`로 기본 수집에서 RED 스텁 제외 |
| **검증** | 기본 `pytest`: GREEN 8건 통과·RED 8건 deselect; `pytest -m red_phase tests/red_phase`: 8건 의도적 실패 |

---

## 2. 작업 목록(파일 단위)

| 경로 | 작업 |
|------|------|
| [`Reporter/21_magic-square-d2-tc-red-branch-github-session-export-report.md`](21_magic-square-d2-tc-red-branch-github-session-export-report.md) | 실습 가이드 §0 전면 보강; venv 생성·활성화·의존성·`deactivate`; PowerShell 실행 정책; GREEN/RED pytest 명령; Git·트러블슈팅; 가상환경 **복사용 요약** 및 **RED 스텁** 실행 문단 추가 |
| [`tests/red_phase/__init__.py`](../tests/red_phase/__init__.py) | 패키지 초기화(짧은 모듈 설명) |
| [`tests/red_phase/test_user_entity_red.py`](../tests/red_phase/test_user_entity_red.py) | RED 스텁 8개, `pytestmark = pytest.mark.red_phase`, TC·Reporter/21 교차 참조 docstring |
| [`pyproject.toml`](../pyproject.toml) | `[tool.pytest.ini_options]`에 `addopts = ["-m", "not red_phase"]`, `markers`에 `red_phase` 설명 등록 |
| 본 파일 `Reporter/22_…` | 세션 산출 **보내기 보고서** |

**변경 없음(참고):** [`tests/entity/test_user.py`](../tests/entity/test_user.py) — GREEN 참조 구현 그대로 유지.

---

## 3. 설계 의도

1. **기본 CI·로컬 `pytest` 동작**  
   `addopts`로 `red_phase` 마크가 붙은 테스트를 기본 마커 표현식에서 제외하여, 문서 [`Reporter/21`](21_magic-square-d2-tc-red-branch-github-session-export-report.md) §0.3이 말하는 **GREEN 검증**(`pytest tests/entity` 등)이 **항상 통과**하도록 했다.

2. **교육용 RED**  
   동일 TC 행에 대응하는 함수명으로 `pytest.fail`만 두어, **RED → GREEN** 순서를 새 브랜치·새 클론에서도 재현할 수 있게 했다. GREEN 구현 복사는 `tests/entity/test_user.py`를 참고한다.

3. **가상환경**  
   전역 Python 오염을 피하고, 보고서 한 곳에서 **PowerShell + `.venv`** 기준으로 끝까지 따라 할 수 있게 정리했다.

---

## 4. 검증 명령(재현)

가상환경을 켠 뒤 저장소 루트에서 실행한다. (venv 없이면 `pytest` → `py -3 -m pytest`.)

| 목적 | 명령 |
|------|------|
| GREEN만 | `pytest tests/entity -q` 또는 `pytest tests -q` |
| RED 스텁만(8 실패 예상) | `pytest -m red_phase tests/red_phase -v` |
| 수집 확인 | `pytest tests/entity --collect-only -q` |

---

## 5. 연계 문서

| 문서·코드 | 관계 |
|-----------|------|
| [`Reporter/21`](21_magic-square-d2-tc-red-branch-github-session-export-report.md) | D2·TC·Git·venv·RED 실행의 **단일 실습 SoT**(지속 개정됨) |
| [`docs/TC_D2_unit_magic_square_entity_user_sample.md`](../docs/TC_D2_unit_magic_square_entity_user_sample.md) | TC 표지·테스트 단계·RED 스텁 함수명 1:1 근거 |
| [`docs/PRD_MagicSquare_4x4_TDD.md`](../docs/PRD_MagicSquare_4x4_TDD.md) | 마방진 본 기능 요구; TC 빈 양식 확장 시 참조 |

---

## 6. 후속 권장(선택)

- `README.md` 문서 맵에 **`Reporter/22`**(본 보고서) 한 줄을 추가해, `Reporter/21` 후속 코드·설정 변경 추적을 쉽게 한다.  
- 팀에서 RED 스텁을 기본 수집에 포함시키고 싶다면 `addopts`의 `not red_phase`를 제거하거나 별도 CI 잡으로 분리하는 정책을 문서화한다.

---

## 7. 변경 이력(Reporter)

| 일자 | 내용 |
|------|------|
| 2026-04-28 | 초안: `Reporter/21` 후속 세션 — venv·RED 스텁·`pyproject.toml`·검증·연계를 정리한보내기 보고서 (`Reporter/22`) |
