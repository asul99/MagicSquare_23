# PRD — Magic Square (4×4) TDD 연습 프로젝트

**문서 성격:** 제품·도메인 요구사항 정의 (구현 코드 없음).  
**근거 문서:** `Reporter/04_magic-square-cursorrules-tdd-rules-review-report.md`(골격·검토 관점), `Reporter/01_magic-square-problem-definition-report.md`(문제·동기), `Reporter/02_magic-square-clean-architecture-tdd-design-report.md`(기능·계약·성공·실패 정책), `Reporter/03_magic-square-cursorrules-tdd-rules-report.md`(Red–Green–Refactor 품질 원칙).  
**범위 고정:** 본 PRD는 **4×4, 빈칸 2개, 두 조합 시도 후 `int[6]` 반환 또는 표준 오류**만을 다룬다. UI·DB·Web·N×N 일반화·완전 생성 알고리즘은 명시적 Out-of-Scope다.

---

## 1. Executive Summary

본 프로젝트는 **4×4 부분 채움 격자**에서 두 빈칸에 누락된 두 숫자를 배치해 **마방진 불변조건(행·열·주·부대각선 합 34, 1~16 각 1회)**을 만족시키는지 판단하고, 규칙에 따라 **1-index 좌표와 배치 숫자 순서가 고정된 `int[6]`**을 반환한다. 알고리즘 난이도가 아니라 **TDD로 계약을 고정하고, 불변조건을 테스트로 검증 가능한 문장으로 유지하는 훈련**이 목적이다. 핵심 역량은 **도메인 불변조건 명세화**, **Boundary와 Domain의 이중 트랙 계약 테스트**, **Concept → Rule → Use Case → Contract → Test → Component 추적성**이다.

---

## 2. Problem Statement (문제 정의)

### 2.1 문제의 정의(올바른 관점)

표면적 표현인 “4×4 마방진을 만든다”가 아니라, **주어진 입력 계약을 만족하는 상태에서, 결정적 규칙으로 빈칸·누락 수를 식별하고, 최대 두 번의 후보 배치를 검사하여 마방진 불변조건을 만족하는 완성이 존재하는지 판단하고, 성공 시 규격화된 출력 벡터로 표현한다**는 문제다. “완성”은 **불변조건 INV-05~09를 동시에 만족하는 완전 격자(0 없음)**로 정의한다.

### 2.2 입력·출력 계약이 핵심인 이유

- 테스트는 **호출자와 구현 간 계약**이다. 행렬 크기·빈칸 개수·값 범위·중복·빈칸 순서·`n1,n2` 의미가 고정되지 않으면, 실패가 **버그인지 스펙 변경인지** 구분할 수 없다.
- **경계(Boundary)**는 원시 `int[][]`의 구조적·도메인 전제를 검증하고, **도메인**은 전제가 성립한 뒤의 순수 판단만 수행한다. 계약이 문서·테스트에 없으면 Dual-Track TDD의 **RED 대상**이 사라진다.

---

## 3. Target Users

| 구분 | 설명 |
|------|------|
| **주 사용자** | TDD·불변조건·레이어 분리를 연습하는 **학습자(구현자)** |
| **이해관계자** | 동일 계약으로 리뷰·채점하는 **리뷰어/교육자** |
| **사용 목적** | 콘솔 또는 테스트 러너에서 **단위·통합 테스트를 반복 실행**하며 Red–Green–Refactor 사이클을 유지 |
| **사용 환경** | JVM 기반 테스트 도구(예: JUnit), IDE, CI. **별도 UI·DB 없이** 호출 가능한 API 또는 Application 진입점 |

---

## 4. Scope

### 4.1 In-Scope

- **입력 검증(Boundary):** 4×4, 빈칸 정확히 2개, 값 0 또는 1~16, 0 제외 중복 없음
- **빈칸 좌표:** row-major(행 우선, 행·열 오름차순) 스캔에서 첫 번째·두 번째 `0`의 1-index 좌표
- **누락 숫자:** `{1..16}`에서 격자에 나타난 0이 아닌 값의 집합을 제외한 정확히 2개
- **마방진 판정:** 완전 격자에 대해 합 34(행 4, 열 4, 주대각선, 부대각선) 및 1~16 각 1회
- **해 찾기:** 시도 1 실패 시 시도 2; 성공 시 출력 규칙에 따른 `int[6]`; 실패·모호 시 **§6·§11에 명시된 오류 정책**
- **Concept-to-Code 추적:** §12 매트릭스 유지

