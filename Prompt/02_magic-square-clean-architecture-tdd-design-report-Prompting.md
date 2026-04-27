# Magic Square TDD design and architecture
_Exported on 4/27/2026 at 16:50:21 GMT+9 from Cursor (3.2.11)_

---

**User**

당신은 Dual-Track UI + Logic TDD 및 Clean Architecture 설계 전문가입니다.

프로젝트: Magic Square (4x4) — TDD 연습용
목적: 알고리즘 난이도보다 “레이어 분리 + 계약 기반 테스트 + 리팩토링” 훈련
제약:
- 구현 코드는 작성하지 마십시오. (설계/계약/테스트/통합 계획만)
- UI는 실제 화면이 아니라 “입력/출력 경계(Boundary)”로 정의
- Data Layer는 DB가 아니라 “저장/로드 인터페이스(메모리/파일 교체 가능)” 수준만
- 입력/출력은 명확히 고정

입력 계약:
- 4x4 int[][] (0은 빈칸)
- 빈칸은 정확히 2개
- 값 범위: 0 또는 1~16
- 0 제외 중복 금지
출력 계약:
- int[6]
- 좌표는 1-index
- 반환 형식: [r1,c1,n1,r2,c2,n2]
- n1,n2는 두 누락 숫자이며, (작은수→첫빈칸, 큰수→둘째빈칸) 조합이 마방진이면 그 순서로, 아니면 반대로

------------------------------------------------------------
출력 형식 (반드시 이 구조로)
------------------------------------------------------------

# 1) Logic Layer (Domain Layer) 설계
## 1.1 도메인 개념
- Entities / Value Objects / Domain Services 목록과 책임(SRP)
## 1.2 도메인 불변조건(Invariants)
- 행/열/대각선 합 일치, Magic Constant 등
## 1.3 핵심 유스케이스(도메인 관점)
- 빈칸 찾기, 누락 숫자 찾기, 마방진 판정, 두 조합 시도
## 1.4 Domain API(내부 계약)
- 메서드 시그니처 수준(코드 X) + 입력/출력/실패조건
## 1.5 Domain 단위 테스트 설계(RED 우선)
- 테스트 케이스 목록(정상/비정상/엣지)
- 각 테스트가 보호하는 invariant 명시

# 2) Screen Layer (UI Layer) 설계 (Boundary Layer)
## 2.1 사용자/호출자 관점 시나리오
- “행렬 입력 → 검증 → 결과 출력” 흐름
## 2.2 UI 계약(외부 계약)
- Input schema / Output schema / Error schema
## 2.3 UI 레벨 테스트(Contract-first, RED 우선)
- 잘못된 크기, 빈칸 개수 오류, 값 범위 오류, 중복 오류, 반환 포맷 검증
- Domain은 Mock으로 가정
## 2.4 UX/출력 규칙
- 에러 메시지 표준(정확한 문구 규칙까지)

# 3) Data Layer 설계 (Data Layer)
## 3.1 목적 정의
- “저장/로드”의 필요성과 범위(학습용)
## 3.2 인터페이스 계약
- 예: MatrixRepository.save/load (메서드 수준, 코드 X)
- 저장 대상: 입력 행렬, 실행 결과(선택)
## 3.3 구현 옵션 비교(메모리/파일)
- 옵션 A: InMemory / 옵션 B: File(JSON/CSV)
- 추천안 1개 선택 + 이유
## 3.4 Data 레이어 테스트
- 저장/로드 정합성, 예외(파일 없음/형식 오류), 불변조건(4x4 유지)

# 4) Integration & Verification (통합 및 검증)
## 4.1 통합 경로 정의
- UI → Application(선택) → Domain → Data 흐름(의존성 방향 포함)
## 4.2 통합 테스트 시나리오
- 정상 시나리오 2개 이상
- 실패 시나리오 3개 이상(입력 오류, 도메인 실패, 데이터 실패)
## 4.3 회귀 보호 규칙
- 기존 테스트 유지 정책
- 변경 금지 규칙(계약/출력 포맷)
## 4.4 커버리지 목표
- Domain Logic 95%+
- UI Boundary 85%+
- Data 80%+
## 4.5 Traceability Matrix (필수)
- Concept(Invariant) → Rule → Use Case → Contract → Test → Component

