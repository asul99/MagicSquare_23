# Test skeletons for RED principle
_Exported on 4/28/2026 at 14:16:45 GMT+9 from Cursor (3.2.11)_

---

**User**

레포 테스트 프레임워크 이름(JUnit 5, pytest 등)에 맞춰 파일/클래스 이름만 적은 테스트 스켈레톤(메서드 빈 본문, fail 또는 assertTrue(false) 한 줄)도 같은 RED 원칙으로만 적어봅니다.


---

**Cursor**

레포지토리의 테스트 프레임워크와 기존 테스트 구조를 확인 중입니다.



이 저장소는 **Python + pytest**(`pyproject.toml`, `tests/entity/test_user.py`) 기준이므로, RED만 만족하는 **이름 + 한 줄 실패** 스켈레톤은 아래처럼 두면 됩니다.

## pytest (본 레포와 동일)

**파일:** `tests/entity/test_user.py` (또는 모듈별 `tests/<mirror>/test_<module>.py`)

```python
"""Tests for ``magic_square.entity.user`` — RED skeleton."""

import pytest


def test_create_user_strips_whitespace() -> None:
    pytest.fail("RED")


def test_create_user_valid_minimal() -> None:
    pytest.fail("RED")


def test_create_user_rejects_empty_user_id_after_strip() -> None:
    pytest.fail("RED")


def test_create_user_rejects_empty_display_name_after_strip() -> None:
    pytest.fail("RED")


def test_validate_user_id_rejects_invalid_characters() -> None:
    pytest.fail("RED")


def test_validate_user_id_rejects_too_long() -> None:
    pytest.fail("RED")


def test_validate_display_name_rejects_too_long() -> None:
    pytest.fail("RED")


def test_user_is_frozen() -> None:
    pytest.fail("RED")
```

클래스 스타일을 쓸 때는 관례상 **`Test*` + `test_*` 메서드**입니다.

```python
import pytest


class TestUser:
    def test_create_user_strips_whitespace(self) -> None:
        pytest.fail("RED")
```

`pytest.fail(...)` 대신 **한 줄만** 쓰려면 `assert False`도 RED에 해당합니다.

---

## JUnit 5 (참고: PRD/다른 JVM 레포용 이름만)

**파일:** `UserTest.java` 또는 `test/java/.../UserTest.java`  
**클래스:** `UserTest`  
**메서드:** `@Test void createUserStripsWhitespace()` 등

```java
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.fail;

class UserTest {

    @Test
    void createUserStripsWhitespace() {
        fail("RED");
    }
}
```

`fail("RED")` 대신 `org.junit.jupiter.api.Assertions.assertTrue(false)` 한 줄도 동일한 RED 스켈레톤입니다.

---

정리하면, **이 레포에 맞추려면** `test_` 접두 함수(또는 `Test*` 클래스의 `test_*`)와 `pytest.fail("RED")` 또는 `assert False` 한 줄이 RED 스켈레톤에 가장 잘 맞습니다.

---

**User**

@Reporter/21_magic-square-d2-tc-red-branch-github-session-export-report.md 를 참조해 테스트 해 볼수 있도록 자세하게 다시 작성해줘

---

**Cursor**

보고서 전체를 읽고 실제로 따라 테스트할 수 있게 확장합니다.



보고서를 실습·검증 절차 중심으로 재작성합니다.



`Reporter/21_magic-square-d2-tc-red-branch-github-session-export-report.md`를 **직접 따라 하며 검증할 수 있게** 고쳐 두었습니다.

### 추가·강화한 내용

1. **§0 이 문서로 “직접 테스트”하기**  
   - Python 3.10+, `pip install -e ".[dev]"`, `pytest --version`  
   - `pytest tests\entity -q`, `-v`, `--collect-only`, `파일::함수` 단일 케이스 실행  
   - TC 문서를 열고 표 **비고** 열과 `test_*`를 맞춰 가며 확인하는 순서  

2. **Git 재현**  
   - `remote -v`, `fetch`, `status`, `branch -vv`, `HEAD` vs `origin/main`  
   - 세션에 나온 SHA는 **그때 기준 스냅샷**이라고 명시해, 나중에 달라져도 헷갈리지 않게 함  

