## Magic Square — `domain.py`/`boundary.py`/GUI( `magicsquare/gui/app.py` ) 분석 및 리팩토링 계획 보고서

**보내기 일자:** 2026-04-28  
**산출물 유형:** 코드 수정 없이 수행한 **테스트 현황 확인 + Code Smell/ECB/SRP 분석 + 리팩토링 계획서** 아카이브

---

## 1. 대상 범위

- `magicsquare/domain.py`
- `magicsquare/boundary.py`
- GUI 파일: 사용자 요청은 `gui/main_window.py`였으나, 현재 레포에는 해당 파일이 없고 UI는 `magicsquare/gui/app.py`가 담당

---

## 2. 테스트 파일 존재 여부(현황)

### 2.1 `test_*.py` 존재 여부

현재 테스트 파일(`test_*.py`)은 존재한다.

- `tests/red_phase/logic/test_magic_square_control_red.py`
- `tests/red_phase/boundary/test_magic_square_boundary_red.py`
- `tests/red_phase/ui/test_magic_square_ui_red.py`
- `tests/entity/test_user.py`
- `tests/red_phase/logic/test_user_entity_red.py`
- `tests/magicsquare/test_dual_track_ld01_ud01.py`

### 2.2 “테스트 없이 리팩토링하면 안 되는 이유”(1줄)

리팩토링은 **동작을 바꾸지 않고 구조만 바꾸는 작업**이므로, 테스트가 없으면 회귀(동작 변화)를 즉시 검증할 안전망이 없다.

---

## 3. Code Smell 점검 결과(요약 표)

| 파일명 | 줄번호 | 스멜 종류 | 문제 설명 | 우선순위 |
|---|---:|---|---|---|
| `magicsquare/domain.py` | 76–120 | 긴 함수(20줄 초과) | `solve_two_blanks()`가 입력 검증 + 누락 값 계산 + 후보 대입/검증(탐색)까지 한 함수에 집중 | 높음 |
| `magicsquare/domain.py` | 27 | 하드코딩된 매직 넘버 | 빈칸을 `0`으로 직접 비교(동일 파일의 `EMPTY_CELL_VALUE`와 불일치) | 중간 |
| `magicsquare/domain.py` | 95 | 하드코딩된 매직 넘버 | 에러 메시지에 `1 to 16`이 문자열로 고정(상수 변경 시 불일치 위험) | 중간 |
| `magicsquare/boundary.py` | 21–31 | 중복 코드 | 같은 `ValueError(f"Grid must be {MATRIX_SIZE}x{MATRIX_SIZE}.")` 문구가 분기마다 반복 | 낮음 |
| `magicsquare/gui/app.py` | 14–185 | 긴 함수(20줄 초과) | `main()`이 UI 구성/레이아웃/스타일/이벤트/도메인 호출까지 모두 수행(가독성·테스트성 저하) | 높음 |
| `magicsquare/gui/app.py` | 54–59 | 하드코딩된 매직 넘버 | `default_board`가 4×4 고정 샘플로 하드코딩(`MATRIX_SIZE` 변경 시 즉시 깨질 가능성) | 중간 |
| `magicsquare/gui/app.py` | 68–69 | 하드코딩된 매직 넘버 | 셀 크기(64, 36) 고정값 | 낮음 |
| `magicsquare/gui/app.py` | 92–96 | 하드코딩된 매직 넘버 | 폰트/패딩/색상 등 스타일 값이 코드 문자열에 고정 | 낮음 |
| `magicsquare/gui/app.py` | 107–130 | 긴 함수(20줄 초과) | `format_board_lines()`가 데이터 구성 + 문자열 표현을 함께 처리 | 중간 |
| `magicsquare/gui/app.py` | 132–166 | 중복 코드 | `update_sums_label()`와 `on_solve_clicked()`가 `solve()` 호출/예외 처리/벡터 적용 흐름에서 유사 로직을 가짐 | 중간 |
| `magicsquare/gui/app.py` | 180 | 하드코딩된 매직 넘버 | `window.resize(520, 360)` 고정 | 낮음 |

---

## 4. ECB(Entity-Control-Boundary) 관점 분석

### 4.1 각 파일의 현재 ECB 역할

- `magicsquare/domain.py`: **Control(도메인 규칙/계산)** 중심  
  - `list[list[int]]` 같은 원시 구조를 직접 다룸(명시적인 Entity/값 객체 부재)
- `magicsquare/boundary.py`: **Boundary(입력 형태 검증 + 도메인 위임)** 역할을 대체로 수행  
  - 다만 `solve()`가 결과 벡터 길이(`SOLUTION_VECTOR_SIZE`) 같은 내부 규약 확인까지 수행해 Boundary가 약간 두꺼워질 여지
- `magicsquare/gui/app.py`: **UI(Screen)**  
  - UI 표시/이벤트 처리 외에, `solve()` 결과 벡터를 해석하여 “프리뷰용 보드”를 구성하는 변환 로직이 UI에 섞여 있음

### 4.2 잘못된 위치(또는 이동 고려) 코드

- UI(`magicsquare/gui/app.py`)에 있는 “solution vector를 board에 적용해 filled board 생성” 로직은 재사용/일관성 관점에서 이동 후보
  - 이동 후보:
    - `magicsquare/boundary.py`: 표현 독립 변환(`apply_solution_vector(grid, vec) -> new_grid`)처럼 어댑터 성격으로
    - 또는 `magicsquare/domain.py`: 벡터 의미 자체가 도메인 규약이라면 도메인 유틸로

