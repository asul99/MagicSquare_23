# Magic Square (4x4) — GREEN 브랜치 GUI·venv·커버리지 후속 세션 보내기 보고서

**보내기 일자:** 2026-04-28  
**산출물 유형:** Cursor 세션에서 수행한 **GREEN 브랜치 작업**, **PyQt6 GUI 실행 경로**, **venv 구성**, **마방진 풀이·합계 표시 보정**, **커버리지 실행 안내** 아카이브  
**선행 보고서:** [`Reporter/21`](21_magic-square-d2-tc-red-branch-github-session-export-report.md), [`Reporter/23`](23_magic-square-venv-evaluation-red-phase-layout-session-export-report.md)

---

## 1. 보내기 요약

| 구분 | 내용 |
|------|------|
| **브랜치** | `green` — `red` 브랜치 기준으로 생성 |
| **커밋 1** | `e64b980` — `feat(magicsquare): domain blank scan + boundary grid shape (L-RED-01, U-RED-01)` |
| **커밋 2** | `9eea6d7` — `feat(gui): add PyQt6 screen entrypoint` |
| **후속 보정(미커밋 상태)** | GUI 초기값·합계 표시·두 빈칸 풀이 로직 보강, 테스트 추가, `magic_square/ui/` 및 RED UI 테스트 일부 변경 |
| **검증** | 기본 pytest: 최종 시점 `14 passed, 17 deselected` |
| **실행 경로** | `.\.venv\Scripts\python -m magicsquare.gui` |

---

## 2. 브랜치 전략과 GREEN 시작

사용자 요청에 따라 `red`에서 `green` 브랜치를 생성했다.

```powershell
git checkout red
git checkout -b green
```

세션 확인 결과 `green`, `red`, `main`은 당시 동일 커밋 `b5f3ee7`에서 시작했다. 이후 GREEN 작업은 `green` 브랜치에서 진행했다.

---

## 3. Dual-Track GREEN 1차 커밋

### 3.1 선택한 RED

| Track | ID | 설명 |
|-------|----|------|
| Logic | `L-RED-01` | `find_blank_coords()`가 row-major 순서로 빈칸 좌표 2개를 반환 |
| Boundary | `U-RED-01` | 입력이 4x4가 아니면 `ValueError` 발생 |

선택 이유:

- row-major 빈칸 순서는 이후 성공 출력 `[r1,c1,n1,r2,c2,n2]`의 좌표 순서를 결정한다.
- Boundary의 4x4 크기 검증은 GUI/Screen이 Domain을 직접 호출하지 않도록 하는 첫 진입 계약이다.

### 3.2 GREEN 구현

| 파일 | 내용 |
|------|------|
| [`magicsquare/constants.py`](../magicsquare/constants.py) | `MATRIX_SIZE` 단일 상수 |
| [`magicsquare/domain.py`](../magicsquare/domain.py) | `find_blank_coords()` |
| [`magicsquare/boundary.py`](../magicsquare/boundary.py) | `validate_grid_input()` |
| [`tests/magicsquare/test_dual_track_ld01_ud01.py`](../tests/magicsquare/test_dual_track_ld01_ud01.py) | L-RED-01, U-RED-01 검증 |
| [`pyproject.toml`](../pyproject.toml) | `magicsquare*` 패키지 탐색 추가 |

검증:

```powershell
.\.venv\Scripts\python -m pytest tests/magicsquare/test_dual_track_ld01_ud01.py -q
.\.venv\Scripts\python -m pytest tests -q
```

결과:

- 선택 묶음: `4 passed`
- 기본 전체: `12 passed, 17 deselected`

---

## 4. PyQt6 GUI 실행 커밋

### 4.1 범위

요구에 맞춰 GUI는 **Screen 전용 하위 패키지**에 두었다.

| 항목 | 결정 |
|------|------|
| 공식 실행 경로 | `python -m magicsquare.gui` |
| Qt import 위치 | [`magicsquare/gui/`](../magicsquare/gui/) 내부만 |
| 의존성 | `pyproject.toml` optional dependency `gui = ["PyQt6>=6.6"]` |
| Domain/Boundary | PyQt import 없음 |

### 4.2 GUI MVP

| 기능 | 내용 |
|------|------|
| 입력 | `QSpinBox` 4x4 그리드, 0은 빈칸 |
| 버튼 | `Solve` |
| 호출 흐름 | `validate_grid_input()` -> `solve()` |
| 실패 표시 | `QMessageBox.critical()` 및 결과 라벨 `Result: (error)` |
| 성공 표시 | 결과 벡터 `[r1,c1,n1,r2,c2,n2]` 라벨 표시 |

실행:

```powershell
.\.venv\Scripts\python -m magicsquare.gui
```

---

## 5. venv 구성과 실행 문제 해결

### 5.1 문제

전역 Python은 아래처럼 확인되었다.

```powershell
python -V
python -m pip -V
```

결과 요지:

- `Python 3.14.4`
- `pip ... C:\Python314 ...`

또한 `pytest` 직접 실행 시 PATH에 없어 실패했다.

```text
'pytest'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 배치 파일이 아닙니다.
```

### 5.2 조치

