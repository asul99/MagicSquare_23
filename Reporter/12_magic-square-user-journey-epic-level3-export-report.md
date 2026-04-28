# Magic Square 사용자 여정 — 보고서보내기 (Level 3 User Stories)

**보내기 일자:** 2026-04-28  
**산출물 유형:** Reporter 폴더 공유·아카이브용 Level 3 통합 보고서  
**관련 원본:** `Reporter/11_magic-square-user-journey-epic-level3-user-stories-report.md` (동일 범위의 작업본과 정합)  
**상위 맥락:** `Reporter/10_magic-square-user-journey-epic-level2-export-report.md` (Level 1·2 Epic·User Journey)

---

## 보내기 요약

| 구분 | 내용 |
|------|------|
| **Level 3** | User Story 5건 — 입력 검증, 빈칸 탐색, 누락 숫자 탐색, 마방진 판정, 두 조합 시도 |
| **형식** | 각 스토리별 As a / I want to / So that 및 Acceptance Criteria(표) |
| **도메인 매핑(참고)** | Story 1·2·3·4·5는 Level 2의 계약·경계 및 BlankFinder / MissingNumberFinder / MagicSquareValidator / Solver 역할과 정합 |

아래 본문은 위 요약을 **전문**으로 펼친 것이다.

---

**작성 목적:** Epic 하위 **Level 3: User Stories**를 한 문서로 보존·배포하여, 구현·테스트·리뷰 시 동일한 수용 기준을 참조할 수 있게 한다.  
**범위:** `11_...` 작업본과 동일한 다섯 스토리 전문. Level 1·2 본문은 `10_...`에 있다.

**참고:** “Invariant 기반 사고 훈련 시스템” 및 4×4 Magic Square 도메인 전제를 반영하였다.

---

## Level 3 — User Stories (전문)

### Story 1 — 입력 검증

**As a** 학습자  
**I want to** 입력이 정확히 4×4인지 검증되길 원한다  
**So that** 잘못된 데이터가 Domain으로 전달되지 않도록 한다

#### Acceptance Criteria

| # | 기준 |
|---|------|
| 1 | 4×4가 아니면 예외 |
| 2 | 빈칸이 정확히 2개가 아니면 예외 |
| 3 | 중복 숫자가 있으면 예외 |
| 4 | 허용 범위(값 도메인) 위반이면 예외 |

---

### Story 2 — 빈칸 탐색

**As a** 학습자  
**I want to** 0(빈칸)의 좌표를 정확히 찾고 싶다  
**So that** 조합 시도(Solver)가 가능하다

#### Acceptance Criteria

| # | 기준 |
|---|------|
| 1 | row-major 순서로 좌표를 반환한다 |
| 2 | 빈칸 좌표는 정확히 2개를 반환한다 |

---

### Story 3 — 누락 숫자 탐색

**As a** 학습자  
**I want to** 격자에 없는 숫자(빈칸에 넣을 후보)를 1~16 관점에서 파악하고 싶다  
**So that** Magic Square를 완성하기 위한 후보 집합을 일관되게 얻는다

#### Acceptance Criteria

| # | 기준 |
|---|------|
| 1 | 1~16 중 격자에 나타나지 않은 숫자가 정확히 2개임을 전제로(또는 그에 부합하게) 누락 목록을 산출한다 |
| 2 | 반환 목록은 오름차순이다 |

---

### Story 4 — 마방진 판정

**As a** 학습자  
**I want to** 완성된(또는 주어진) 격자가 Magic Square 규칙을 만족하는지 판정하고 싶다  
**So that** 불변조건(행·열·대각선) 충족 여부를 도메인에서 단일 책임으로 검증할 수 있다

#### Acceptance Criteria

| # | 기준 |
|---|------|
| 1 | 모든 행의 합이 서로 동일하다 |
| 2 | 모든 열의 합이 서로 동일하다 |
| 3 | 두 주 대각선의 합이 위와 동일하다 |

---

### Story 5 — 두 조합 시도

**As a** 학습자  
**I want to** 누락된 두 숫자를 빈칸에 배치할 때, 정해진 순서로 두 번의 조합을 시도하고 결과를 얻고 싶다  
**So that** 최소 탐색 전략(작은 수 우선 → 첫 빈칸, 실패 시 역순)으로 해 후보를 체계적으로 평가할 수 있다

#### Acceptance Criteria

| # | 기준 |
|---|------|
| 1 | 첫 시도: **작은 수(small)** → **첫 번째 빈칸(first blank)** 순으로 배치를 시도한다 |
| 2 | 첫 시도가 Magic Square 판정에 실패하면, **reverse**(예: 큰 수 → 두 번째 빈칸 등 정의된 역순 배치)로 두 번째 시도를 한다 |
| 3 | 정답 배열의 길이는 6이다 |

---

## 문서 이력 (보내기)

| 일자 | 내용 |
|------|------|
| 2026-04-28 | Level 3 User Stories를 Reporter **보내기 보고서**(`12_...`)로 보냄 — 원본 `11_...`과 본문 동일 |