------------------------------------------------------------
추가 조건
------------------------------------------------------------
- 모호한 표현 금지(“적절히/충분히” 금지)
- 모든 규칙은 검증 가능해야 함(테스트로 확인 가능)
- 구현 코드 작성 금지
- 표/체크리스트를 적극 사용


---

**Cursor**

요청하신 구조로 설계·계약·테스트·통합 계획만 정리합니다. (구현 코드 없음)

---

# 1) Logic Layer (Domain Layer) 설계

## 1.1 도메인 개념

| 구분 | 이름 | 책임 (SRP) |
|------|------|------------|
| Entity | `PartialMagicSquare` (또는 `MagicSquareGrid`) | 4×4 셀 상태 보유; 빈칸 좌표·배치 후 완전 그리드 표현 단일 소스 |
| Value Object | `CellCoordinate` | 행·열 (도메인 내부는 1-index 고정 여부를 한 곳에서만 정의; 외부 계약과 일치시키면 경계에서만 변환) |
| Value Object | `CellValue` | 허용 값: 0(빈칸) 또는 1~16; 동등성·범위 검증 의미만 담당 |
| Value Object | `MagicConstant` | 4×4 고정 상수 34 단일 정의 |
| Value Object | `PlacementOrder` | (n_first_empty, n_second_empty) 순서 후보 2가지 중 도메인 규칙으로 선택된 하나 |
| Domain Service | `EmptyCellLocator` | 그리드에서 값 0인 셀을 정확히 2개 찾기; 개수 불일치 시 실패 |
| Domain Service | `MissingNumberResolver` | 등장한 1~16 집합과 비교해 누락된 정수 2개 결정 |
| Domain Service | `MagicSquareCompletenessChecker` | 두 빈칸에 후보 배치 후 행·열·두 대각선 합이 `MagicConstant`와 일치하는지 판정 |
| Domain Service | `SolutionOrderingPolicy` | 출력 규칙: (작은수→첫 빈칸, 큰수→둘째 빈칸)이 마방진이면 그 순서, 아니면 반대로 `(n1,n2)` 확정 |

**엔티티 vs VO 경계:** 그리드는 시간에 따라 “부분 → 완성”으로 바뀌므로 Entity; 좌표·단일 값·상수는 VO.

---

## 1.2 도메인 불변조건 (Invariants)

| ID | Invariant | 검증 시점 | 검증 가능 규칙 |
|----|-----------|-----------|----------------|
| INV-01 | 그리드 크기는 4×4 | 입력 수용 직후 | `rows == 4 && each row length == 4` |
| INV-02 | 빈칸(0) 개수는 정확히 2 | 전처리 후 | `count(value==0) == 2` |
| INV-03 | 0 제외 값은 1~16 | 전처리 후 | `∀v≠0: 1≤v≤16` |
| INV-04 | 0 제외 중복 없음 | 전처리 후 | `|distinct(nonZero)| == count(nonZero)` |
| INV-05 | 완성 그리드에서 사용 숫자는 {1..16} 전부 1회 | 해 탐색 성공 시 | multiset equals {1..16} |
| INV-06 | 모든 행 합 = 34 | 완성 판정 시 | `∀row: sum(row)==34` |
| INV-07 | 모든 열 합 = 34 | 완성 판정 시 | `∀col: sum(col)==34` |
| INV-08 | 주대각선 합 = 34 | 완성 판정 시 | `sum(diag1)==34` |
| INV-09 | 부대각선 합 = 34 | 완성 판정 시 | `sum(diag2)==34` |
| INV-10 | 빈칸 순서 “첫 빈칸/둘째 빈칸”는 결정적 규칙으로 고정 | 해 출력 시 | 행 우선 스캔: `(r asc, c asc)`에서 첫 0, 그다음 0 |

**Magic Constant:** `M = n(n²+1)/2` with n=4 → **34** (INV-06~09와 동일 출처).

---

## 1.3 핵심 유스케이스 (도메인 관점)

