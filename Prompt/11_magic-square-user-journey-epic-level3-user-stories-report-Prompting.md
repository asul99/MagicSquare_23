# User stories for input validation and processing
_Exported on 4/28/2026 at 08:32:27 GMT+9 from Cursor (3.2.11)_

---

**User**

Level 3: User Stories를 다음 내용처럼 작성해 주세요.
Story 1 — 입력 검증
As a 학습자
I want to 입력이 정확히 4x4인지 검증되길 원한다
So that 잘못된 데이터가 Domain으로 전달되지 않도록 한다
Acceptance Criteria:
4x4가 아니면 예외
빈칸 2개 아니면 예외
중복 숫자 예외
범위 위반 예외
Story 2 — 빈칸 탐색
As a 학습자
I want to 0의 좌표를 정확히 찾고 싶다
So that 조합 시도가 가능하다
Acceptance Criteria:
row-major 순서 유지
정확히 2개 반환
Story 3 — 누락 숫자 탐색
Acceptance Criteria:
1~16 중 누락 2개
오름차순 반환
Story 4 — 마방진 판정
Acceptance Criteria:
모든 행 합 동일
모든 열 합 동일
대각선 동일
Story 5 — 두 조합 시도
Acceptance Criteria:
small→first blank 시도
실패 시 reverse
정답 배열 길이 6


---

**Cursor**

프로젝트의 Level 2 보고서 형식을 확인한 뒤 Level 3 User Stories 문서를 작성합니다.



Level 3 전용 파일이 없어 Level 2 보고서 스타일에 맞춰 `Reporter/11_...` 문서를 생성합니다.



Story 5의 세 번째 수용 기준을 요청하신 문구에 더 가깝게 다듬습니다.



다음 파일에 Level 3 User Stories를 반영해 두었습니다.

**파일:** `Reporter/11_magic-square-user-journey-epic-level3-user-stories-report.md`

### 요약

| 스토리 | As a / I want / So that | 수용 기준 |
|--------|-------------------------|-----------|
| **1 — 입력 검증** | 요청하신 문구 그대로 | 4×4 아님·빈칸 2개 아님·중복·범위 위반 시 예외 |
| **2 — 빈칸 탐색** | 요청하신 문구 그대로 | row-major, 좌표 2개 |
| **3 — 누락 숫자** | Story 3용으로 As a / I want / So that 보강 | 1~16 중 누락 2개, 오름차순 |
| **4 — 마방진 판정** | Story 4용으로 As a / I want / So that 보강 | 행·열·대각선 합 동일 |
| **5 — 두 조합 시도** | Story 5용으로 As a / I want / So that 보강 | small→first blank, 실패 시 reverse, 정답 배열 길이 6 |

상단에 Level 2 보고서(`10_...`)와의 연결·작성 목적을 두었고, 수용 기준은 읽기 쉽게 표로 정리했습니다. Story 3~5는 원문에 역할 문장이 없어, Level 2의 BlankFinder / MissingNumberFinder / MagicSquareValidator / Solver 맥락에 맞춰 As a / I want / So that만 보완했습니다. 문구를 전부 한글 한 줄 형태로 통일하거나, `10_...` 본문에 Level 3 절을 합치길 원하시면 알려 주세요.

---

**User**

Reporter 폴더에  지금 작업한 내용을 보고서로 내보내줘.

---

**Cursor**

Level 3 작업본과 Level 2 ‘보내기’ 형식을 확인한 뒤, 동일한보내기 스타일의 보고서를 작성합니다.



Level 2 보내기 보고서(`10_...`)와 동일한 ‘보내기’ 형식으로 Level 3 통합보내기 파일을 추가합니다.



작업 반영했습니다.

**생성 파일:** `Reporter/12_magic-square-user-journey-epic-level3-export-report.md`

`10_magic-square-user-journey-epic-level2-export-report.md`와 같은 **보내기** 구성으로 맞춰 두었습니다.

- **보내기 일자·산출물 유형·관련 원본** (`11_...` 작업본, `10_...` 상위 맥락)
- **보내기 요약** 표(Level 3 범위·형식·Level 2 도메인 매핑 참고)
- **작성 목적·범위**
- **Story 1~5 전문**(As a / I want to / So that + Acceptance Criteria)
- **문서 이력**

일상 수정은 `11_...`에 하고, 공유·아카이브용으로는 `12_...`를 쓰면 Level 2의 `10_...`과 짝이 맞습니다. `11` 이력에 보내기 일자 한 줄을 남기고 싶으면 말해 주세요.

