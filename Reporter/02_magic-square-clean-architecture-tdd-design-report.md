# 4×4 마방진 — Clean Architecture · Dual-Track TDD · Boundary 설계 보고서

**작성 목적:** 알고리즘 구현이 아니라 레이어 분리, 계약 기반 테스트, 리팩토링 훈련을 위한 Logic / UI(Boundary) / Data 설계·계약·테스트·통합 계획을 한 문서로 보존한다.  
**범위:** 도메인 설계, UI 경계 계약, Data 저장·로드 계약, 단위·통합 테스트 목록, Traceability Matrix. **구현 코드는 포함하지 않는다.**  
**작성일:** 2026-04-27  

**입력 계약 (고정):** `4x4 int[][]`, `0`은 빈칸, 빈칸 정확히 2개, 값은 `0` 또는 `1~16`, `0` 제외 중복 금지.  
**출력 계약 (고정):** `int[6]` — `[r1,c1,n1,r2,c2,n2]`, 좌표 1-index, `n1,n2`는 누락 숫자; (작은수→첫 빈칸, 큰수→둘째 빈칸)이 마방진이면 그 순서, 아니면 반대 순서.

---

## 1) Logic Layer (Domain Layer) 설계

### 1.1 도메인 개념

| 구분 | 이름 | 책임 (SRP) |
|------|------|------------|
| Entity | `PartialMagicSquare` (또는 `MagicSquareGrid`) | 4×4 셀 상태 보유; 빈칸 좌표·배치 후 완전 그리드 표현 단일 소스 |
| Value Object | `CellCoordinate` | 행·열; 도메인 내부 인덱스 규칙을 한 곳에서만 정의 (외부 1-index와 맞출 경우 경계에서만 변환) |
| Value Object | `CellValue` | 허용 값: 0(빈칸) 또는 1~16; 동등성·범위 검증 의미만 담당 |
| Value Object | `MagicConstant` | 4×4 고정 상수 34 단일 정의 |
| Value Object | `PlacementOrder` | (n_first_empty, n_second_empty) 순서 후보 중 규칙으로 선택된 하나 |
| Domain Service | `EmptyCellLocator` | 값 0인 셀을 정확히 2개 찾기; 개수 불일치 시 실패 |
| Domain Service | `MissingNumberResolver` | 등장한 1~16 집합과 비교해 누락된 정수 2개 결정 |
| Domain Service | `MagicSquareCompletenessChecker` | 두 빈칸에 후보 배치 후 행·열·두 대각선 합이 `MagicConstant`와 일치하는지 판정 |
| Domain Service | `SolutionOrderingPolicy` | 출력 규칙: (작은수→첫 빈칸, 큰수→둘째 빈칸)이 마방진이면 그 순서, 아니면 반대로 `(n1,n2)` 확정 |

**엔티티 vs VO 경계:** 그리드는 시간에 따라 부분→완성으로 바뀌므로 Entity; 좌표·단일 값·상수는 VO.

### 1.2 도메인 불변조건 (Invariants)

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
| INV-10 | 빈칸 순서 “첫 빈칸/둘째 빈칸”은 결정적 규칙으로 고정 | 해 출력 시 | 행 우선 스캔: `(r asc, c asc)`에서 첫 0, 그다음 0 |

**Magic Constant:** `M = n(n²+1)/2`, n=4 → **34** (INV-06~09와 동일 출처).

### 1.3 핵심 유스케이스 (도메인 관점)