| UC-ID | 이름 | 전제 | 결과 / 실패 |
|-------|------|------|----------------|
| UC-D01 | 빈칸 찾기 | INV-01~04 만족 가정 | 두 좌표 `(r1,c1),(r2,c2)` 결정적 반환; 빈칸 수 ≠2면 실패 |
| UC-D02 | 누락 숫자 찾기 | UC-D01 성공 | `{a,b} = {1..16} \ set(배치된 수)` |
| UC-D03 | 마방진 판정 | 완전 4×4 (0 없음) | INV-05~09 동시 만족 시 true |
| UC-D04 | 두 조합 시도 | UC-D01~02 성공 | 배치 A: 작은수→첫 빈칸, 큰수→둘째 빈칸; 배치 B: 반대; UC-D03로 각각 판정 |
| UC-D05 | 출력 순서 확정 | UC-D04 | A가 true면 `(n1,n2)=(min,max)` 위치 고정; B만 true면 순서 반대; 둘 다 true/둘 다 false면 별도 실패 정책 필요 (아래 실패조건) |

**실패 정책 (도메인 명시):**

- 둘 다 마방진이면: 문제 정의상 “유일한 해법” 학습 범위라면 **실패(모호)**로 처리하거나, **결정적 타이브레이크**를 도메인 규칙에 한 줄로 고정해야 검증 가능함.  
  **권장 (검증 가능):** “둘 다 성공이면 실패” 또는 “첫 번째 성공한 순서 채택” 중 하나만 택일. 아래 계약에서는 **둘 다 true → `AMBIGUOUS_SOLUTION`** / **둘 다 false → `NO_SOLUTION`** 으로 고정.

---

## 1.4 Domain API (내부 계약)

코드 없이 시그니처 수준만 기술.

| API-ID | 연산 | 입력 | 출력 | 실패 조건 |
|--------|------|------|------|-----------|
| DA-01 | `parseOrValidateGrid` | `int[][]` 원시 | `PartialMagicSquare` 또는 검증 리포트 | INV-01~04 위반 |
| DA-02 | `locateEmptyCells` | `PartialMagicSquare` | 두 `CellCoordinate` (INV-10 순서) | 빈칸 수 ≠2 |
| DA-03 | `computeMissingNumbers` | `PartialMagicSquare` | 두 정수 `(minMissing, maxMissing)` 집합 표현 | 누락 개수 ≠2 |
| DA-04 | `isCompletedMagicSquare` | 완전 그리드 | boolean | 입력에 0 존재 시 실패 또는 명시적 false 정책 택일 |
| DA-05 | `resolvePlacementOrder` | 부분 그리드 + 빈칸 2 + 누락 2 | `(n1,n2)` 및 각 셀에 대한 값 매핑 | UC-D05: `NO_SOLUTION` / `AMBIGUOUS_SOLUTION` |
| DA-06 | `toSolutionVector` (선택: 경계 직전) | 내부 표현 | `int[6]` 1-index 좌표 + `n1,n2` | 좌표·순서 불변 위반 시 실패 |

**실패 타입 (도메인 에러 코드 목록):**

- `INVALID_GRID_SIZE`
- `INVALID_EMPTY_CELL_COUNT`
- `VALUE_OUT_OF_RANGE`
- `DUPLICATE_NONZERO_VALUE`
- `NO_SOLUTION`
- `AMBIGUOUS_SOLUTION` (둘 다 true 채택 시)

---

## 1.5 Domain 단위 테스트 설계 (RED 우선)

### 테스트 케이스 목록

