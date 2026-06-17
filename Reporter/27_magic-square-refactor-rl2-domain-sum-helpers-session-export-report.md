## Magic Square (4x4) — Dual-Track REFACTOR 실행 보고서 (R-L2)

**보내기 일자:** 2026-04-28  
**산출물 유형:** “커밋 1개 단위” **Dual-Track REFACTOR 실행 결과** 아카이브 (기능/계약 변경 없음)

---

## 1. 기준선 확인 (Step 0)

PowerShell 환경에서 `pytest` 명령이 PATH에 없어, 동일 의미의 모듈 실행으로 기준선을 확인했다.

```powershell
python -m pytest -q
```

결과:

- `14 passed, 17 deselected`

---

## 2. 이번 커밋 리팩토링 목표 (Step 1)

선택:

- **Logic Track — R-L2**: 행/열/대각선 합 계산 중복 로직을 `sum_row` / `sum_col` / `sum_diag`로 추출

선택 사유(최소 단위):

- 변경 범위가 `magicsquare/domain.py` 내부로 제한되어 위험도가 낮다.
- `line_sums()`와 `is_magic_square_complete()` 사이의 중복 제거 효과가 크다.
- 외부 계약(입출력/예외/포맷)에 영향이 없다.

---

## 3. 보호 테스트(안전망) 점검 (Step 2)

리팩토링과 직접 연관된 기존 테스트가 이미 계약을 고정하고 있어, 추가 테스트는 최소 변경 원칙에 따라 수행하지 않았다.

- `tests/magicsquare/test_dual_track_ld01_ud01.py`
  - `test_default_complete_board_has_equal_row_col_diag_sums()`가 `get_line_sums()` 결과를 **정확한 딕셔너리 값**으로 고정
  - `test_solve_fills_two_blanks_to_complete_magic_square()`가 결과 벡터(길이 6) 및 완성된 마방진 성립을 고정

---

## 4. Dual-Track 리팩토링 수행 (Step 3)

### 4.1 변경 전 문제점

- `is_magic_square_complete()`와 `line_sums()`에서 row/col/diag 합 계산이 중복되어, 규칙 변경/수정 시 누락 또는 불일치 위험이 있었다.

### 4.2 변경 후 개선점

- 합 계산을 `sum_row(board, r)`, `sum_col(board, c)`, `sum_diag(board, which)`로 통일하여 중복을 제거했다.
- 동작(계약/예외/포맷)은 유지하고, 내부 가독성과 변경 안전성만 개선했다.

### 4.3 변경 범위 (Track 분리)

- **UI Track (`magicsquare/boundary.py`, GUI 등)**: 변경 없음
- **Logic Track (`magicsquare/domain.py`)**:
  - `sum_row`, `sum_col`, `sum_diag` 추가
  - `is_magic_square_complete`, `line_sums`가 위 헬퍼를 사용하도록 치환

---

## 5. 테스트 재실행 (Step 4)

```powershell
python -m pytest -q
```

결과:

- `14 passed, 17 deselected`

---

## 6. 수정된 파일 목록 (Step 5)

- **수정**: `magicsquare/domain.py`
- **추가/이동/삭제**: 없음

---

## 7. 위험 요소 및 롤백 포인트

위험 요소(낮음):

- `sum_diag(board, which)`의 selector 규약(0=main, 1=anti)이 잘못되면 대각선 합이 뒤바뀔 수 있다.

롤백 포인트:

- `magicsquare/domain.py`에서 추가된 `sum_row/sum_col/sum_diag` 및 호출 치환부만 되돌리면 즉시 원복 가능.

---

## 8. 커밋 메시지 제안 (Conventional Commit)

- `refactor(domain): extract row/col/diag sum helpers`