### 4.2 Out-of-Scope

- **UI 화면** 개발(웹·데스크톱·모바일)
- **DB 저장·조회**, 파일 영속 레이어(본 PRD 기본 범위에서 제외; 확장 시 별도 PRD 부록)
- **N×N 일반화**(n≠4, 상수≠34) — 필요 시 “확장 항목”으로만 언급, 본 구현 요구 아님
- **마방진 완전 생성**(임의 조건에서 모든 해 탐색·열거)
- **구현 소스 코드** — 본 문서에 포함하지 않음

---

## 5. Functional Requirements (기능 요구사항)

공통 전제: 모든 FR의 “입력”은 논리적 의미이며, FR-01을 통과한 입력만 FR-02 이후의 도메인 전제로 사용한다.

---

### FR-01 — 입력 검증 (Boundary)

| 항목 | 내용 |
|------|------|
| **Feature ID** | FR-01 |
| **설명** | 호출자가 제출한 `int[][]`가 본 PRD의 입력 계약을 만족하는지 검사한다. 위반 시 도메인 로직을 호출하지 않는다. |
| **입력** | `int[][] grid` (참조 `grid` 및 하위 행 참조는 호출자 소유) |
| **처리 규칙** | (1) `grid != null`, `grid.length == 4`, 모든 행 `row != null` 및 `row.length == 4`. (2) 셀 값은 `0` 또는 `1 <= v <= 16`. (3) 값 `0`인 셀의 개수는 정확히 2. (4) `0`이 아닌 값들은 서로 중복 없음. **불변조건:** 검증 과정에서 `grid`의 어떤 셀 값도 변경하지 않는다(§7 부작용 금지와 동일 정책). |
| **출력** | 검증 성공 시 도메인으로 전달 가능한 동일 논리 격자(참조 정책은 구현에서 결정하되 **원본 배열 불변**). 실패 시 §6의 `errorCode` 및 고정 `message`를 담는 실패 결과(또는 예외; 프로젝트 단일 정책으로 선택하되 테스트는 동일 기대로 검증). |
| **승인 기준 (AC)** | AC-FR01-1: `null` 또는 길이≠4인 최상위 배열이면 `INVALID_GRID_SIZE` 및 메시지 `Grid must be 4x4.`와 정확히 일치한다. AC-FR01-2: 임의 행이 `null`이거나 길이≠4이면 동일 코드·메시지다. AC-FR01-3: `0` 개수가 0,1,3,…이면 `INVALID_EMPTY_CELL_COUNT` 및 `Exactly two cells must be empty (value 0).`와 정확히 일치한다. AC-FR01-4: 셀에 17 또는 -1이 존재하면 `VALUE_OUT_OF_RANGE` 및 `Each cell must be 0 or an integer from 1 to 16.`와 정확히 일치한다. AC-FR01-5: 0 제외 동일 값이 2회 이상이면 `DUPLICATE_NONZERO_VALUE` 및 `Non-zero values must not repeat.`와 정확히 일치한다. AC-FR01-6: 위 실패 케이스에서 도메인 `resolve`/`isMagic` 등 핵심 연산이 **0회** 호출됨을 테스트가 검증한다(Mock 또는 스파이). AC-FR01-7: 검증 전후 동일 `int[][]` 참조에 대해 모든 셀 값이 비트 동일(bitwise 동등)하다. |
| **오류/예외 정책** | §6 BR-ERR 및 §8.1 표준 문구. Boundary에서만 매핑 가능한 일반 오류는 `DOMAIN_UNEXPECTED` / `An unexpected domain error occurred.` (도메인에서 처리되지 않은 예외 상황에 한함). |

---

### FR-02 — 빈칸 탐색