| TC-ID | 유형 | 설명 | 기대 |
|-------|------|------|------|
| D-T01 | 정상 | 알려진 완성 4×4 마방진에서 임의 두 칸을 0으로 바꾼 뒤, 누락 숫자·위치가 복원되는 케이스 | `resolvePlacementOrder` 성공, `isCompletedMagicSquare` true |
| D-T02 | 정상 | 다른 완성 패턴(동일 INV)으로 동일 절차 | 동일 |
| D-T03 | 정상 | 빈칸 스캔 순서: (1,1)과 (4,4) 등 극단 위치 | 첫/둘째 빈칸이 INV-10과 일치 |
| D-T04 | 정상 | 작은수→첫 빈칸 조합만 성공하는 인스턴스 | `n1<n2`가 아닌 출력 규칙까지 포함해 기대 벡터 고정 |
| D-T05 | 정상 | 큰수→첫 빈칸 조합만 성공 | `n1,n2` 순서가 규칙에 따라 뒤바뀐 기대 벡터 |
| D-T06 | 비정상 | 3×3 또는 4×5 | `INVALID_GRID_SIZE` |
| D-T07 | 비정상 | 빈칸 0개 | `INVALID_EMPTY_CELL_COUNT` |
| D-T08 | 비정상 | 빈칸 3개 | 동일 |
| D-T09 | 비정상 | 값 17 | `VALUE_OUT_OF_RANGE` |
| D-T10 | 비정상 | 값 -1 | 동일 |
| D-T11 | 비정상 | 중복 (예: 두 칸에 5) | `DUPLICATE_NONZERO_VALUE` |
| D-T12 | 엣지 | 14개 고정 + 빈칸 2개인데 어떤 배치도 마방진 불가능한 그리드 | `NO_SOLUTION` |
| D-T13 | 엣지 | (선택) 둘 다 true가 되도록 인위적 그리드가 불가능하면 스펙으로 `AMBIGUOUS` 제거; 가능하면 | `AMBIGUOUS_SOLUTION` |
| D-T14 | 엣지 | `isCompletedMagicSquare`: 행만 맞고 대각선 틀린 그리드 | false |
| D-T15 | 엣지 | 합 34이지만 1~16 multiset 위반 | false (INV-05) |

### Invariant 보호 매핑 (요약)

| TC-ID | 보호하는 Invariant |
|-------|---------------------|
| D-T01~05 | INV-05~10 + 출력 순서 규칙 |
| D-T06 | INV-01 |
| D-T07~08 | INV-02 |
| D-T09~10 | INV-03 |
| D-T11 | INV-04 |
| D-T12~13 | UC-D05 정책 |
| D-T14~15 | INV-06~09, INV-05 |

---

# 2) Screen Layer (UI Layer) 설계 (Boundary Layer)

## 2.1 사용자/호출자 관점 시나리오

| 단계 | 시나리오 |
|------|----------|
| S1 | 호출자가 4×4 정수 행렬을 Boundary에 제출 |
| S2 | Boundary가 스키마·불변 전처리 검증 수행 |
| S3 | 성공 시 Domain 포트에 위임; 실패 시 표준 에러 스키마 반환 (Domain 미호출) |
| S4 | Domain 성공 시 `int[6]`을 Output schema로 반환 |
| S5 | Domain 실패 시 에러 코드를 Boundary 에러 스키마로 매핑 (문구 고정) |

---

## 2.2 UI 계약 (외부 계약)

### Input schema

| 필드 | 타입 | 규칙 |
|------|------|------|
| `grid` | `int[][]` | 길이 4; 각 행 길이 4 |
| 셀 값 | `int` | 0 또는 1~16 |
| 빈칸 | | `grid` 전체에서 값 0인 셀 정확히 2개 |
| 중복 | | 0을 제외한 값은 서로 다름 |

### Output schema (성공)

| 필드 | 타입 | 규칙 |
|------|------|------|
| `result` | `int[6]` | `[r1,c1,n1,r2,c2,n2]` |
| 좌표 | | `r1,c1,r2,c2` ∈ {1,2,3,4} (1-index) |
| 숫자 | | `n1,n2` ∈ {1..16}, 문제 정의의 순서 규칙 준수 |

### Error schema

| 필드 | 타입 | 규칙 |
|------|------|------|
| `errorCode` | enum 문자열 | 아래 목록과 정확히 동일 |
| `message` | string | 아래 **표준 문구**와 바이트 단위 동일 (학습용 고정) |

**errorCode 목록:** `INVALID_GRID_SIZE`, `INVALID_EMPTY_CELL_COUNT`, `VALUE_OUT_OF_RANGE`, `DUPLICATE_NONZERO_VALUE`, `NO_SOLUTION`, `AMBIGUOUS_SOLUTION`, `DOMAIN_UNEXPECTED` (매핑 누락 방지용, 테스트에서만 사용 여부 택일)

---

## 2.3 UI 레벨 테스트 (Contract-first, RED 우선)

**전제:** Domain 포트는 Mock. Mock은 “성공 시 고정 `int[6]` 반환”, “호출 시 인자 캡처”, “에러 코드 던지기”만 수행.