3. **`red` 브랜치 선택 실습**  
   - `checkout -b`, `add`, `commit`, `push -u`, PR URL  

4. **트러블슈팅 표**  
   - pytest 미설치, `magic_square` import, 수집 실패  

5. **§5 보강**  
   - TC ↔ pytest **한 줄 실행 예** 표  

6. **§8 변경 이력**  
   - 이번 개정 항목 한 줄 추가  

기존 §1~§7의 세션 요약·브랜치 전략·문서 구조·연계·후속 권장은 유지하면서, 위 실습 절을 맨 앞에 두어 **문서만 읽지 않고 명령으로 끝까지 확인**할 수 있게 맞춰 두었습니다.

---

**User**

실행 방법을 가상환경 할 수 있도록 알려줘

---

**Cursor**

보고서 §0의 사전 준비와 관련 문단에 가상환경(venv) 절차를 추가합니다.



보고서 §0에 가상환경 생성·활성화·비활성화와, venv 기준/비venv 대안 명령을 정리해 반영합니다.



`Reporter/21_magic-square-d2-tc-red-branch-github-session-export-report.md`의 **§0**을 고쳐, 가상환경 기준으로 실행할 수 있게 정리해 두었습니다.

### 반영 내용 요약

1. **맨 앞 안내** — venv를 켠 뒤에는 `python`·`pytest`, 안 쓰면 `py -3`·`py -3 -m pytest`로 바꿔 쓰면 된다는 한 줄 규칙.

2. **§0.2 가상환경(venv)**  
   - `py -3 -m venv .venv`  
   - `.\.venv\Scripts\Activate.ps1`  
   - `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` (스크립트 막힐 때)  
   - 활성화 후 `python -m pip install -e ".[dev]"`, `python -m pytest --version`  
   - `deactivate`  
   - `.gitignore`에 `.venv/` 무시된다는 점

3. **§0.3 pytest** — 첫 블록에 활성화 포함, venv 없을 때 한 줄 대안.

4. **§0.4~0.7** — 이전 0.3~0.6 번호만 맞춤 (`0.2` → `0.3` 교차 참조 수정).

5. **§0.7 트러블슈팅** — `pytest` 없음 ↔ venv 미활성화, `Activate.ps1` ↔ 실행 정책.

6. **§5 TC↔pytest 표** — 예시를 `pytest ...`로 통일하고, venv 없을 때는 `py -3 -m pytest`로 바꾼다는 주석.

필요하면 `README.md`에도 같은 venv 절차를 넣을 수 있는데, 지금은 요청하신 보고서만 수정했습니다.

---

**User**

@Reporter/21_magic-square-d2-tc-red-branch-github-session-export-report.md  문서를 참조해서 red 테스트 코드를 만들어줘

---

**Cursor**

보고서와 기존 테스트·패키지 구조를 확인한 뒤 RED 단계용 테스트 파일을 추가합니다.



TC 문서와 동일한 8개 케이스명의 RED 스텁을 추가하고, 기본 `pytest`는 통과하도록 `red_phase` 마커로 제외합니다.



기본 `pytest`는 8개 통과·8개 제외로 정상입니다. 실패 메시지의 유니코드 대시를 ASCII로 바꿉니다.



작업 반영했습니다. **Reporter/21**과 **TC_D2**의 8개 케이스명을 그대로 쓰는 RED 스텁을 두었고, 보고서에 나온 기본 검증(`pytest tests\entity`)이 깨지지 않도록 설정했습니다.

### 추가된 파일

- `tests/red_phase/test_user_entity_red.py` — 각 테스트 본문은 `pytest.fail("RED: ...")` 한 줄만 (의도적 실패).
- `tests/red_phase/__init__.py` — 패키지용 빈 모듈.

### `pyproject.toml` 변경

- `markers`에 `red_phase` 등록.
- `addopts = ["-m", "not red_phase"]` — **일반 `pytest`에서는 RED 스텁을 수집만 제외**하고, 기존 `tests/entity/test_user.py` 8개만 실행되어 전부 통과합니다.

