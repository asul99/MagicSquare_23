## Magic Square (4x4) — GUI 가독성·편집 UX 후속 세션 보내기 보고서

**보내기 일자:** 2026-04-28
**산출물 유형:** Cursor 세션에서 수행한 **GUI 합계 표시·두 자리 표시·빈칸 편집 UX 보강** 아카이브
**선행 보고서:** [`Reporter/24`](24_magic-square-green-gui-venv-coverage-session-export-report.md)

---

## 1. 보내기 요약

| 구분 | 내용 |
|------|------|
| 브랜치 | `green` (원격 `origin/green`) |
| 기준 커밋 | `1f11c50` (`feat(green): complete GUI magic-square solve flow`) |
| 변경 파일 | [`magicsquare/gui/app.py`](../magicsquare/gui/app.py) (미커밋 상태) |
| 동기 | 사용자 피드백 3건 — (a) 합계 옆에 사용된 칸 값도 보여 줄 것, (b) 두 자리 숫자가 잘려 보임, (c) 0 칸을 사용자가 수정할 수 있도록 UI에 명확히 보여 줄 것 |
| 검증 | `pytest tests` → `14 passed, 17 deselected` |

---

## 2. 변경 의도와 결과

### 2.1 합계와 사용된 칸 값을 함께 표시

`Current visible board`와 `Solved preview` 각각에 대해, 가로 4줄·세로 4줄·대각선 2줄에 사용된 칸 값을 합과 함께 한 줄씩 인쇄한다. 사용자가 GUI 격자에 쓰인 숫자와 합 인쇄가 동일한지 즉시 비교할 수 있다.

표시 예시(초기, 0 두 칸):

```
Current visible board:
  row 1: 16 + 2 + 3 + 13 = 34
  row 2: 5 + 11 + 10 + 8 = 34
  row 3: 9 + 7 + 0 + 12 = 28
  row 4: 4 + 14 + 15 + 0 = 33
  col 1: 16 + 5 + 9 + 4 = 34
  col 2: 2 + 11 + 7 + 14 = 34
  col 3: 3 + 10 + 0 + 15 = 28
  col 4: 13 + 8 + 12 + 0 = 33
  diag \: 16 + 11 + 0 + 0 = 27
  diag /: 13 + 10 + 7 + 4 = 34
Solved preview (fill (3,3)=6, (4,4)=1):
  row 1: 16 + 2 + 3 + 13 = 34
  row 2: 5 + 11 + 10 + 8 = 34
  row 3: 9 + 7 + 6 + 12 = 34
  row 4: 4 + 14 + 15 + 1 = 34
  col 1: 16 + 5 + 9 + 4 = 34
  col 2: 2 + 11 + 7 + 14 = 34
  col 3: 3 + 10 + 6 + 15 = 34
  col 4: 13 + 8 + 12 + 1 = 34
  diag \: 16 + 11 + 6 + 1 = 34
  diag /: 13 + 10 + 7 + 4 = 34
```

### 2.2 두 자리 숫자 잘림 수정

`QSpinBox` 기본 위/아래 화살표가 셀 너비를 잡아먹어 16 등 두 자리가 잘려 보였다. 화살표 버튼을 제거하고 셀 크기와 폰트를 키워 두 자리 숫자가 모두 보이게 했다.

| 항목 | 값 |
|------|----|
| `setButtonSymbols` | `QAbstractSpinBox.ButtonSymbols.NoButtons` |
| `setFixedWidth` | `64` |
| `setMinimumHeight` | `36` |
| 기본 스타일 | `QSpinBox { font-size: 18px; padding: 2px; }` |

### 2.3 0 칸 강조와 편집 보장

키보드 입력은 `QSpinBox` 기본 동작으로 가능하지만, 화살표를 없애면서 “편집 가능” 신호가 약해졌다. 이를 시각·접근성 양쪽으로 보강했다.

| 항목 | 처리 |
|------|------|
| 빈칸 강조 | `background-color: #FFF59D`, `border: 1px solid #FBC02D` |
| 값이 0이 아닐 때 | 즉시 기본 스타일로 전환 (`refresh_cell_styles`) |
| 편집 보장 | `setReadOnly(False)`, `setFocusPolicy(Qt.FocusPolicy.StrongFocus)` |
| 첫 편집 편의 | 시작 시 각 셀 `lineEdit().selectAll()` 호출 |
| 안내 문구 | `Click any cell to type a new number (0-16). Click Solve to fill the blanks.` |

`valueChanged` 시그널은 합계 갱신과 스타일 갱신을 함께 호출한다.

---

## 3. 코드 흐름 요약

| 함수/위치 | 역할 |
|-----------|------|
| `format_board_lines(board, sums)` | 행/열/대각선의 사용 값과 합을 사람이 읽는 문자열로 직렬화 |
| `update_sums_label()` | `Current visible board`와 (가능 시) `Solved preview` 두 섹션을 합쳐 라벨에 표시 |
| `refresh_cell_styles()` | 각 셀의 현재 값을 보고 0이면 노란 강조, 아니면 기본 스타일 |
| `on_value_changed(_value)` | 사용자가 값을 바꿀 때마다 합계와 스타일을 동시에 갱신 |
| `on_solve_clicked()` | `validate_grid_input` -> `solve` 결과를 셀에 채우고 합계 라벨/결과 라벨 갱신 |

ECB/Screen 경계는 그대로다. PyQt import는 `magicsquare/gui/app.py` 안 함수 본문에만 있고, `magicsquare/domain.py`·`magicsquare/boundary.py`는 PyQt 의존이 없다.

---

## 4. 검증

| 명령 | 결과 |
|------|------|
| `.\.venv\Scripts\python -m pytest tests -q` | `14 passed, 17 deselected` |
| `.\.venv\Scripts\python -m magicsquare.gui` | 두 자리 숫자가 모두 보이고, 0 두 칸이 노랗게 강조되며, 합계 옆 사용 칸 값이 인쇄됨 |

---

## 5. 알려진 한계

- 미커밋 상태이므로 원격 `origin/green`에는 아직 반영되지 않았다.
- 시각 강조 색은 라이트 테마 기준 고정값이다. 다크 테마에서는 별도 색·대비 검토가 필요할 수 있다.
- 현재 입력 가드는 `QSpinBox` 범위(0..16)에 의존하며, “0이 정확히 2개” 등의 도메인 규칙은 `Solve` 시점에 boundary/도메인에서 검증한다.

---

## 6. 후속 권장

1. 본 보강을 별도 GREEN 커밋으로 묶어 푸시한다 (예: `feat(gui): show line sums per cell, fix 2-digit display, highlight blanks`).
2. UI 동작 자동화는 여전히 선택 사항이지만, `format_board_lines`는 GUI 의존이 없으므로 단위 테스트로 분리·검증할 수 있다.
3. `pytest-cov`를 dev 의존성에 추가해 본 변경 이후 커버리지 변동을 추적한다.

---

## 7. 변경 이력(Reporter)

| 일자 | 내용 |
|------|------|
| 2026-04-28 | 초안: GUI 합계 옆 사용 칸 값 인쇄, 두 자리 숫자 잘림 수정, 0 칸 강조·편집 UX 정리 (`Reporter/25`) |
