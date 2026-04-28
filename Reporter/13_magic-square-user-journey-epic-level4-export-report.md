# Magic Square 사용자 여정 — 보고서보내기 (Level 4 구현 시나리오 · Technical)

**보내기 일자:** 2026-04-28  
**산출물 유형:** Reporter 폴더 공유·아카이브용 Level 4 통합 보고서  
**관련 원본:** `Reporter/12_magic-square-user-journey-epic-level4-technical-scenarios-report.md` (동일 범위의 작업본과 정합)  
**상위 맥락:** `Reporter/11_magic-square-user-journey-epic-level3-user-stories-report.md`, `Reporter/12_magic-square-user-journey-epic-level3-export-report.md` (Level 3 User Stories)

---

## 보내기 요약

| 구분 | 내용 |
|------|------|
| **Level 4** | Gherkin 기반 **구현 시나리오(Technical)** — Feature, Background, 시나리오 5건 |
| **도메인** | 4×4 부분 채움 마방진 완성, 빈칸(`0`) 2개, 누락 숫자 2개, 상수 34, 순·역 배치, 유효성 실패 |
| **형식** | Feature 서술, Background 전제, Given/When/Then 및 예시 Data Table |
| **Level 3 매핑** | Story 1~5(입력 검증·빈칸·누락 숫자·판정·두 조합)와 시나리오 절 대응 |

아래 본문은 위 요약을 **전문**으로 펼친 것이다.

---

**작성 목적:** Epic 하위 **Level 4: 구현 시나리오(Technical)**를 한 문서로 보존·배포하여, TDD·BDD·코드 리뷰 시 **동일한 시나리오·불변조건**을 참조할 수 있게 한다.  
**범위:** `12_magic-square-user-journey-epic-level4-technical-scenarios-report.md` 작업본과 동일한 Feature·Background·시나리오 전문.

**참고:** “Invariant 기반 사고 훈련 시스템” 및 4×4 Magic Square 도메인 전제를 반영하였다.

---

## Level 4 — 구현 시나리오 (전문)

### Feature: 4×4 마방진 완성

```gherkin
Feature: 4x4 마방진 완성
  불변조건 기반 로직을 검증하기 위해
  TDD를 연습하는 개발자로서
  부분적으로 채워진 4x4 마방진을 완성하고 싶다
```

---

### Background

```gherkin
Background:
  Given 4x4 행렬이 주어지고
  And 0은 빈칸을 의미하며
  And 정확히 2개의 셀이 0을 포함하고 있고
  And 숫자는 1부터 16 사이여야 하며
  And 0을 제외한 중복 숫자는 허용되지 않으며
  And 4x4의 마방진 상수는 34이다
```

---

### Scenario: 작은 수 → 큰 수 순서로 마방진이 완성되는 경우

```gherkin
Scenario: 작은 수 → 큰 수 순서로 마방진이 완성되는 경우
  Given 다음과 같은 행렬이 주어졌을 때:
    | 16 |  2 |  3 | 13 |
    |  5 | 11 | 10 |  8 |
    |  9 |  7 |  0 | 12 |
    |  4 | 14 | 15 |  0 |
  When 시스템이 빈칸 좌표를 찾고
  And 누락된 두 숫자를 찾은 뒤
  And 작은 숫자를 첫 번째 빈칸에 배치하고
  And 큰 숫자를 두 번째 빈칸에 배치하면
  Then 모든 행의 합은 34여야 하고
  And 모든 열의 합은 34여야 하며
  And 두 대각선의 합도 34여야 하고
  And 결과는 길이 6의 배열로 반환되어야 하며
  And 반환되는 좌표는 1-index 기준이어야 한다
```

---

### Scenario: 역순 배치 시 마방진이 완성되는 경우

```gherkin
Scenario: 역순 배치 시 마방진이 완성되는 경우
  Given 다음과 같은 행렬이 주어졌을 때:
    | 16 |  2 |  3 | 13 |
    |  5 | 11 | 10 |  8 |
    |  9 |  7 |  0 | 12 |
    |  4 | 14 | 15 |  0 |
  When 작은 숫자를 첫 번째 빈칸에 배치했을 때 마방진이 되지 않고
  And 큰 숫자를 첫 번째 빈칸에 배치했을 때 마방진이 되면
  Then 시스템은 역순 배치 결과를 반환해야 하며
  And 최종 행렬은 마방진 상수 34를 만족해야 한다
```

---

### Scenario: 빈칸 개수가 올바르지 않은 경우

```gherkin
Scenario: 빈칸 개수가 올바르지 않은 경우
  Given 행렬에 빈칸이 1개만 존재할 때
  When 유효성 검증을 수행하면
  Then 오류가 발생해야 한다
```

---

### Scenario: 중복 숫자가 존재하는 경우

```gherkin
Scenario: 중복 숫자가 존재하는 경우
  Given 0을 제외한 중복 숫자가 포함된 행렬일 때
  When 유효성 검증을 수행하면
  Then 오류가 발생해야 한다
```

---

### Scenario: 값의 범위를 벗어난 경우

```gherkin
Scenario: 값의 범위를 벗어난 경우
  Given 행렬에 16을 초과하는 숫자가 포함되어 있을 때
  When 유효성 검증을 수행하면
  Then 오류가 발생해야 한다
```

---

## Level 3 매핑 (참고)

| Level 4 시나리오·절 | Level 3 Story |
|---------------------|---------------|
| Background, 빈칸·범위·중복·상수 34 | Story 1 — 입력 검증 |
| 빈칸 좌표 찾기 | Story 2 — 빈칸 탐색 |
| 누락된 두 숫자 | Story 3 — 누락 숫자 탐색 |
| 행·열·대각선 34 | Story 4 — 마방진 판정 |
| 작은 수→큰 수 / 역순, 길이 6·1-index | Story 5 — 두 조합 시도 |

---

## 관련 Reporter 산출물 (사용자 여정 계열)

| 파일 | 역할 |
|------|------|
| `Reporter/09_magic-square-user-journey-epic-business-goal-report.md` | Level 1 작업본 |
| `Reporter/10_magic-square-user-journey-epic-level2-export-report.md` | Level 1·2 보내기 |
| `Reporter/11_magic-square-user-journey-epic-level3-user-stories-report.md` | Level 3 작업본 |
| `Reporter/12_magic-square-user-journey-epic-level3-export-report.md` | Level 3 보내기 |
| `Reporter/12_magic-square-user-journey-epic-level4-technical-scenarios-report.md` | Level 4 작업본 |
| `Reporter/13_magic-square-user-journey-epic-level4-export-report.md` | Level 4 보내기(본 문서) |
| `Reporter/14_magic-square-user-journey-epic-level5-scenario-verification-report.md` | Level 5 시나리오 검증 작업본 |
| `Reporter/15_magic-square-user-journey-epic-level5-export-report.md` | Level 5 보내기 |

---

## 문서 이력 (보내기)

| 일자 | 내용 |
|------|------|
| 2026-04-28 | Level 4 Technical(Gherkin) 시나리오를 Reporter **보내기 보고서**(`13_...`)로 보냄 — 원본 `12_magic-square-user-journey-epic-level4-technical-scenarios-report.md`과 본문 동일 |