### 실행 방법

| 목적 | 명령 (PowerShell, 루트에서) |
|------|---------------------------|
| GREEN 검증 (보고서 §0.3과 동일) | `py -3 -m pytest tests\entity -q` 또는 `py -3 -m pytest tests -q` |
| RED만 일부러 실패시키기 | `py -3 -m pytest -m red_phase tests\red_phase -v` |

GREEN 구현 참고는 그대로 `tests/entity/test_user.py`이고, RED에서 같은 이름으로 TC를 따라가다가 GREEN으로 옮기는 흐름을 연습할 수 있습니다.

---

**User**

실행 방법을 가상환경 할 수 있도록 알려줘

---

**Cursor**

보고서에 RED 단계(`pytest -m red_phase`) 실행까지 가상환경 절차가 포함돼 있는지 확인하고, 빠진 부분을 보강합니다.



보고서에 이미 §0.2 가상환경이 있습니다. 복사용 **요약 블록**과 **RED 단계(`pytest -m red_phase`)**를 가상환경 기준으로 추가합니다.



`Reporter/21_magic-square-d2-tc-red-branch-github-session-export-report.md`에 **가상환경 기준 실행**을 더 분명히 넣어 두었습니다.

### 추가·정리한 내용

1. **복사용 요약 블록** (§0 맨 위, 명령 표기 바로 아래)  
   `cd` → `py -3 -m venv .venv` → `Activate.ps1` → `pip install` → `pytest tests\entity -q` 한 번에 붙여 넣을 수 있게 했고, 새 터미널마다 다시 할 **활성화 한 줄**도 적어 두었습니다.

2. **§0.3에 RED 스텁 실행**  
   가상환경 활성화 후 `pytest -m red_phase tests\red_phase -v`, venv 없을 때는 `py -3 -m pytest ...` 로 대체한다는 문장과, **8건 실패가 정상**이라는 설명을 넣었습니다.

기존 **§0.2 가상환경(venv)** 절차(생성, `Activate.ps1`, 실행 정책, `pip install -e ".[dev]"`, `deactivate`)는 그대로 두었습니다.

### 채팅에서만 보려면 (요약)

| 단계 | PowerShell (루트에서) |
|------|------------------------|
| 최초 1회 | `py -3 -m venv .venv` |
| 매 세션 | `.\.venv\Scripts\Activate.ps1` |
| 의존성 | `python -m pip install -e ".[dev]"` |
| GREEN 검증 | `pytest tests\entity -q` |
| RED 스텁만 | `pytest -m red_phase tests\red_phase -v` |

venv 없이 쓸 때는 `python` → `py -3`, `pytest` → `py -3 -m pytest` 로 바꾸면 됩니다.

---

**User**

Reporter 폴더에  지금 작업한 내용을 보고서로 내보내줘.

---

**Cursor**

Reporter 폴더의 번호·형식을 확인한 뒤, 이번 세션 작업을 정리한 보고서를 추가합니다.



`Reporter/22` 번호로 세션 작업(문서·코드·검증)을 정리한 보고서를 작성합니다.



`Reporter` 폴더에 아래 파일로 정리해 두었습니다.

**파일:** [`Reporter/22_magic-square-reporter21-venv-red-phase-follow-up-session-export-report.md`](Reporter/22_magic-square-reporter21-venv-red-phase-follow-up-session-export-report.md)

**포함 내용 요약**

1. **§1 요약표** — 이번 세션 목적(Reporter/21 보강, venv 안내, RED 스텁, 보내기)  
2. **§2 파일별 작업** — `Reporter/21`, `tests/red_phase/*`, `pyproject.toml`, 본 `Reporter/22`  
3. **§3 설계 의도** — `red_phase` 제외로 기본 `pytest` GREEN 유지, 교육용 RED, venv  
4. **§4 검증 명령** — GREEN / RED-only / collect-only  
5. **§5 연계** — Reporter/21, TC_D2, PRD  
6. **§6 후속** — README 문서 맵에 Reporter/22 추가 등(선택)  
7. **§7 변경 이력**

번호는 기존 `21` 다음으로 **`22`**를 사용했습니다.

