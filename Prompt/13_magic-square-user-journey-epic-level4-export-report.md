# 4x4 magic square implementation scenarios
_Exported on 4/28/2026 at 08:34:46 GMT+9 from Cursor (3.2.11)_

---

**User**

Level 4:구현 시나리오 - Technical를 다음 내용처럼 작성해 주세요.
Feature: 4x4 마방진 완성
불변조건 기반 로직을 검증하기 위해
TDD를 연습하는 개발자로서
부분적으로 채워진 4x4 마방진을 완성하고 싶다
Background:
Given 4x4 행렬이 주어지고
And 0은 빈칸을 의미하며
And 정확히 2개의 셀이 0을 포함하고 있고
And 숫자는 1부터 16 사이여야 하며
And 0을 제외한 중복 숫자는 허용되지 않으며
And 4x4의 마방진 상수는 34이다

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
Scenario: 빈칸 개수가 올바르지 않은 경우
Given 행렬에 빈칸이 1개만 존재할 때
When 유효성 검증을 수행하면
Then 오류가 발생해야 한다
Scenario: 중복 숫자가 존재하는 경우
Given 0을 제외한 중복 숫자가 포함된 행렬일 때
When 유효성 검증을 수행하면
Then 오류가 발생해야 한다
Scenario: 값의 범위를 벗어난 경우
Given 행렬에 16을 초과하는 숫자가 포함되어 있을 때
When 유효성 검증을 수행하면
Then 오류가 발생해야 한다


---

**Cursor**

기존 Reporter 파일 형식과 Level 3 구조를 확인한 뒤 Level 4 Technical 시나리오 문서를 작성합니다.



Level 3와 동일한 Reporter 메타데이터·교차 참조를 두고, 요청하신 Gherkin 형식의 Level 4 Technical 시나리오 문서를 `Reporter/12_...`로 추가합니다.



시나리오 1·2에서 표가 중복되어 있습니다. Gherkin 블록만 남기고 정리합니다.



다음 파일에 **Level 4 — 구현 시나리오 (Technical)** 를 반영해 두었습니다.

**파일:** `Reporter/12_magic-square-user-journey-epic-level4-technical-scenarios-report.md`

포함 내용은 다음과 같습니다.

- **메타:** 작성일, Level 3 보고서와의 정합, 작성 목적·범위  
- **Feature:** 4×4 마방진 완성 (역할·목적·이익 문장 그대로)  
- **Background:** 4×4, `0` = 빈칸, 빈칸 2개, 1~16, 비0 중복 불가, 상수 34  
- **Scenario 5개:**  
  1. 작은 수 → 큰 수로 완성 + 길이 6 배열 + 좌표 1-index  
  2. 역순 배치로 완성  
  3. 빈칸 1개 → 검증 시 오류  
  4. 비0 중복 → 오류  
  5. 16 초과 값 → 오류  
- **부록:** Level 3 Story 1~5와의 매핑 표, 문서 이력  

Gherkin은 ` ```gherkin ` 블록 안에 두었고, 예시 격자는 시나리오 안의 Data Table 형태로 넣었습니다.

---

**User**

Reporter 폴더에  지금 작업한 내용을 보고서로 내보내줘.

---

**Cursor**

Level 2보내기 보고서 형식과 Reporter 폴더 상태를 확인한 뒤, Level 3·4를 포함한 통합보내기 보고서를 작성합니다.



Level 3 보내기 보고서와 동일한 형식으로 Level 4 구현 시나리오 보내기 보고서를 `13_...`로 추가합니다. (Reporter에 `12_`가 두 개라 Level 4 보내기는 `13`으로 구분합니다.)



`Reporter`에 **보내기용 통합 보고서**를 추가했습니다.

## 생성 파일

**`Reporter/13_magic-square-user-journey-epic-level4-export-report.md`**

- **제목:** Magic Square 사용자 여정 — 보고서보내기 (Level 4 구현 시나리오 · Technical)  
- **구성:** `10_`·`12_level3_export`와 같은 패턴으로 **보내기 요약 표** → 작성 목적·범위 → **Level 4 전문**(Feature, Background, 시나리오 5개) → Level 3 매핑 → **관련 Reporter 목록** → 문서 이력  
- **본문:** `12_magic-square-user-journey-epic-level4-technical-scenarios-report.md`와 동일한 Gherkin 전문을 한 파일에 담아 배포·아카이브에 쓰기 쉽게 했습니다.

## Reporter 안 사용자 여정 계열 정리

| 파일 | 용도 |
|------|------|
| `09_...business-goal...` | Level 1 작업본 |
| `10_...level2-export...` | Level 1·2 보내기 |
| `11_...level3-user-stories...` | Level 3 작업본 |
| `12_...level3-export...` | Level 3 보내기 |
| `12_...level4-technical-scenarios...` | Level 4 작업본 |
| **`13_...level4-export...`** | **Level 4 보내기(방금 추가)** |

참고로 `12_` 접두어가 Level 3 보내기와 Level 4 작업본에 겹쳐 있어, 보내기 문서는 **`13_`**로 구분해 두었고, `13` 안의 표에 두 `12_` 파일을 함께 적어 두었습니다.

Level 3·4를 **한 파일**로만 묶은 보내기가 필요하면 그 형식으로도 만들 수 있습니다.