| 항목 | 내용 |
|------|------|
| **Feature ID** | FR-02 |
| **설명** | FR-01을 만족하는 격자에서 값 `0`인 두 셀의 1-index 좌표 `(r1,c1)`, `(r2,c2)`를 **결정적**으로 산출한다. |
| **입력** | FR-01 통과 격자 |
| **처리 규칙** | 행 인덱스 `r`를 1→4, 열 `c`를 1→4 순서로 스캔할 때 처음 만나는 `0`이 `(r1,c1)`, 그 다음 `0`이 `(r2,c2)` (내부 0-index 사용 시 경계에서만 변환). **불변조건:** `r1,c1,r2,c2 ∈ {1,2,3,4}` 및 `(r1,c1)`이 lexicographically `(r2,c2)`보다 앞선다. |
| **출력** | 두 좌표 쌍(도메인 내부 표현은 구현 자유) |
| **승인 기준 (AC)** | AC-FR02-1: 알려진 격자에 대해 기대 `(r1,c1,r2,c2)`가 스펙 스캔 순서와 일치한다. AC-FR02-2: FR-01 실패 격자에서는 본 기능이 호출되지 않거나, 호출되지 않도록 설계된 진입 경로만 허용된다. |
| **오류/예외 정책** | FR-01이 보장하는 한 빈칸 2개는 존재하므로 별도 도메인 오류는 발생하지 않아야 한다. |

---

### FR-03 — 누락 숫자 탐색

| 항목 | 내용 |
|------|------|
| **Feature ID** | FR-03 |
| **설명** | 0이 아닌 칸에 나타난 값의 집합을 이용해 `{1..16}`에서 빠진 정수 두 개 `{a,b}`를 구한다. |
| **입력** | FR-01 통과 격자 |
| **처리 규칙** | `missing = {1..16} \ { v \| cell(v) != 0 }`. 결과 집합 크기는 정확히 2. **불변조건:** `a != b`, `1 <= a,b <= 16`. |
| **출력** | 두 정수의 집합(순서는 FR-05에서 결정) |
| **승인 기준 (AC)** | AC-FR03-1: 완성 마방진에서 임의 두 칸을 0으로 바꾼 입력에 대해 누락 집합이 수학적으로 그 두 수와 일치한다. AC-FR03-2: FR-01을 만족하는 모든 유효 입력에서 누락 개수가 2가 아닌 경우는 존재하지 않음을 단위 테스트로 증명(모순 입력은 FR-01에서 차단). |
| **오류/예외 정책** | 논리상 불가; 발생 시 `DOMAIN_UNEXPECTED`로 간주 가능. |

---

### FR-04 — 마방진 판정

| 항목 | 내용 |
|------|------|
| **Feature ID** | FR-04 |
| **설명** | **0이 없는** 4×4 정수 격자가 마방진 불변조건을 만족하는지 판별한다. |
| **입력** | 4×4, 모든 셀 1~16 |
| **처리 규칙** | (1) multiset이 `{1,..,16}`과 일치. (2) 각 행 합=34, 각 열 합=34, 주대각선 합=34, 부대각선 합=34. **불변조건:** BR-01~BR-04 및 마법 상수 34. |
| **출력** | `true` 또는 `false`(또는 실패 타입; 0 존재 시 호출 금지 정책 택일) |
| **승인 기준 (AC)** | AC-FR04-1: 알려진 완성 4×4 마방진에 대해 `true`. AC-FR04-2: 행합만 34로 맞추고 대각선을 깨트린 완전 격자에 대해 `false`. AC-FR04-3: 합은 34이나 1~16 multiset 위반인 완전 격자에 대해 `false`. AC-FR04-4: 셀에 0이 남아 있으면 본 판정 API는 호출되지 않거나, 호출 시 명시적 실패로 테스트 고정. |
| **오류/예외 정책** | 0 포함 입력은 FR-05 조합 단계에서 완성 후에만 본 판정에 전달한다. |

---

### FR-05 — 해 찾기 (solution): 두 조합 시도 및 반환