| TC-ID | 설명 | Mock 기대 | 검증 포인트 |
|-------|------|-------------|-------------|
| U-T01 | 4×4 유효 입력 | 성공 반환 | Domain 호출 1회, 반환 배열 참조 동일 또는 값 동등 |
| U-T02 | 행 개수 3 | Mock 미호출 | `errorCode=INVALID_GRID_SIZE`, 표준 message |
| U-T03 | 행 길이 불균일 (예: 첫 행 3) | Mock 미호출 | 동일 |
| U-T04 | 빈칸 1개 | Mock 미호출 | `INVALID_EMPTY_CELL_COUNT` |
| U-T05 | 빈칸 3개 | Mock 미호출 | 동일 |
| U-T06 | 셀 값 17 | Mock 미호출 | `VALUE_OUT_OF_RANGE` |
| U-T06b | 셀 값 -5 | Mock 미호출 | 동일 |
| U-T07 | 중복 값 | Mock 미호출 | `DUPLICATE_NONZERO_VALUE` |
| U-T08 | 유효 입력인데 Domain이 `NO_SOLUTION` | Mock이 해당 에러 | Boundary가 동일 코드·문구 전달 |
| U-T09 | Domain이 `AMBIGUOUS_SOLUTION` | Mock | 동일 |
| U-T10 | 출력 길이 6, 좌표 범위 1~4 | Mock이 경계값 벡터 | Boundary 검증(선택): 추가 방어 레이어 |

**Invariant 보호:** 입력 계약 전부는 UI 테스트에서만으로도 재현 가능해야 함 (Domain 없이 RED).

---

## 2.4 UX/출력 규칙 — 에러 메시지 표준 (정확한 문구)

**규칙:** 성공 응답에는 `message` 없음. 실패 시에만 아래 문자열 **전체 일치** (줄바꿈 없음, 끝 공백 없음).

| errorCode | message (고정) |
|-----------|----------------|
| `INVALID_GRID_SIZE` | `Grid must be 4x4.` |
| `INVALID_EMPTY_CELL_COUNT` | `Exactly two cells must be empty (value 0).` |
| `VALUE_OUT_OF_RANGE` | `Each cell must be 0 or an integer from 1 to 16.` |
| `DUPLICATE_NONZERO_VALUE` | `Non-zero values must not repeat.` |
| `NO_SOLUTION` | `No valid magic-square completion exists for this grid.` |
| `AMBIGUOUS_SOLUTION` | `Multiple valid orderings satisfy the rule; input is rejected.` |
| `DOMAIN_UNEXPECTED` | `An unexpected domain error occurred.` |

**체크리스트 (리뷰용):**

- [ ] 모든 UI 실패 테스트가 위 표의 `message`를 `assertEquals`로 검증
- [ ] `errorCode`는 대소문자·스펠링 고정
- [ ] 성공 응답 JSON/XML 등 포맷을 쓰면 스키마에 `result`만 포함하는지 명시

---

# 3) Data Layer 설계 (Persistence Boundary)

## 3.1 목적 정의

| 항목 | 내용 |
|------|------|
| 목적 | 연습: Application/Domain과 저장 매체 분리; “같은 유스케이스, 다른 저장소” 교체 |
| 범위 | (A) 마지막 입력 그리드 저장·로드 (B) 마지막 성공 `int[6]` 저장·로드 (선택, 플래그로 켜기) |
| 비범위 | DB 스키마, 마이그레이션, 동시성, 보안 |

---

## 3.2 인터페이스 계약

| 메서드 (개념) | 입력 | 출력 | 실패 |
|---------------|------|------|------|
| `MatrixRepository.saveInput(grid: int[][])` | 입력 계약 만족 그리드 | void 또는 저장 키 | 직렬화 불가 시 `STORAGE_WRITE_FAILED` |
| `MatrixRepository.loadInput()` | 없음 | `int[][]` 또는 empty | 없으면 `NOT_FOUND` (학습용: 빈 optional 정책 택일) |
| `MatrixRepository.saveResult(vector: int[6])` | 성공 결과만 | void | 동상 |
| `MatrixRepository.loadResult()` | 없음 | `int[6]` optional | `NOT_FOUND` |

**저장 대상 불변:** 로드된 입력은 다시 검증하거나, 저장 시점에 “검증 통과된 것만 저장” 정책을 문서에 고정.