| UC-ID | 이름 | 전제 | 결과 / 실패 |
|-------|------|------|----------------|
| UC-D01 | 빈칸 찾기 | INV-01~04 만족 가정 | 두 좌표 `(r1,c1),(r2,c2)` 결정적 반환; 빈칸 수 ≠2면 실패 |
| UC-D02 | 누락 숫자 찾기 | UC-D01 성공 | `{a,b} = {1..16} \ set(배치된 수)` |
| UC-D03 | 마방진 판정 | 완전 4×4 (0 없음) | INV-05~09 동시 만족 시 true |
| UC-D04 | 두 조합 시도 | UC-D01~02 성공 | 배치 A: 작은수→첫 빈칸, 큰수→둘째 빈칸; 배치 B: 반대; UC-D03로 각각 판정 |
| UC-D05 | 출력 순서 확정 | UC-D04 | A가 true면 `(n1,n2)=(min,max)` 위치 고정; B만 true면 순서 반대; 둘 다 true면 `AMBIGUOUS_SOLUTION`, 둘 다 false면 `NO_SOLUTION` (고정 정책) |

### 1.4 Domain API (내부 계약)

구현 코드 없이 연산·입출력·실패만 기술한다.

| API-ID | 연산 | 입력 | 출력 | 실패 조건 |
|--------|------|------|------|-----------|
| DA-01 | `parseOrValidateGrid` | `int[][]` 원시 | `PartialMagicSquare` 또는 검증 리포트 | INV-01~04 위반 |
| DA-02 | `locateEmptyCells` | `PartialMagicSquare` | 두 `CellCoordinate` (INV-10 순서) | 빈칸 수 ≠2 |
| DA-03 | `computeMissingNumbers` | `PartialMagicSquare` | 누락 두 정수 (집합) | 누락 개수 ≠2 |
| DA-04 | `isCompletedMagicSquare` | 완전 그리드 | boolean | 입력에 0 존재 시 실패 또는 명시적 false 정책 택일 |
| DA-05 | `resolvePlacementOrder` | 부분 그리드 + 빈칸 2 + 누락 2 | `(n1,n2)` 및 셀별 값 매핑 | `NO_SOLUTION` / `AMBIGUOUS_SOLUTION` |
| DA-06 | `toSolutionVector` (선택, 경계 직전) | 내부 표현 | `int[6]` 1-index | 좌표·순서 불변 위반 시 실패 |

**도메인 에러 코드:** `INVALID_GRID_SIZE`, `INVALID_EMPTY_CELL_COUNT`, `VALUE_OUT_OF_RANGE`, `DUPLICATE_NONZERO_VALUE`, `NO_SOLUTION`, `AMBIGUOUS_SOLUTION`.

### 1.5 Domain 단위 테스트 설계 (RED 우선)

#### 테스트 케이스 목록

| TC-ID | 유형 | 설명 | 기대 |
|-------|------|------|------|
| D-T01 | 정상 | 알려진 완성 4×4 마방진에서 임의 두 칸을 0으로 바꾼 뒤 복원 | `resolvePlacementOrder` 성공, `isCompletedMagicSquare` true |
| D-T02 | 정상 | 다른 완성 패턴으로 동일 절차 | 동일 |
| D-T03 | 정상 | 빈칸 (1,1)과 (4,4) 등 극단 위치 | 첫/둘째 빈칸이 INV-10과 일치 |
| D-T04 | 정상 | 작은수→첫 빈칸 조합만 성공 | 출력 규칙 포함 기대 벡터 고정 |
| D-T05 | 정상 | 큰수→첫 빈칸 조합만 성공 | `n1,n2` 순서 반대 기대 벡터 |
| D-T06 | 비정상 | 3×3 또는 4×5 | `INVALID_GRID_SIZE` |
| D-T07 | 비정상 | 빈칸 0개 | `INVALID_EMPTY_CELL_COUNT` |
| D-T08 | 비정상 | 빈칸 3개 | 동일 |
| D-T09 | 비정상 | 값 17 | `VALUE_OUT_OF_RANGE` |
| D-T10 | 비정상 | 값 -1 | 동일 |
| D-T11 | 비정상 | 중복 (예: 두 칸에 5) | `DUPLICATE_NONZERO_VALUE` |
| D-T12 | 엣지 | 완성 불가능 그리드 | `NO_SOLUTION` |
| D-T13 | 엣지 | 둘 다 true 가능 시 | `AMBIGUOUS_SOLUTION` |
| D-T14 | 엣지 | 행만 맞고 대각선 틀린 완전 그리드 | false |
| D-T15 | 엣지 | 합 34이지만 1~16 multiset 위반 | false (INV-05) |