| 항목 | 내용 |
|------|------|
| **Feature ID** | FR-05 |
| **설명** | 누락 두 수를 두 빈칸에 넣는 두 가지 시도 순서를 규칙대로 평가하고, 성공 시 `int[6]`을 반환한다. |
| **입력** | FR-01~03 결과(격자, `(r1,c1,r2,c2)`, 누락 `{a,b}`, `min=min(a,b)`, `max=max(a,b)`) |
| **처리 규칙** | **시도 1:** `(r1,c1)`에 `min`, `(r2,c2)`에 `max`를 넣은 완전 격자를 구성하고 FR-04로 판정. true이면 출력 `[r1,c1,min,r2,c2,max]`를 반환하고 종료. **시도 2:** 시도 1이 false일 때만 수행. `(r1,c1)`에 `max`, `(r2,c2)`에 `min`을 넣어 FR-04. true이면 출력 `[r1,c1,max,r2,c2,min]`을 반환하고 종료(시도 1에서 정의한 `n1,n2` 순서 대비 **역순**: 첫 빈칸에 큰 수, 둘째 빈칸에 작은 수). 둘 다 false이면 `NO_SOLUTION`. 둘 다 true이면 `AMBIGUOUS_SOLUTION`(본 PRD에서 허용되는 유일한 “둘 다 성공” 정책). |
| **출력** | 성공: `int[6]` = `[r1,c1,n1,r2,c2,n2]` (모두 1-index 좌표, `n1,n2`는 해당 좌표에 배치된 값). 실패: §6 오류. |
| **승인 기준 (AC)** | AC-FR05-1: 시도 1만 성공하는 입력에 대해 반환 배열이 `[r1,c1,min,r2,c2,max]`와 **원소 단위 동일**하다. AC-FR05-2: 시도 1 실패·시도 2만 성공하는 입력에 대해 `[r1,c1,max,r2,c2,min]`과 동일하다. AC-FR05-3: 둘 다 실패 시 `NO_SOLUTION` 및 메시지 `No valid magic-square completion exists for this grid.` 정확 일치. AC-FR05-4: 둘 다 성공 시 `AMBIGUOUS_SOLUTION` 및 `Multiple valid orderings satisfy the rule; input is rejected.` 정확 일치. AC-FR05-5: 시도 1 성공 시 시도 2를 수행하지 않음을 테스트가 검증(호출 횟수 또는 플래그). |
| **오류/예외 정책** | `NO_SOLUTION`, `AMBIGUOUS_SOLUTION`은 Boundary 출력 스키마와 동일 코드·문구로 전달된다. |

---

## 6. Business Rules (도메인 규칙)

아래는 **유효 입력·완성 상태에서 항상 참**이어야 하는 규칙이다.

| ID | 규칙 문장 |
|----|-----------|
| BR-01 | 격자는 4행 4열이며, 모든 행의 길이는 4이다. |
| BR-02 | 각 셀의 값은 `0` 또는 `1` 이상 `16` 이하의 정수이다. |
| BR-03 | 값이 `0`인 셀은 정확히 2개이다. |
| BR-04 | `0`이 아닌 임의의 두 셀의 값은 서로 다르다. |
| BR-05 | “첫 번째 빈칸”과 “둘째 빈칸”은 행 번호 오름차순, 동일 행이면 열 번호 오름차순으로 `0`을 스캔했을 때의 첫 번째·두 번째 `0`이다(1-index 보고 시 동일 순서). |
| BR-06 | 누락 숫자 두 개는 집합 `{1,…,16}`에서 격자에 등장한 0이 아닌 값을 제외한 결과이며, 서로 다르다. |
| BR-07 | 완성 마방진에서 네 행·네 열·주대각선·부대각선 각각의 네 수의 합은 **34**이다. |
| BR-08 | 완성 마방진에서 1부터 16까지 각 정수는 정확히 한 번씩 나타난다. |
| BR-09 | 성공 응답 `int[6]`의 `r1,c1,r2,c2`는 각각 1 이상 4 이하의 정수이다. |
| BR-10 | 성공 응답에서 `n1`은 좌표 `(r1,c1)`에 배치된 값, `n2`는 `(r2,c2)`에 배치된 값이다. |
| BR-11 | 시도 1이 성공하면 `n1 = min(누락 두 수)`, `n2 = max(누락 두 수)`이다. |
| BR-12 | 시도 1이 실패하고 시도 2만 성공하면 `n1 = max(누락 두 수)`, `n2 = min(누락 두 수)`이다. |
| BR-ERR-01 | `INVALID_GRID_SIZE`의 메시지는 `Grid must be 4x4.`와 **전체 문자열 일치**(앞뒤 공밍·줄바꿈 없음)이다. |
| BR-ERR-02 | `INVALID_EMPTY_CELL_COUNT`의 메시지는 `Exactly two cells must be empty (value 0).`와 전체 일치한다. |
| BR-ERR-03 | `VALUE_OUT_OF_RANGE`의 메시지는 `Each cell must be 0 or an integer from 1 to 16.`와 전체 일치한다. |
| BR-ERR-04 | `DUPLICATE_NONZERO_VALUE`의 메시지는 `Non-zero values must not repeat.`와 전체 일치한다. |
| BR-ERR-05 | `NO_SOLUTION`의 메시지는 `No valid magic-square completion exists for this grid.`와 전체 일치한다. |
| BR-ERR-06 | `AMBIGUOUS_SOLUTION`의 메시지는 `Multiple valid orderings satisfy the rule; input is rejected.`와 전체 일치한다. |
| BR-ERR-07 | `DOMAIN_UNEXPECTED`의 메시지는 `An unexpected domain error occurred.`와 전체 일치한다. |