---

## 3.3 구현 옵션 비교

| 기준 | 옵션 A: InMemory | 옵션 B: File (JSON 권장) |
|------|------------------|---------------------------|
| 프로세스 재시작 후 유지 | 없음 | 있음 |
| 테스트 난이도 | 낮음 (단위·통합 단순) | 중간 (임시 디렉터리) |
| 실패 모드 | 거의 없음 | 파일 없음, JSON 깨짐, 타입 불일치 |
| 학습 목표 달성 | 레이어 분리 | 분리 + I/O 예외 + 직렬화 계약 |

**추천:** **옵션 B (JSON 파일)** — “메모리/파일 교체 가능” 제약을 충족하면서, Data 레이어 테스트(파일 없음·형식 오류)를 실제로 작성할 수 있음. InMemory는 **테스트용 Fake**로 병행 유지하는 것을 권장 (빠른 단위 테스트).

---

## 3.4 Data 레이어 테스트

| TC-ID | 내용 | 기대 |
|-------|------|------|
| DT-01 | saveInput 후 loadInput | 배열 깊은 동등, 4×4 |
| DT-02 | saveResult 후 loadResult | `int[6]` 동등 |
| DT-03 | loadInput 파일 없음 | `NOT_FOUND` (또는 empty 정책 일치) |
| DT-04 | 손상 JSON | `STORAGE_CORRUPT` |
| DT-05 | JSON에 3×3 데이터 | `STORAGE_SCHEMA_INVALID` + 4×4 불변 위반 |
| DT-06 | 중복 값이 포함된 저장본 로드 후 검증 레이어에서 거부 | 저장은 허용할지 정책 택일; **권장:** 저장 전 검증으로 `INVALID` 저장 방지 |

**불변조건 체크리스트:**

- [ ] 로드 직후 행/열 길이 4
- [ ] 선택: 로드 후 UI와 동일 전처리 호출 시 동일 에러

---

# 4) Integration & Verification (통합 및 검증)

## 4.1 통합 경로 정의

```text
Caller
  → UI Boundary (입력 검증, 출력/에러 매핑)
      → Application Service (선택: 유스케이스 오케스트레이션, 트랜잭션 없음)
          → Domain (resolve)
      ←
  ↔ Data Boundary (선택: save/load; Application 전후)
```

**의존성 방향:**

- UI → Application(선택) → Domain 포트(인터페이스)
- Data → 인터페이스만 노출; Domain은 Data를 **참조하지 않음**
- Application이 `MatrixRepository`를 알면: Infrastructure 구현체 주입

---

## 4.2 통합 테스트 시나리오

### 정상 (2개 이상)

| IT-ID | 흐름 |
|-------|------|
| IT-01 | 유효 그리드 → Domain 실제 구현 → `int[6]`이 알려진 기대와 일치 |
| IT-02 | IT-01 후 `saveInput`/`saveResult` → 새 프로세스/새 Repository 인스턴스로 load → 재실행 결과 동일 |

### 실패 (3개 이상)

| IT-ID | 흐름 |
|-------|------|
| IT-E01 | 변형된 크기 그리드 → UI에서 거부, Domain·Data 미호출 |
| IT-E02 | 유효 형식이지만 불가능 퍼즐 → `NO_SOLUTION` + 고정 문구 |
| IT-E03 | 손상된 저장 파일 로드 시도 → Data `STORAGE_CORRUPT`, 상위에서 매핑 규칙 고정 |

---

## 4.3 회귀 보호 규칙

| 규칙 | 설명 |
|------|------|
| R-01 | `int[6]` 길이·1-index 좌표·`n1,n2` 순서 규칙에 대한 골든 테스트 스위트는 변경 시 PR에 “계약 변경” 라벨 필수 |
| R-02 | 에러 `message` 문자열 변경은 **의도된 계약 변경**으로만; CI에서 스냅샷 또는 명시 assert |
| R-03 | Domain 공개 포트 시그니처 변경 시 Mock 기반 UI 테스트 컴파일 깨짐으로 조기 발견 |
| R-04 | 기존 테스트 삭제 금지; 대체 시 동일 TC-ID 범위 커버 증명 |

---

## 4.4 커버리지 목표