#### Invariant 보호 매핑

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

## 2) Screen Layer (UI Layer) 설계 (Boundary Layer)

### 2.1 사용자/호출자 관점 시나리오

| 단계 | 시나리오 |
|------|----------|
| S1 | 호출자가 4×4 정수 행렬을 Boundary에 제출 |
| S2 | Boundary가 스키마·불변 전처리 검증 수행 |
| S3 | 성공 시 Domain 포트에 위임; 실패 시 표준 에러 스키마 반환 (Domain 미호출) |
| S4 | Domain 성공 시 `int[6]`을 Output schema로 반환 |
| S5 | Domain 실패 시 에러 코드를 Boundary 에러 스키마로 매핑 (문구 고정) |

### 2.2 UI 계약 (외부 계약)

**Input schema**

| 필드 | 타입 | 규칙 |
|------|------|------|
| `grid` | `int[][]` | 길이 4; 각 행 길이 4 |
| 셀 값 | `int` | 0 또는 1~16 |
| 빈칸 | | 값 0인 셀 정확히 2개 |
| 중복 | | 0을 제외한 값은 서로 다름 |

**Output schema (성공)**

| 필드 | 타입 | 규칙 |
|------|------|------|
| `result` | `int[6]` | `[r1,c1,n1,r2,c2,n2]` |
| 좌표 | | `r1,c1,r2,c2` ∈ {1,2,3,4} (1-index) |
| 숫자 | | `n1,n2` ∈ {1..16}, 문제 정의 순서 규칙 준수 |

**Error schema**

| 필드 | 타입 | 규칙 |
|------|------|------|
| `errorCode` | 문자열 enum | 아래 목록과 정확히 동일 |
| `message` | string | 아래 표준 문구와 전체 문자열 일치 |

**errorCode 목록:** `INVALID_GRID_SIZE`, `INVALID_EMPTY_CELL_COUNT`, `VALUE_OUT_OF_RANGE`, `DUPLICATE_NONZERO_VALUE`, `NO_SOLUTION`, `AMBIGUOUS_SOLUTION`, `DOMAIN_UNEXPECTED` (매핑 누락 방지용, 사용 여부는 프로젝트에서 단일 정책으로 택일).

### 2.3 UI 레벨 테스트 (Contract-first, RED 우선)

**전제:** Domain 포트는 Mock (성공 시 고정 `int[6]`, 인자 캡처, 에러 던지기).

| TC-ID | 설명 | Mock 기대 | 검증 포인트 |
|-------|------|-------------|-------------|
| U-T01 | 4×4 유효 입력 | 성공 반환 | Domain 호출 1회, 반환 배열 값 동등 |
| U-T02 | 행 개수 3 | Mock 미호출 | `INVALID_GRID_SIZE` + 표준 message |
| U-T03 | 행 길이 불균일 | Mock 미호출 | 동일 |
| U-T04 | 빈칸 1개 | Mock 미호출 | `INVALID_EMPTY_CELL_COUNT` |
| U-T05 | 빈칸 3개 | Mock 미호출 | 동일 |
| U-T06 | 셀 값 17 | Mock 미호출 | `VALUE_OUT_OF_RANGE` |
| U-T06b | 셀 값 -5 | Mock 미호출 | 동일 |
| U-T07 | 중복 값 | Mock 미호출 | `DUPLICATE_NONZERO_VALUE` |
| U-T08 | Domain `NO_SOLUTION` | Mock | 동일 코드·문구 전달 |
| U-T09 | Domain `AMBIGUOUS_SOLUTION` | Mock | 동일 |
| U-T10 | 출력 길이·좌표 범위 | Mock이 경계값 벡터 | Boundary 추가 검증(선택) |