---

## 7. Non-Functional Requirements

| ID | 요구사항 | 검증 방법 |
|----|----------|-----------|
| NFR-01 | **Domain Logic** 라인 커버리지 **≥ 95%** | 빌드 도구의 커버리지 리포트에서 수치 확인 |
| NFR-02 | **Boundary Validation** 라인 커버리지 **≥ 85%** | 동일 |
| NFR-03 | **결정론:** 동일 입력에 대해 동일 출력(성공 배열 또는 동일 `errorCode`+`message`) | 동일 입력 연속 실행 테스트 |
| NFR-04 | **부작용 금지:** Boundary·Domain 공통으로, 호출자가 전달한 `int[][]` 및 각 행 배열에 대해 **메서드/유스케이스 종료 후 모든 셀 값이 호출 전과 비트 동등** | 호출 전 깊은 복사 스냅샷과 `assertArrayEquals` 등으로 검증 |
| NFR-05 | **성능(선택):** 단일 유효 입력에 대한 end-to-end 처리 시간이 **50ms 이하**(개발 머신 기준, CI에서는 상한 완화 가능)를 만족 | `@Timeout` 또는 시간 측정 assertion(상한 명시) |

**품질 원칙(Report/03·04 정합):** Red 단계에서는 **의도된 실패**만 허용하고 프로덕션 변경은 최소화한다. Green은 **현재 실패 테스트 통과에 필요한 최소 변경**만 한다. Refactor는 **관측 가능한 동작 불변**을 유지하며, 커버리지는 리팩터 전 대비 낮아지지 않는다(측정 가능 시).

---

## 8. Dual-Track TDD Strategy

### 8.1 Track A — Boundary(UI) TDD

- **Contract-first 테스트 항목:** `INVALID_GRID_SIZE`, `INVALID_EMPTY_CELL_COUNT`, `VALUE_OUT_OF_RANGE`, `DUPLICATE_NONZERO_VALUE`, `NO_SOLUTION`, `AMBIGUOUS_SOLUTION`, `DOMAIN_UNEXPECTED` 각각에 대해 `errorCode` 및 **전체 `message` 문자열** assert. 유효 입력 1건은 Mock 도메인으로 `int[6]` 동등성 assert.
- **실패 정책:** 예외를 쓰는 경우에도 **타입·메시지**는 위 스키마와 동일하게 검증 가능해야 한다. Domain은 Boundary에 **에러 코드**만 넘기고 문구 중복 정의는 Boundary 한 곳으로 제한하는 것이 바람직하나(SRP), 프로젝트 정책이 “도메인 예외 직통”이어도 **문구 표**는 단일 SoT로 유지한다.

### 8.2 Track B — Domain(Logic) TDD

- **메서드 단위 테스트:** `locateEmptyCells`, `computeMissingNumbers`, `isCompletedMagicSquare`, `resolveTwoPlacements`(명칭 예시) 각각에 대해 성공·실패 경로.
- **불변조건 테스트:** BR-01~BR-12에 대응하는 표 형 테스트(표준 4×4 예제·깨진 대각선·중복·범위 외 값은 Boundary에서 차단되는지/도메인 전제 분리되는지 구분).

### 8.3 병렬 진행 규칙

- **금지:** “도메인 전부 구현 후 경계 추가” 단일 워터폴.
- **권장 사이클:** 동일 주제에 대해 **UI(Boundary) RED & Logic RED → UI GREEN & Logic GREEN → REFACTOR**를 짧은 루프로 반복. 한 기능 주제(예: 빈칸 개수 오류)를 고를 때 Track A·B에 **대칭되는 실패 테스트**를 먼저 추가한다.
- **근거:** `Reporter/04`에 명시된 대로 IDE가 단계를 강제하지 않으므로, **PR·태스크 단위로 RED 범위를 쪼개** 인간이 루프를 집행한다.

---

## 9. Test Plan (QA)