| 레이어 | 목표 |
|--------|------|
| Domain | 라인/브랜치 95%+ (판정 분기·실패 경로 포함) |
| UI Boundary | 85%+ (모든 errorCode 경로 + 성공 1회) |
| Data | 80%+ (정상·파일 없음·손상·스키마 오류) |

---

## 4.5 Traceability Matrix (필수)

| Concept (Invariant / Rule) | Rule ID | Use Case | Contract (UI/Domain/Data) | Test (ID) | Component |
|-----------------------------|---------|----------|---------------------------|-----------|-----------|
| 4×4 크기 | INV-01 | S2 전처리 | UI Input + DA-01 | U-T02~03, D-T06 | UI, Domain |
| 빈칸 2개 | INV-02 | UC-D01 | DA-02, UI Input | U-T04~05, D-T07~08 | UI, Domain |
| 값 범위 0 또는 1~16 | INV-03 | S2 | UI Input, DA-01 | U-T06~06b, D-T09~10 | UI, Domain |
| 0 제외 중복 금지 | INV-04 | S2 | UI Input, DA-01 | U-T07, D-T11 | UI, Domain |
| 1~16 완전 사용 | INV-05 | UC-D03 | DA-04 | D-T15 | Domain |
| 행/열/대각 합 34 | INV-06~09 | UC-D03~04 | DA-04 | D-T01~02, D-T14 | Domain |
| 빈칸 스캔 순서 | INV-10 | UC-D01, UC-D05 | DA-02, DA-05 | D-T03 | Domain |
| 출력 순서 (작/큰 vs 빈칸) | Rule-OUT | UC-D05 | Output schema, DA-05 | D-T04~05, IT-01 | Domain, Integration |
| 입력 검증 우선 | Rule-LAYER | S2~S3 | UI contract | U-T01~10 | UI |
| 저장 정합성 | INV-STORE | IT-02 | `save/load`* | DT-01~02, IT-02 | Data |
| 손상/스키마 | Rule-IO | — | Data errors | DT-04~05, IT-E03 | Data |
| 고정 에러 문구 | Rule-MSG | S5 | Error schema | U-T02~09, IT-E01~02 | UI |

\*Data 계약은 섹션 3.2 명칭과 대응.

---

## 부록: Dual-Track TDD 체크리스트

| 트랙 | 산출물 | 완료 기준 |
|------|--------|-----------|
| Logic | Domain 테스트 목록 1.5 + 에러 타입 | Domain RED 전부 작성 후 최소 1 GREEN 루프 |
| UI | Boundary 테스트 2.3 + 메시지 표 2.4 | Mock으로 UI RED → Adapter만 연결 |
| Data | 3.4 TC + Fake/JSON 구현 순서 문서화 | File I/O는 테스트 임시 폴더 고정 |

---

이 문서만으로 레이어별 테스트를 RED부터 추가하고, 계약(입력·`int[6]`·에러 문자열)을 변경하지 않는 한 회귀를 유지할 수 있도록 맞춰 두었습니다. `AMBIGUOUS_SOLUTION`을 실제 데이터에서 제거하고 싶다면, 도메인에서 “둘 다 true 불가”를 증명하거나 UC-D05 정책을 “첫 성공 채택”으로 바꾸고 표·테스트·Traceability를 한 번에 갱신하면 됩니다.

---

**User**

Reporter 폴더에  지금 작업한 내용을 보고서로 내보내줘.

---

**Cursor**

Reporter 폴더 구조와 기존 보고서 형식을 확인한 뒤 동일한 톤으로 보고서 파일을 생성합니다.



기존 `01_` 보고서 다음 번호로 `02_` 설계·계약 보고서를 작성합니다.



다음 파일로 저장했습니다.

**경로:** `c:\DEV\MagicSquare_XXX\Reporter\02_magic-square-clean-architecture-tdd-design-report.md`

**구성:** 이전 대화에서 정리한 Logic / UI(Boundary) / Data / 통합·Traceability·Dual-Track 체크리스트를 그대로 옮겼고, 상단에 작성 목적·범위·입출력 계약·작성일(2026-04-27) 메타데이터를 두었습니다. 기존 `01_magic-square-problem-definition-report.md`(문제 인식·정의)와 짝이 되도록 번호를 `02_`로 맞춰 두었습니다.