### 2.4 UX/출력 규칙 — 에러 메시지 표준 (정확한 문구)

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

**체크리스트**

- [ ] 모든 UI 실패 테스트가 위 표의 `message`를 `assertEquals`로 검증
- [ ] `errorCode` 대소문자·스펠링 고정
- [ ] 성공 응답에 `result`만 포함하는지 직렬화 스키마에 명시

---

## 3) Data Layer 설계

### 3.1 목적 정의

| 항목 | 내용 |
|------|------|
| 목적 | Application/Domain과 저장 매체 분리; 동일 유스케이스에 대해 메모리/파일 교체 |
| 범위 | (A) 마지막 입력 그리드 저장·로드 (B) 마지막 성공 `int[6]` 저장·로드 (선택) |
| 비범위 | DB 스키마, 마이그레이션, 동시성, 보안 |

### 3.2 인터페이스 계약

| 메서드 (개념) | 입력 | 출력 | 실패 |
|---------------|------|------|------|
| `MatrixRepository.saveInput(grid: int[][])` | 입력 계약 만족 그리드 | void 또는 저장 키 | `STORAGE_WRITE_FAILED` |
| `MatrixRepository.loadInput()` | 없음 | `int[][]` 또는 empty | `NOT_FOUND` (또는 empty 정책 택일) |
| `MatrixRepository.saveResult(vector: int[6])` | 성공 결과만 | void | 동상 |
| `MatrixRepository.loadResult()` | 없음 | `int[6]` optional | `NOT_FOUND` |

**저장 정책:** 저장 시점에 “검증 통과된 것만 저장”으로 고정하면 불변 재검증 비용을 줄일 수 있다.

### 3.3 구현 옵션 비교 및 추천

| 기준 | 옵션 A: InMemory | 옵션 B: File (JSON 권장) |
|------|------------------|---------------------------|
| 프로세스 재시작 후 유지 | 없음 | 있음 |
| 테스트 난이도 | 낮음 | 중간 (임시 디렉터리) |
| 실패 모드 | 거의 없음 | 파일 없음, JSON 깨짐, 타입 불일치 |
| 학습 목표 | 레이어 분리 | 분리 + I/O 예외 + 직렬화 계약 |

**추천:** **옵션 B (JSON 파일)** — “메모리/파일 교체 가능” 제약을 충족하고 Data 레이어 테스트(파일 없음·형식 오류)를 실제로 작성 가능. **InMemory는 테스트용 Fake로 병행** 권장.

### 3.4 Data 레이어 테스트

| TC-ID | 내용 | 기대 |
|-------|------|------|
| DT-01 | saveInput 후 loadInput | 배열 깊은 동등, 4×4 |
| DT-02 | saveResult 후 loadResult | `int[6]` 동등 |
| DT-03 | loadInput 파일 없음 | `NOT_FOUND` (또는 empty 정책 일치) |
| DT-04 | 손상 JSON | `STORAGE_CORRUPT` |
| DT-05 | JSON에 3×3 데이터 | `STORAGE_SCHEMA_INVALID` + 4×4 불변 위반 |
| DT-06 | 저장 전 검증 정책 | 잘못된 그리드는 저장 거부 등 정책과 테스트 일치 |

**불변조건 체크리스트**

- [ ] 로드 직후 행/열 길이 4
- [ ] 선택: 로드 후 UI와 동일 전처리 시 동일 에러

---

## 4) Integration & Verification

### 4.1 통합 경로 정의

```text
Caller
  → UI Boundary (입력 검증, 출력/에러 매핑)
      → Application Service (선택)
          → Domain (resolve)
      ←
  ↔ Data Boundary (선택: save/load)
```

**의존성 방향:** UI → Application(선택) → Domain 포트. Domain은 Data를 참조하지 않음. Application이 `MatrixRepository`를 주입받아 사용.