### 9.1 시나리오 기반 테스트 목록

| 시나리오 ID | 조건 | 기대 |
|---------------|------|------|
| TP-01 | 완성 마방진에서 두 칸을 0으로, 시도 1이 성공하는 배치 | `int[6]`이 시도 1 규칙과 일치 |
| TP-02 | 시도 1 실패·시도 2만 성공 | `n1>n2`이고 BR-12 만족 |
| TP-03 | 시도 1·2 모두 실패 | `NO_SOLUTION` + 고정 메시지 |
| TP-04 | 시도 1·2 모두 성공(이론상 가능 입력) | `AMBIGUOUS_SOLUTION` + 고정 메시지 |
| TP-05 | 행 수 3 | `INVALID_GRID_SIZE`, 도메인 미호출 |
| TP-06 | 빈칸 1개 | `INVALID_EMPTY_CELL_COUNT` |
| TP-07 | 값 17 | `VALUE_OUT_OF_RANGE` |
| TP-08 | 중복 값 | `DUPLICATE_NONZERO_VALUE` |

### 9.2 회귀 테스트 정책

- `int[6]`·1-index·`n1,n2` 의미 변경 시 PR에 **“계약 변경”** 라벨 및 리뷰어 2인 승인(팀 규칙에 위임).
- 에러 `message` 변경은 **의도된 계약 변경**으로만 허용; CI에서 문자열 전체 assert 유지.
- 기존 테스트 삭제 금지; 교체 시 동일 시나리오 ID 범위 커버를 증명하는 커밋 메시지 필수.

### 9.3 테스트 데이터 — 대표 4×4 행렬

아래 **완성 마방진**은 행·열·대각 합이 34이며 1~16 순열이다. 부분 입력은 **교육용 예시**로 두 칸을 `0`으로 바꾼 뒤 FR-05 결과를 별도 골든 파일로 고정한다.

**완성 격자 G0 (0-index 내부 표기 예시; PRD 검증 시 1-index로 변환해 사용):**

```text
16  3  2  13
5  10 11  8
9   6  7  12
4  15 14  1
```

| ID | 용도 |
|----|------|
| TD-01 | G0 그대로(빈칸 0개) — **FR-01이 거부**해야 함(빈칸 2개 아님). 완성 판정 단위 테스트용으로는 0 없는 복사본 사용. |
| TD-02 | G0에서 임의 두 위치를 `0`으로 — 빈칸 순서·누락 수·시도 1/2 중 어느 쪽 성공인지 케이스별로 골든 벡터 고정 |
| TD-03 | 합만 맞춘 위조 완전 격자(대각선 실패) — FR-04 `false` |
| TD-04 | 4×4이나 마방진 불가능한 0 두 개 패턴 — `NO_SOLUTION` |

### 9.4 Property / Invariant 기반 체크 항목

| PID | 속성 |
|-----|------|
| P-01 | FR-01 통과 격자에 대해 `count(0)==2` |
| P-02 | FR-02 결과는 row-major 순서와 일치 |
| P-03 | 완성 후 FR-04 `true`이면 모든 행·열·대각 합은 34 |
| P-04 | 완성 후 FR-04 `true`이면 multiset은 {1,…,16} |
| P-05 | 동일 입력 두 번 호출 시 결과 동일(NFR-03) |

---

## 10. Architecture Overview (High-Level)

### 10.1 레이어

| 레이어 | 책임 |
|--------|------|
| **Boundary** | `null`/크기/빈칸 개수/범위/중복 검증; 도메인 실패 코드를 외부 계약으로 매핑; **입력 배열 불변** 보장 |
| **Domain** | 빈칸·누락 수·완성 판정·두 시도 해결; **Boundary에 의존하지 않음** |
| **Application(선택)** | Boundary와 Domain을 조합하는 얇은 오케스트레이션만 허용 |

### 10.2 SRP·OCP

- **SRP:** 검증은 Boundary, 판정은 Domain, 출력 벡터 조립은 Domain 또는 Boundary 직전 단일 컴포넌트 중 하나만이 책임(중복 금지).
- **OCP:** N×N 확장은 새 타입·새 상수 전략으로 열리되, **본 PRD 범위 코드 경로는 4×4 고정**으로 닫는다.

### 10.3 의존성 방향

```text
Caller → Boundary → Domain 포트(인터페이스)
           ↑
      (Domain은 Boundary를 알지 못함)
```