프로젝트 루트에 `.venv`를 만들고 dev/gui 의존성을 설치했다.

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -U pip
.\.venv\Scripts\python -m pip install -e ".[dev,gui]"
```

PowerShell 실행 정책으로 `Activate.ps1`이 차단될 수 있어, 활성화 없이도 아래 명령을 권장했다.

```powershell
.\.venv\Scripts\python -m pytest
.\.venv\Scripts\python -m magicsquare.gui
```

---

## 6. GUI 보정: 초기값·마방진 합계·풀이

### 6.1 사용자 피드백

초기 GUI에서 모든 값이 0으로 보이는 문제, 이후 0 두 개 조건과 합계 표시가 혼동되는 문제가 있었다.

정리된 현재 의도:

- 초기 화면에는 **0이 정확히 2개** 보여야 한다.
- 보이는 값 기준 합계는 0 때문에 일부 줄이 34가 아닐 수 있다.
- `Solve` 후에는 두 0이 채워지고, 가로 4개·세로 4개·대각선 2개의 합이 모두 34가 되어야 한다.

### 6.2 현재 기본 보드

```text
16  2  3 13
 5 11 10  8
 9  7  0 12
 4 14 15  0
```

풀이 후 기대 보드:

```text
16  2  3 13
 5 11 10  8
 9  7  6 12
 4 14 15  1
```

이 보드는 `rows = [34, 34, 34, 34]`, `cols = [34, 34, 34, 34]`, `diags = [34, 34]`를 만족한다.

### 6.3 보정된 코드 흐름

| 파일 | 내용 |
|------|------|
| [`magicsquare/domain.py`](../magicsquare/domain.py) | `magic_constant()`, `is_magic_square_complete()`, `line_sums()`, `solve_two_blanks()` |
| [`magicsquare/boundary.py`](../magicsquare/boundary.py) | `solve()`가 Domain의 `solve_two_blanks()` 호출, `get_line_sums()` 추가 |
| [`magicsquare/gui/app.py`](../magicsquare/gui/app.py) | 두 0이 있는 초기 보드, Current visible sums / Solved preview 분리 표시, Solve 성공 시 스핀박스 값 채움 |
| [`tests/magicsquare/test_dual_track_ld01_ud01.py`](../tests/magicsquare/test_dual_track_ld01_ud01.py) | 풀이 후 완전 마방진 검증, 기본 완성 보드 합계 검증 |

---

## 7. 테스트와 커버리지 안내

### 7.1 pytest

```powershell
Set-Location C:\DEV\MagicSquare_23
.\.venv\Scripts\python -m pytest
```

최종 확인:

```text
14 passed, 17 deselected
```

### 7.2 coverage

`pytest-cov` 설치:

```powershell
.\.venv\Scripts\python -m pip install pytest-cov
```

터미널 리포트:

```powershell
.\.venv\Scripts\python -m pytest --cov=magicsquare --cov=magic_square --cov-report=term-missing
```

HTML 리포트:

```powershell
.\.venv\Scripts\python -m pytest --cov=magicsquare --cov=magic_square --cov-report=html --cov-report=term-missing
start htmlcov\index.html
```

`start htmlcov\index.html`은 `C:\DEV\MagicSquare_23` 프로젝트 루트에서 실행한다.

---

## 8. 현재 Git 상태 메모

본 보고서 작성 직전 기준으로 최근 커밋은 다음과 같다.

```text
9eea6d7 feat(gui): add PyQt6 screen entrypoint
e64b980 feat(magicsquare): domain blank scan + boundary grid shape (L-RED-01, U-RED-01)
b5f3ee7 Split red_phase tests into logic/boundary/ui; add Reporter/21 venv evaluation and Reporter/23 export
```

보고서 작성 전 워킹 트리에는 다음 변경이 남아 있었다.

```text
 M magicsquare/boundary.py
 M magicsquare/domain.py
 M magicsquare/gui/app.py
 M tests/magicsquare/test_dual_track_ld01_ud01.py
 M tests/red_phase/ui/test_magic_square_ui_red.py
?? magic_square/ui/
```

즉, `9eea6d7` 이후 GUI 보정·풀이 보강·RED UI 테스트 일부 변경은 아직 별도 커밋으로 정리되지 않은 상태다.

---

## 9. 후속 권장

1. GUI 보정과 Domain 풀이 보강을 별도 GREEN 커밋으로 정리한다.
2. `magic_square/ui/`와 `tests/red_phase/ui/test_magic_square_ui_red.py` 변경은 `magicsquare/gui/` 흐름과 중복 여부를 확인해 분리 커밋 또는 정리 커밋으로 처리한다.
3. `pytest-cov`를 `dev` 의존성에 넣을지 결정한다. 교육용이면 `dev = ["pytest>=7.0", "pytest-cov>=..."]` 형태로 고정해도 좋다.

---

## 10. 변경 이력(Reporter)

| 일자 | 내용 |
|------|------|
| 2026-04-28 | 초안: `green` 브랜치 생성, Dual-Track GREEN, PyQt6 GUI 실행, venv 구성, GUI 마방진 보정, 커버리지 실행 방법 정리 (`Reporter/24`) |