### 4.3 `domain.py` 내 Entity/Control 혼재 여부

현재는 “Entity + Control 혼재”라기보다는 **Control 위주이며, Entity(데이터 보관 구조)가 부재**한 상태에 가깝다.  
분리가 필요하다면 다음 “데이터 표현/해석 규약”을 값 객체(Entity)에 가깝게 끌어올릴 수 있다.

- 1-based 좌표 규약(빈칸 좌표/해답 벡터 포맷)
- 6원소 solution vector `[r1,c1,n1,r2,c2,n2]`라는 출력 포맷 규약

---

## 5. SRP(단일 책임 원칙) 위반 후보(위반 사항만)

### 5.1 하나의 함수가 두 가지 이상의 역할

- `magicsquare/domain.py:76-120` — `solve_two_blanks` (검증 + 누락값 계산 + 탐색/판정)
- `magicsquare/boundary.py:33-55` — `solve` (입력 검증 + 도메인 호출 + 결과 규약 검증)
- `magicsquare/gui/app.py:14-185` — `main` (UI 구성 + 이벤트/핸들러 + 도메인 연결)
- `magicsquare/gui/app.py:132-150` — `update_sums_label` (표현 구성 + solve 호출/예외 처리 + 프리뷰 보드 구성)
- `magicsquare/gui/app.py:152-166` — `on_solve_clicked` (solve/검증 + UI 오류 처리 + UI 상태 변경)
- `magicsquare/gui/app.py:107-130` — `format_board_lines` (데이터 구성 + 문자열 직렬화)

### 5.2 하나의 클래스가 “데이터 보관 + 검증 로직”을 동시에 담당

해당 3개 파일에는 사용자 정의 클래스가 없어 본 항목 위반은 확인되지 않음.

### 5.3 GUI에서 UI 외 비즈니스 판단(예: `if total == 34`) 직접 수행

UI에서 “마방진 성립 여부(예: 합=34)” 같은 직접 판단 코드는 보이지 않지만, 아래처럼 **solve 결과를 해석해 보드를 재구성하는 변환**이 UI에 존재한다.

- `magicsquare/gui/app.py:132-150` — solved preview를 위해 `vec`를 분해 후 `filled` board 구성
- `magicsquare/gui/app.py:152-166` — solve 성공/실패에 따른 UI 반영 분기(예외 처리 포함)

---

## 6. 리팩토링 계획서

## 리팩토링 대상 목록 (우선순위 순)

| 순번 | 대상 파일 | 문제 | 적용 기법 | 우선순위 |
|---:|---|---|---|---|
| 1 | `magicsquare/domain.py` | `solve_two_blanks()`에 검증/계산/탐색이 혼재(SRP 위반, 변경 리스크 큼) | Extract Function, (선택) Introduce Value Object(Position/SolutionVector), 단계 분리 | 높음 |
| 2 | `magicsquare/gui/app.py` | `main()` 과밀 + 프리뷰 구성 로직이 UI에 혼재 | Extract Function(빌더/핸들러/표현), Move Function(프리뷰 변환 로직 이동) | 높음 |
| 3 | `magicsquare/boundary.py` | Boundary가 내부 규약(벡터 길이 등)까지 일부 인지, 검증 실패 메시지 중복 | Thin Boundary, DRY(검증/메시지 정리) | 중간 |
| 4 | `magicsquare/domain.py`, `magicsquare/gui/app.py` | 규약 상수/메시지/표현에 매직값 산재 | Replace Magic Number with Constant, 메시지 상수화(단일 출처) | 중간 |
| 5 | `magicsquare/gui/app.py` | UI 치수/스타일 하드코딩 | Extract Constant/Config | 낮음 |

## 테스트 선행 필요 항목

리팩토링 전에 먼저 테스트를 추가/보강해야 할 함수 목록:

- `magicsquare/domain.py`
  - `solve_two_blanks()` (정상 케이스 + 예외 케이스 전부)
  - `is_magic_square_complete()`
  - `line_sums()`
  - `find_blank_coords()`
  - `magic_constant()`
- `magicsquare/boundary.py`
  - `validate_grid_input()`
  - `solve()`
  - `get_line_sums()`

## 리팩토링 후 검증 방법

### 회귀 테스트(Regression Test) 실행 명령어

- 기본(현 `pyproject.toml` 설정상 `red_phase` 제외):

```bash
python -m pytest
```

- red_phase 포함 전체 확인:

```bash
python -m pytest -m red_phase
```

### 외부 동작(기능)이 바뀌지 않았음을 확인하는 방법

- **도메인/바운더리 계약 유지 확인**
  - `solve(grid)`가 동일 의미의 6원소 벡터(`[r1,c1,n1,r2,c2,n2]`, 1-based)를 반환
  - 동일 입력에서 동일한 `ValueError` 동작(성공/실패, 메시지 정책은 테스트로 고정)
- **GUI 스모크 체크**
  - GUI 엔트리포인트: `python -m magicsquare.gui`
  - Solve 클릭 시 두 빈칸이 채워지고, 잘못된 입력은 오류로 안내되는지 수동 확인