---

## 11. Risks & Ambiguities

| 결정 ID | 결정 내용 |
|---------|-----------|
| DEC-01 | 두 시도 모두 실패 시 **`NO_SOLUTION`** 및 BR-ERR-05 메시지로 처리한다. |
| DEC-02 | 두 시도 모두 성공 시 **`AMBIGUOUS_SOLUTION`** 및 BR-ERR-06 메시지로 처리한다(입력 거부). |
| DEC-03 | 시도 1이 성공하면 시도 2를 **실행하지 않는다**. |
| DEC-04 | “시도 2 성공 시 역순 반환”은 **`[r1,c1,n1,r2,c2,n2]`에서 `n1`이 큰 수, `n2`가 작은 수**로 해석한다(좌표 순서는 FR-02와 동일). |
| DEC-05 | 호출자 배열 **불변**; 내부 작업용 복사는 구현 세부이나 **관측 가능 부작용 없음**은 테스트로 고정(NFR-04). |

**자주 실수하는 포인트:** 0-index vs 1-index 혼동; row-major 첫 빈칸 정의; 시도 1 성공 후 시도 2 중복 실행; 입력 배열 제자리 수정; `NO_SOLUTION`과 `false` 판정 혼동; 에러 메시지 부분 문자열 assert로 인한 계약 붕괴.

---

## 12. Traceability Matrix (필수)

| Concept / Invariant | Business Rule | Feature (FR) | Acceptance Criteria (요약) | Test Case / 시나리오 | Component |
|---------------------|---------------|--------------|------------------------------|----------------------|-----------|
| 4×4 크기 | BR-01 | FR-01 | AC-FR01-1,2 | TP-05, U계열 매핑 | Boundary |
| 빈칸 정확히 2 | BR-03 | FR-01 | AC-FR01-3 | TP-06 | Boundary |
| 값 0 또는 1~16 | BR-02 | FR-01 | AC-FR01-4 | TP-07 | Boundary |
| 0 제외 중복 없음 | BR-04 | FR-01 | AC-FR01-5 | TP-08 | Boundary |
| 검증 시 도메인 미호출 | 입력 계약 | FR-01 | AC-FR01-6 | Boundary Mock 테스트 | Boundary |
| 입력 배열 불변 | NFR-04 | FR-01 | AC-FR01-7 | 스냅샷 비교 테스트 | Boundary, Domain 진입 |
| Row-major 빈칸 | BR-05 | FR-02 | AC-FR02-1 | D-T03 대응, TP-02 보조 | Domain |
| 누락 두 수 | BR-06 | FR-03 | AC-FR03-1 | TD-02 계열 | Domain |
| 합 34 | BR-07 | FR-04 | AC-FR04-1~3 | TD-03 | Domain |
| 1~16 순열 | BR-08 | FR-04 | AC-FR04-3 | D-T15 대응 | Domain |
| 성공 좌표 범위 | BR-09 | FR-05 | AC-FR05-1,2 | TP-01,02 | Domain, Boundary |
| n1,n2 위치 의미 | BR-10 | FR-05 | AC-FR05-1,2 | TP-01,02 | Domain |
| 시도 1 성공 순서 | BR-11 | FR-05 | AC-FR05-1,5 | TP-01 | Domain |
| 시도 2 성공 순서 | BR-12 | FR-05 | AC-FR05-2 | TP-02 | Domain |
| 모두 실패 | DEC-01, BR-ERR-05 | FR-05 | AC-FR05-3 | TP-03 | Domain → Boundary |
| 모두 성공 | DEC-02, BR-ERR-06 | FR-05 | AC-FR05-4 | TP-04 | Domain → Boundary |
| 고정 오류 문구 | BR-ERR-01~07 | FR-01, FR-05 | 각 AC | TP-05~08, TP-03~04 | Boundary |
| 결정론 | NFR-03 | FR-02~05 | P-05 | 반복 실행 테스트 | System |
| 커버리지 목표 | NFR-01,02 | 전 FR | 리포트 수치 | CI 잡 | Quality |

---

## 문서 이력

| 항목 | 내용 |
|------|------|
| 위치 | `docs/PRD_MagicSquare_4x4_TDD.md` |
| 버전 | 1.0 (2026-04-28) |
| 제외 | 구현 코드, UI/DB 구현, N×N 일반화 요구 |

---

**문서 끝**