### 4.2 통합 테스트 시나리오

**정상 (2개 이상)**

| IT-ID | 흐름 |
|-------|------|
| IT-01 | 유효 그리드 → Domain 실제 구현 → `int[6]` 기대값 일치 |
| IT-02 | IT-01 후 save → 새 인스턴스로 load → 재실행 결과 동일 |

**실패 (3개 이상)**

| IT-ID | 흐름 |
|-------|------|
| IT-E01 | 잘못된 크기 → UI 거부, Domain·Data 미호출 |
| IT-E02 | 유효 형식·불가능 퍼즐 → `NO_SOLUTION` + 고정 문구 |
| IT-E03 | 손상된 저장 파일 로드 → `STORAGE_CORRUPT` 및 상위 매핑 규칙 고정 |

### 4.3 회귀 보호 규칙

| 규칙 | 설명 |
|------|------|
| R-01 | `int[6]`·1-index·`n1,n2` 순서에 대한 골든 테스트 변경 시 PR에 “계약 변경” 라벨 |
| R-02 | 에러 `message` 변경은 의도된 계약 변경으로만; CI에서 명시 assert |
| R-03 | Domain 포트 시그니처 변경 시 Mock UI 테스트로 조기 발견 |
| R-04 | 기존 테스트 삭제 금지; 대체 시 동일 TC-ID 범위 커버 증명 |

### 4.4 커버리지 목표

| 레이어 | 목표 |
|--------|------|
| Domain | 95%+ (라인/브랜치, 실패 경로 포함) |
| UI Boundary | 85%+ (모든 errorCode + 성공 1회) |
| Data | 80%+ (정상·파일 없음·손상·스키마 오류) |

### 4.5 Traceability Matrix

| Concept (Invariant / Rule) | Rule ID | Use Case | Contract | Test | Component |
|-----------------------------|----------|----------|----------|------|-----------|
| 4×4 크기 | INV-01 | S2 전처리 | UI Input + DA-01 | U-T02~03, D-T06 | UI, Domain |
| 빈칸 2개 | INV-02 | UC-D01 | DA-02, UI Input | U-T04~05, D-T07~08 | UI, Domain |
| 값 범위 | INV-03 | S2 | UI Input, DA-01 | U-T06~06b, D-T09~10 | UI, Domain |
| 0 제외 중복 금지 | INV-04 | S2 | UI Input, DA-01 | U-T07, D-T11 | UI, Domain |
| 1~16 완전 사용 | INV-05 | UC-D03 | DA-04 | D-T15 | Domain |
| 행/열/대각 합 34 | INV-06~09 | UC-D03~04 | DA-04 | D-T01~02, D-T14 | Domain |
| 빈칸 스캔 순서 | INV-10 | UC-D01, UC-D05 | DA-02, DA-05 | D-T03 | Domain |
| 출력 순서 | Rule-OUT | UC-D05 | Output, DA-05 | D-T04~05, IT-01 | Domain, Integration |
| 입력 검증 우선 | Rule-LAYER | S2~S3 | UI contract | U-T01~10 | UI |
| 저장 정합성 | INV-STORE | IT-02 | save/load | DT-01~02, IT-02 | Data |
| 손상/스키마 | Rule-IO | — | Data errors | DT-04~05, IT-E03 | Data |
| 고정 에러 문구 | Rule-MSG | S5 | Error schema | U-T02~09, IT-E01~02 | UI |

---

## 부록: Dual-Track TDD 체크리스트

| 트랙 | 산출물 | 완료 기준 |
|------|--------|-----------|
| Logic | §1.5 테스트 목록 + 에러 타입 | Domain RED 후 최소 1 GREEN 루프 |
| UI | §2.3~2.4 | Mock으로 UI RED → Adapter 연결 |
| Data | §3.4 + Fake/JSON 순서 | File I/O는 테스트 임시 폴더 고정 |

---

**문서 끝**
