# To-do list creation references
_Exported on 4/28/2026 at 10:41:07 GMT+9 from Cursor (3.2.11)_

---

**User**

Ｔｏ－Ｄｏ　리스트를 작성하고 싶습니다. 작성한 문서 중 무엇을 참조해서 만들어야 할까요?


---

**Cursor**

열람 중인 문서와 프로젝트의 문서 구조를 확인합니다.



To-Do를 **무엇을 위해** 쓰는지에 따라 참조 문서를 나누면 됩니다.

## 1. 항상 기준으로 삼을 문서: `docs/PRD_MagicSquare_4x4_TDD.md`

**제품·구현·테스트의 단일 근거**입니다. To-Do를 “해야 할 일”로 쪼갤 때 여기서 뽑는 것이 맞습니다.

| PRD 구간 | To-Do에 쓰는 방식 |
|----------|-------------------|
| **§5 FR-01~** | 기능 단위·AC(승인 기준)별 체크리스트 |
| **§6 BR / 오류** | 오류 코드·메시지·경계 vs 도메인 동작 |
| **§2.3 INV-C1~C5** | “완성” 판정·도메인 테스트 조건 |
| **§7 NFR** | 성능·부작용·재현 가능 빌드(NFR-06 등) |
| **§8 Dual-Track / MLOps** | UX Contract vs Logic Rule, CI 게이트·금지 의존성 |
| **§9 테스트 플랜** | 시나리오·트랙(A/B)·실행 순서(§9.5) |
| **§10 아키텍처·§10.4** | 패키지·레이어·테스트 배치 |
| **§12 추적성** | FR/TP/TD와 테스트 매핑(누락 방지) |
| **§13 Glossary** | 용어 통일(이슈 제목·태그에 사용) |

PRD 자체에 **“근거 문서”**로 `Reporter/01`, `02`, `03`, `04`가 적혀 있으므로, PRD만으로 부족할 때만 그 Reporter를 보조로 열면 됩니다.

---

## 2. “PRD 반영 후 바로 할 일”용: `Reporter/17_magic-square-prd-dual-track-mlops-alignment-report.md`

PRD **전문 대체**가 아니라, **1.1~1.2 변경 요약 + 권장 후속**이 들어 있습니다. 특히 **§5 구현·CI에 대한 권장 후속**에 CI Job 분리, ArchUnit/리뷰 규칙, Reporter/16 갱신 같은 **짧은 실행 목록**이 있어, “문서 작업 다음 스텝” To-Do를 만들 때 참조하기 좋습니다.

---

## 3. 사용자 스토리·에픽 단위 To-Do: `Reporter/09`~`15` (User Journey 계열)

**사용자 여정·에픽·시나리오**로 쪼개진 To-Do를 원하면 `Reporter/11`(user stories), `Reporter/12`~`14`(level3~5 시나리오/검증) 등이 맞습니다. PRD의 FR/AC와 **중복·불일치**가 없는지는 PRD로 한 번 맞추는 것이 안전합니다.

---

**정리:**  
- **기본:** `docs/PRD_MagicSquare_4x4_TDD.md`  
- **CI·정합·후속 3줄 요약:** `Reporter/17_magic-square-prd-dual-track-mlops-alignment-report.md`  
- **스토리/에픽 쪼개기:** `Reporter/09`~`15` + 필요 시 PRD §12로 추적성 맞추기

---

**User**

당신은 시니어 소프트웨어 아키텍트이자 TDD 코치입니다. 할 일 목록의 항목과 완료 조건은 docs/5.PRD_MagicSquare_4x4_TDD.md를 주 소스로 두고, 스토리 단위 분해는 Report/4, 계약·오류 세부는 Report/2, 품질·TDD·ECB 준수는 Report/3와 Cursor 규칙을 참조해,
다음 방법론을 적용하여
"Magic Square 4x4 완성 시스템"의 구현용 To-Do 구조를 작성하세요.
적용 방법론:
Concept-to-Code Traceability
Dual-Track UI + Logic TDD
To-Do → Scenario → Test → Code 구조
ECB(Entity / Control / Boundary) 모델
RED → GREEN → REFACTOR
반드시 한국어로 작성하세요.
[시스템 목표]
부분적으로 비어 있는 4x4 Magic Square를 완성하는 시스템의 개발 To-Do를 작성합니다.
[도메인 규칙]
보드는 4x4이다.
숫자는 1~16만 사용한다.
0은 빈칸이다.
정확히 2칸이 비어 있다.
0을 제외한 중복 숫자는 허용되지 않는다.
모든 행, 열, 대각선의 합은 34여야 한다.
해결 가능한 경우 빈칸 값을 찾아 채운다.
유효하지 않은 보드는 거부한다.
[출력 형식]
다음 구조를 반드시 지켜서 작성하세요.
Epic
User Story
Phase별 Task 목록
각 Task에는 반드시 아래 정보를 포함하세요.
Task ID
RED / GREEN / REFACTOR 여부
작업 제목
Scenario Level (L0/L1/L2/L3)
연결되는 Test 이름
연결되는 Code 대상
ECB 스테레오타입 (Entity / Control / Boundary)
필요 시 체크포인트
[표현 스타일]
Markdown 사용
체크박스 형식 사용
실제 Cursor.AI 실습용 개발 보드처럼 작성
식별자는 Epic-001, US-001, TASK-001 형식 사용
유효한 케이스와 실패 케이스를 모두 포함
최소한 다음 작업을 포함
보드 생성
보드 유효성 검사
빈칸 탐지
후보값 필터링
완성 로직
잘못된 입력 처리
테스트 커버리지 체크포인트
[Scenario Level 정의]
L0: 기능 개요
L1: 정상 흐름
L2: 경계 상황
L3: 실패 상황
[추가 제약]
Logic 책임은 명확히 분리할 것
UI/Boundary에는 비즈니스 규칙을 넣지 말 것
Control은 검증과 해결 흐름을 조율할 것
Entity는 보드 상태를 표현할 것
모든 To-Do는 Scenario, Test, Code로 추적 가능해야 함
이제
"Magic Square 4x4 완성 시스템"의 To-Do 구조를 생성하세요.


---

**Cursor**

PRD와 Reporter 02·03·04를 읽어 식별자·용어·테스트 플랜과 정합시킵니다.



참고: 저장소에는 `docs/5.PRD_MagicSquare_4x4_TDD.md`가 없고, 동일 역할의 주 소스는 `docs/PRD_MagicSquare_4x4_TDD.md`입니다. 아래 To-Do는 해당 PRD와 `Reporter/02`, `Reporter/03`, `Reporter/04` 및 PRD §8·§9를 정합해 작성했습니다.

---

# Magic Square 4×4 완성 시스템 — 구현용 To-Do 구조

**추적 체인:** Concept(PR §2·§5) → Scenario(TP-*, §9.1) → Test(클래스·메서드명) → Code(패키지·타입)  
**방법론:** Dual-Track(UI=Track A UX Contract / Logic=Track B), ECB, RED → GREEN → REFACTOR  
**주 소스:** `docs/PRD_MagicSquare_4x4_TDD.md` (FR-01~05, §6 BR-ERR, §7 NFR, §8~§9, §10.4)  
**보조:** `Reporter/02`(계약·DA/UC/D-T), `Reporter/03`·`Reporter/04`(TDD 단계·PR 단위 루프)

---

## Epic-001 — Magic Square 4×4 완성 시스템

**에픽 완료 조건(DoD):** PRD §12 해당 행 추적성 유지, §8.8 Job A·B Green, FR-01~05 AC 및 TP-01~TP-08 회귀 통과, NFR-01·02 하한 충족(측정 시).

---

### US-001 — 보드(격자) 표현·골든 픽스처·개념 고정

**스토리:** 호출자 `int[][]`와 도메인이 공유하는 **4×4 보드 상태**를 Entity로 표현하고, PRD §9.3 TD-* 픽스처로 시나리오·테스트가 동일 입력을 재사용한다.  
**완료 조건:** TD-01~TD-04 로딩 유틸(또는 상수) 존재, 1-index 변환 규칙이 Boundary 한 곳(또는 전용 VO)에만 존재.

#### Phase 1 — 골격·픽스처 (Track B 중심)

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-001 |
| **단계** | RED |
| **작업 제목** | Entity: 부분 보드 불변량·TD 픽스처 로더에 대한 실패 테스트 추가 |
| **Scenario Level** | L0 |
| **연결 Test** | `PartialMagicSquareTest` / `GoldenGridLoaderTest#td01_rejects_emptyCellCountNotTwo` (개념 스케치), `MagicSquareGridFactoryTest` |
| **연결 Code** | `.../domain/model/PartialMagicSquare.java`(또는 동등명), `.../test/fixtures/GoldenGrids.java` |
| **ECB** | Entity |
| **체크포인트** | 테스트가 **컴파일은 되나 의도된 실패**(아직 구현 없음); TD-01 용도가 PRD 표와 일치하는지 주석에 `TD-01` 명시 |
| **추적** | FR-01 전제 구조, §9.3 TD-* |

- [ ] TASK-001 완료

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-002 |
| **단계** | GREEN |
| **작업 제목** | Entity·골든 `int[][]` 빌더 최소 구현으로 TD-02 로딩·스냅샷 비교 통과 |
| **Scenario Level** | L1 |
| **연결 Test** | `GoldenGridsTest#loadG0_twoZeros_matchesExpectedCoordinates` |
| **연결 Code** | `GoldenGrids`, `PartialMagicSquare` |
| **ECB** | Entity |
| **체크포인트** | NFR-04: 픽스처가 **호출자 배열을 변형하지 않음**(복사본 사용) |
| **추적** | TP-01/TP-02 준비 데이터, BR-05 |

- [ ] TASK-002 완료

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-003 |
| **단계** | REFACTOR |
| **작업 제목** | VO 추출(`CellCoordinate`, `MagicConstant=34`) 및 Entity 책임 정리 |
| **Scenario Level** | L2 |
| **연결 Test** | 기존 `GoldenGridsTest`, `CellCoordinateTest`(행·열 경계 1~4) |
| **연결 Code** | `CellCoordinate`, `MagicConstant`, `PartialMagicSquare` |
| **ECB** | Entity (+ Value Object) |
| **체크포인트** | Report/02 INV-10과 스캔 순서 문서화 일치 |
| **추적** | Reporter/02 §1.1 |

- [ ] TASK-003 완료

---

### US-002 — Boundary: 보드 유효성 검사 (FR-01)

**스토리:** 4×4, 0 두 칸, 1~16·중복 규칙을 Boundary에서만 검증하고, 실패 시 도메인 미호출(AC-FR01-6).  
**완료 조건:** BR-ERR-01~04 메시지 **전문** 일치(Track A), Logic 테스트는 코드·타입만(Track B는 별 Task에서 스파이).

#### Phase 2 — Dual-Track 대칭 RED (TP-05~08)

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-004 |
| **단계** | RED |
| **작업 제목** | Track B: `GridValidator`/`BoundaryValidator` 거부 결과 타입·코드만 단언 실패 테스트 |
| **Scenario Level** | L3 |
| **연결 Test** | `GridValidationResultTest` — `INVALID_GRID_SIZE`, `INVALID_EMPTY_CELL_COUNT`, `VALUE_OUT_OF_RANGE`, `DUPLICATE_NONZERO_VALUE` |
| **연결 Code** | `.../boundary/GridValidator.java` |
| **ECB** | Boundary |
| **체크포인트** | **비즈니스 규칙(행합 34 등) 없음** — 크기·0 개수·범위·중복만 |
| **추적** | FR-01, TP-05~TP-08, Reporter/02 D-T06~D-T11 |

- [ ] TASK-004 완료

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-005 |
| **단계** | RED |
| **작업 제목** | Track A: Facade 호출 시 `errorCode`+전체 `message` assert 실패 테스트 |
| **Scenario Level** | L3 |
| **연결 Test** | `MagicSquareFacadeContractTest#tp05_invalidGridSize_messageExact` 등 |
| **연결 Code** | `.../application/MagicSquareFacade.java`, `.../boundary/GridValidator.java` |
| **ECB** | Boundary (+ Application 진입) |
| **체크포인트** | **`**/domain/**` 직접 import 금지**(PRD §8.5.1); Domain은 Mock |
| **추적** | TP-05~TP-08, §8.4 Track A |

- [ ] TASK-005 완료

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-006 |
| **단계** | GREEN |
| **작업 제목** | `GridValidator` 구현 + Facade에서 검증 실패 시 도메인 포트 **0회** 호출 |
| **Scenario Level** | L3 |
| **연결 Test** | `GridValidatorTest`, `MagicSquareFacadeContractTest`(TP-05~08) |
| **연결 Code** | `GridValidator`, `MagicSquareFacade`, `DomainResolvePort`(mock) |
| **ECB** | Boundary, Control(Facade) |
| **체크포인트** | AC-FR01-6, AC-FR01-7(배열 불변) |
| **추적** | FR-01 |

- [ ] TASK-006 완료

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-007 |
| **단계** | REFACTOR |
| **작업 제목** | 오류 매핑 단일 SoT(`ErrorMessages` 또는 enum+메시지)로 중복 제거 |
| **Scenario Level** | L2 |
| **연결 Test** | 동일 TP-05~08 스위트 전부 Green |
| **연결 Code** | `ErrorCode`, `ErrorMessages` |
| **ECB** | Boundary |
| **체크포인트** | 부분 문자열 assert 금지(§8.9) |
| **추적** | §6 BR-ERR, Reporter/03 refactor 규칙 |

- [ ] TASK-007 완료

---

### US-003 — 빈칸 탐지·누락 숫자(후보 쌍) (FR-02, FR-03)

**스토리:** 유효 부분 보드에서 결정적 빈칸 2곳과 `{a,b}` 누락 쌍을 산출한다(시도 순서의 **후보값 공간**은 `{min,max}` 두 배치로 한정).  
**완료 조건:** BR-05, BR-06, P-01, P-02.

#### Phase 3 — Logic (Track B)

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-008 |
| **단계** | RED |
| **작업 제목** | `locateEmptyCells` row-major 순서 실패 테스트(D-T03) |
| **Scenario Level** | L1 |
| **연결 Test** | `EmptyCellLocatorTest#rowMajorOrder_extremeZeros` |
| **연결 Code** | `.../domain/EmptyCellLocator.java` |
| **ECB** | Control(도메인 서비스로 분류 시) 또는 Entity 헬퍼 — **권장:** Report/02 `EmptyCellLocator` = 도메인 서비스 → 여기서는 **Control** 역할의 순수 오케스트레이션 아님 **Domain 서비스**로 표기 |
| **ECB (정정)** | Entity 조회에 가깝지만 Report/02 명명 준수 시 **Control** 대신 **Domain Service** — 사용자 표에 **ECB: Control** 요구 시: **Control** = `CompletionFlow` 내 한 단계로 호출만 하고 규칙은 `EmptyCellLocator`에 위임 → 아래처럼 통일: |
| **ECB** | **Domain에서 FR-02 전담 컴포넌트** → 스테레오타입을 **Entity**가 아닌 경우, PRD ECB 요구에 맞춰 **Boundary 아님·규칙 보유자 아님**이면 **Control**로 표기하기 애매함. 사용자가 "Entity는 보드 상태, Control은 검증과 해결 흐름 조율"이라 했으므로: **빈칸 탐지 로직 클래스 = Domain 순수 함수 묶음**을 ECB에 **Control 하위의 도메인 유스케이스 단계**로 표기하기 어렵다. 일반 ECB: **EmptyCellLocator = Entity에 대한 읽기 전용 연산** → **Control**이 맞음(상태 변경 없이 흐름의 한 단계). |

실제로 Report/02 says EmptyCellLocator is Domain Service. User asked ECB: Entity / Control / Boundary only. So map:
- EmptyCellLocator → **Control** (orchestration of scan - actually it's pure function, often called part of domain). I'll use **Control** for "use case step" services that aren't boundary: User said "Control은 검증과 해결 흐름을 조율" - so locate empty is part of resolve flow → could be sub-control. Simplest: **EmptyCellLocator = Control** (domain control object).

I'll label Domain services as **Control** for FR-02/03/04/05 as user requested Control coordinates validation and resolution flow - the actual classes EmptyCellLocator etc. are the **workers** inside domain. Alternative: mark as **Entity** only if stateful. I'll use:
- **Boundary**: validation only
- **Control**: `MagicSquareCompletionService` (orchestrates validate → locate → missing → try placements) 
- **Entity**: grid
- **Sub-components**: For task granularity, I'll put **EmptyCellLocator** as **Control** (application-style domain control) - actually in ECB, Control handles use cases. So `ResolveMagicSquareUseCase` = Control, `EmptyCellLocator` = could be helper. I'll assign **Control** to the Facade/Application and **inner** `EmptyCellLocator` as part of domain package but ECB column = **Control** when it's "flow step" without UI.

To avoid confusion I'll use:
- **Entity**: `PartialMagicSquare`, `CellCoordinate`
- **Control**: `MagicSquareResolver` / `CompletionCoordinator` (FR-02~05 오케스트레이션), `EmptyCellLocator`, `MissingNumberResolver`, `MagicSquareCompletenessChecker` as **협력 객체** — 사용자 표에 단일 ECB만 가능하면 **주 타입 하나**에 매핑: e.g. TASK-008 Code = `EmptyCellLocator` ECB = **Control** (도메인 제어 로직).

Proceeding with **Control** for all domain services (locate, missing, isMagic, resolve) and **Entity** for grid/state.

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-008 |
| **단계** | RED |
| **작업 제목** | 빈칸 2개 row-major 결정적 좌표 단위 테스트(실패 상태) |
| **Scenario Level** | L1 |
| **연결 Test** | `EmptyCellLocatorTest` |
| **연결 Code** | `EmptyCellLocator` |
| **ECB** | Control |
| **체크포인트** | Logic 트랙: **message 문자열 assert 없음** |
| **추적** | FR-02, D-T03, P-02 |

- [ ] TASK-008 완료

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-009 |
| **단계** | GREEN |
| **작업 제목** | `EmptyCellLocator` 구현 |
| **Scenario Level** | L1 |
| **연결 Test** | `EmptyCellLocatorTest` |
| **연결 Code** | `EmptyCellLocator` |
| **ECB** | Control |
| **체크포인트** | AC-FR02-1 |
| **추적** | FR-02 |

- [ ] TASK-009 완료

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-010 |
| **단계** | RED |
| **작업 제목** | 누락 숫자 집합 `{a,b}` 및 min/max **후보값 필터링** 단위 테스트 |
| **Scenario Level** | L1 |
| **연결 Test** | `MissingNumberResolverTest#fromGoldenPartial_missingPairMatchesSetDifference` |
| **연결 Code** | `MissingNumberResolver` |
| **ECB** | Control |
| **체크포인트** | FR-03, BR-06, 사용자 요구 "후보값 필터링" = {1..16}\present |
| **추적** | FR-03, D-T01 |

- [ ] TASK-010 완료

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-011 |
| **단계** | GREEN |
| **작업 제목** | `MissingNumberResolver` 구현 |
| **Scenario Level** | L1 |
| **연결 Test** | `MissingNumberResolverTest` |
| **연결 Code** | `MissingNumberResolver` |
| **ECB** | Control |
| **체크포인트** | 누락 개수 ≠2는 FR-01에서 불가능함을 테스트 코멘트로 명시 |
| **추적** | FR-03 |

- [ ] TASK-011 완료

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-012 |
| **단계** | REFACTOR |
| **작업 제목** | 완전 격자 복사·임시 배치 유틸 추출(부작용 없는 시도 격자 생성) |
| **Scenario Level** | L2 |
| **연결 Test** | `GridCopyTest` (원본 vs 시도용 복사) |
| **연결 Code** | `GridCopier` 또는 `PartialMagicSquare#withPlacements` |
| **ECB** | Entity |
| **체크포인트** | NFR-04 |
| **추적** | DEC-05 |

- [ ] TASK-012 완료

---

### US-004 — 완성 로직: 마방진 판정 + 두 시도 해결 (FR-04, FR-05)

**스토리:** 0 없는 격자에 대해 INV-C1~C5 판정, 시도1(min→첫 빈칸)·시도2 역배치, 성공 시 `int[6]`, 실패 시 `NO_SOLUTION`, 모호 시 `AMBIGUOUS_SOLUTION`.  
**완료 조건:** TP-01~TP-04, DEC-01~04.

#### Phase 4 — 완성·판정 (Track B + 일부 A)

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-013 |
| **단계** | RED |
| **작업 제목** | `isCompletedMagicSquare`(FR-04) 참/거짓 실패 테스트(TD-03, D-T14~15) |
| **Scenario Level** | L2 |
| **연결 Test** | `MagicSquareCompletenessCheckerTest` |
| **연결 Code** | `MagicSquareCompletenessChecker` |
| **ECB** | Control |
| **체크포인트** | 0 셀 포함 시 호출 금지 정책을 테스트로 고정 |
| **추적** | FR-04, INV-C1~C5, TP-규격 데이터 TD-03 |

- [ ] TASK-013 완료

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-014 |
| **단계** | GREEN |
| **작업 제목** | FR-04 최소 구현 |
| **Scenario Level** | L2 |
| **연결 Test** | `MagicSquareCompletenessCheckerTest` |
| **연결 Code** | `MagicSquareCompletenessChecker` |
| **ECB** | Control |
| **체크포인트** | AC-FR04-1~4 |
| **추적** | FR-04 |

- [ ] TASK-014 완료

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-015 |
| **단계** | RED |
| **작업 제목** | 두 배치 시도·시도1 성공 시 시도2 미호출·`int[6]` 골든(TP-01, TP-02, D-T04~05) |
| **Scenario Level** | L1 |
| **연결 Test** | `ResolveTwoPlacementsTest` / `SolutionOrderingPolicyTest` |
| **연결 Code** | `MagicSquareResolver`(Control), `MagicSquareCompletenessChecker` |
| **ECB** | Control |
| **체크포인트** | DEC-03 스파이로 검증 |
| **추적** | FR-05, TP-01, TP-02 |

- [ ] TASK-015 완료

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-016 |
| **단계** | GREEN |
| **작업 제목** | FR-05 해 결정 로직 구현 |
| **Scenario Level** | L1 |
| **연결 Test** | `ResolveTwoPlacementsTest` |
| **연결 Code** | `MagicSquareResolver` |
| **ECB** | Control |
| **체크포인트** | AC-FR05-1~5, BR-11, BR-12 |
| **추적** | FR-05 |

- [ ] TASK-016 완료

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-017 |
| **단계** | RED |
| **작업 제목** | `NO_SOLUTION`·`AMBIGUOUS_SOLUTION` 도메인 결과 타입(메시지 없음) |
| **Scenario Level** | L3 |
| **연결 Test** | `ResolveTwoPlacementsTest#tp03_noSolution_codeOnly`, `...#tp04_ambiguous_codeOnly` |
| **연결 Code** | `ResolutionResult`, `MagicSquareResolver` |
| **ECB** | Control |
| **체크포인트** | TP-03, TP-04 Logic 측 |
| **추적** | DEC-01, DEC-02 |

- [ ] TASK-017 완료

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-018 |
| **단계** | GREEN |
| **작업 제목** | TD-04 등으로 TP-03·TP-04 Track B Green |
| **Scenario Level** | L3 |
| **연결 Test** | 위와 동일 + `GoldenGridsTest` |
| **연결 Code** | `MagicSquareResolver`, `GoldenGrids` |
| **ECB** | Control |
| **체크포인트** | BR-ERR-05/06는 Boundary 매핑 전 **코드 enum만** |
| **추적** | TP-03, TP-04 |

- [ ] TASK-018 완료

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-019 |
| **단계** | REFACTOR |
| **작업 제목** | `MagicSquareFacade`가 Control(`MagicSquareResolver`)만 호출하도록 의존성 주입 정리 |
| **Scenario Level** | L0 |
| **연결 Test** | Track A+B 통합 스위트 |
| **연결 Code** | `MagicSquareFacade`, `MagicSquareResolver` |
| **ECB** | Control |
| **체크포인트** | §10.3 의존성 방향 |
| **추적** | §10.1 |

- [ ] TASK-019 완료

---

### US-005 — 잘못된 입력·도메인 실패의 외부 계약 (Track A + E2E)

**스토리:** 유효 입력 성공·무해·모호 거부가 **errorCode+전체 message**로 관측된다.  
**완료 조건:** TP-01~TP-04의 A측, BR-ERR-05~06.

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-020 |
| **단계** | RED |
| **작업 제목** | Facade 통합: 성공 `int[6]`·`NO_SOLUTION`·`AMBIGUOUS_SOLUTION` 메시지 전문 |
| **Scenario Level** | L1 / L3 |
| **연결 Test** | `MagicSquareFacadeContractTest#tp01_tp02_success`, `#tp03_tp04_failures` |
| **연결 Code** | `MagicSquareFacade`, `GridValidator`, `MagicSquareResolver` |
| **ECB** | Boundary + Control |
| **체크포인트** | Track A: Domain 구체 클래스 import 금지 |
| **추적** | TP-01~TP-04, §8.3 |

- [ ] TASK-020 완료

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-021 |
| **단계** | GREEN |
| **작업 제목** | Facade에서 도메인 실패→BR-ERR 메시지 매핑 구현 |
| **Scenario Level** | L3 |
| **연결 Test** | `MagicSquareFacadeContractTest` |
| **연결 Code** | `MagicSquareFacade`, `ErrorMessages` |
| **ECB** | Boundary |
| **체크포인트** | `DOMAIN_UNEXPECTED` 경로 단일 정책 |
| **추적** | BR-ERR-07, §6 |

- [ ] TASK-021 완료

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-022 |
| **단계** | REFACTOR |
| **작업 제목** | `resolve` 단일 진입점·예외 vs Result 타입 통일 |
| **Scenario Level** | L2 |
| **연결 Test** | 전체 Contract 스위트 |
| **연결 Code** | `MagicSquareFacade` |
| **ECB** | Control |
| **체크포인트** | NFR-03 동일 입력 두 번 |
| **추적** | P-05, NFR-03 |

- [ ] TASK-022 완료

---

### US-006 — 테스트 커버리지·CI·품질 게이트

**스토리:** NFR-01·02·06 및 Job A/B 분리로 MLOps 정합.  
**완료 조건:** JaCoCo(또는 동등) 리포트, PRD §9.5 순서·접두사.

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-023 |
| **단계** | RED |
| **작업 제목** | 커버리지 미달 시 실패하는 임계 테스트 또는 CI 스크립트(현재 실패) |
| **Scenario Level** | L0 |
| **연결 Test** | CI job `coverage-threshold` (빌드 스크립트) |
| **연결 Code** | `pom.xml` / `build.gradle.kts`, `.github/workflows/*.yml` |
| **ECB** | Boundary(외부 도구) — 또는 인프라로 ECB N/A; 여기서는 **Control** 없음 → 표기 **Boundary** 생략하고 **인프라**로: 사용자가 ECB 세 가지만 허용 → **Control** = 빌드 오케스트레이션은 보통 코드 밖 — **ECB: Control**에 `CoverageGate` 없으면 **Boundary**로 CI 설정 파일 |
| **ECB** | **Control** (품질 게이트 정책을 코드로 표현 시 `CoverageRules`) — 실무적으로 **N/A** 대신 **Boundary**로 두지 않음. **Entity** 아님. **Control**: `build.gradle`의 task가 조율 → **Control** |
| **체크포인트** | Domain ≥95%, Boundary ≥85% (NFR-01, NFR-02) |
| **추적** | §7, §8.5.1 |

- [ ] TASK-023 완료

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-024 |
| **단계** | GREEN |
| **작업 제목** | JaCoCo 한도·Job A(`contract-test`)/Job B(`domain-test`) 분리 |
| **Scenario Level** | L0 |
| **연결 Test** | CI 전체 Green |
| **연결 Code** | CI YAML, 테스트 소스 세트 분리 |
| **ECB** | Control |
| **체크포인트** | DEC-06, 로그 접두사 `[logic]`/`[ux-contract]`(§9.5) |
| **추적** | §8.5.1, §9.5 |

- [ ] TASK-024 완료

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-025 |
| **단계** | REFACTOR |
| **작업 제목** | ArchUnit 또는 패키지 규칙: Track A가 `domain` 패키지 직접 참조 금지 |
| **Scenario Level** | L2 |
| **연결 Test** | `ArchitectureTest#trackA_mustNotDependOnDomainInternals` |
| **연결 Code** | `src/test/.../ArchitectureTest.java` |
| **ECB** | Boundary(규칙은 테스트이나 검증 대상은 경계) |
| **체크포인트** | §8.5.1, §8.9 |
| **추적** | Reporter/17 권장 후속 |

- [ ] TASK-025 완료

---

## 보드 생성 — 별도 매핑 (요구사항 “최소 포함”)

| 항목 | 내용 |
|------|------|
| **Task ID** | TASK-026 |
| **단계** | RED → GREEN → REFACTOR (한 줄로 묶지 말고 분리 가능) |
| **작업 제목** | **보드 생성:** `int[][]` 빌더(유효/무효 시나리오용)·TD 복제 |
| **Scenario Level** | L1 / L3 |
| **연결 Test** | `TestGridBuilderTest`, 픽스처 사용 테스트 전반 |
| **연결 Code** | `TestGridBuilder` (`src/test/...`) |
| **ECB** | Entity(테스트 전용이면 테스트 헬퍼로 표기 가능 — 프로덕션 Entity는 `PartialMagicSquare.fromArray`) |
| **체크포인트** | 프로덕션 경로는 Boundary 검증 전제와 동일 계약 |
| **추적** | §9.3, Report/4 스토리 분해(테스트 가독성) |

- [ ] TASK-026 완료

---

## Concept-to-Code 추적 요약표

| Concept (PRD) | Scenario | Test 스위트 | Code |
|---------------|----------|-------------|------|
| FR-01 | TP-05~08 | `MagicSquareFacadeContractTest`, `GridValidatorTest` | `GridValidator`, `Facade` |
| FR-02 | TP-01 데이터 | `EmptyCellLocatorTest` | `EmptyCellLocator` |
| FR-03 | TP-01 | `MissingNumberResolverTest` | `MissingNumberResolver` |
| FR-04 | TD-03, D-T14 | `MagicSquareCompletenessCheckerTest` | `MagicSquareCompletenessChecker` |
| FR-05 | TP-01~04 | `ResolveTwoPlacementsTest`, `FacadeContract` | `MagicSquareResolver` |
| INV-C1~C5 | §2.3 | `MagicSquareCompletenessCheckerTest` | 동일 |
| NFR-01~02 | §7 | CI + `CoverageGate` | 빌드 설정 |
| Dual-Track | §8 | Job A / Job B 테스트 디렉터리 | 패키지 분리 |

---

## Cursor 실습 보드용 한 줄 원칙

1. **RED:** 프로덕션 최소 변경; 실패 원인이 시나리오와 일치(Reporter/03).  
2. **GREEN:** 통과에 필요한 최소 구현만(Reporter/03).  
3. **REFACTOR:** 동작·계약 불변, 커버리지 약화 금지(Reporter/03·04).  
4. **PR 단위**로 RED 범위 쪼개기(Reporter/04, PRD §8.10).

---

**파일 경로 참고:** PRD의 권장 레이아웃은 `.../domain/...`, `.../boundary/...`, `.../application/...` 및 Track A 테스트의 `domain` 직접 import 금지입니다(§10.4, §8.5.1).

---

위 본문에서 TASK-023의 ECB 설명이 장황해졌습니다. 사용자에게 전달할 때는 깔끔한 최종본으로 정리하겠습니다. TASK-008 주석의 혼란스러운 "정정" 단락은 제거하고 깔끔한 Markdown만 출력합니다.

I'll rewrite the entire response cleanly without the internal monologue and fix TASK-023 ECB to simply "Control" (build orchestration) or leave as infrastructure - user asked only Entity/Control/Boundary - I'll use **Control** for CI gradle tasks coverage gate.

Also remove duplicate TASK-026 if "보드 생성" is already in TASK-001/002 - user asked minimum includes - TASK-026 is the explicit "보드 생성" - good.

I'll also fix the messy TASK-008 section - only clean tables.

The user wanted Report/4 for story decomposition - Reporter/04 is tdd_rules review, not story - I'll note "Report/4(Reporter/04)는 TDD 단계·PR 루프 보조; 스토리 쪼개기의 1차 근거는 PRD §9 TP와 Reporter/02 UC"

Final output: clean Korean markdown only.

아래는 요청하신 구조·식별자·ECB·Dual-Track·R-G-R·시나리오 레벨을 반영한 **구현용 To-Do**입니다.  
**주 소스:** 저장소 기준 `docs/PRD_MagicSquare_4x4_TDD.md`입니다 (`docs/5.PRD_...` 파일명은 없으며, 내용 SoT는 동일 문서로 간주했습니다).  
**Report/4** = `Reporter/04_magic-square-cursorrules-tdd-rules-review-report.md`(RED 범위를 PR 단위로 쪼개는 등 **단계 집행**), **Report/2** = `Reporter/02_...`(DA/UC/D-T·계약), **Report/3** = `Reporter/03_...`(R-G-R 조건)와 PRD §8·§9를 맞춰 두었습니다.

---

# Epic-001 — Magic Square 4×4 완성 시스템

**에픽 완료 조건:** PRD FR-01~05 AC 충족, TP-01~TP-08 회귀, §6 `errorCode`+`message` 전문 계약, NFR-01·02(측정 시)·NFR-03·NFR-04, §8.5.1 Job A·B Green, §12 추적 행 유지.

---

## US-001 — 보드 표현·보드 생성·골든 픽스처 (Concept → TD)

**스토리 완료 조건:** 4×4·0·1~16 의미가 Entity/픽스처에 고정되고, PRD §9.3 TD-*로 테스트·코드가 동일 입력을 참조한다.

### Phase 1 — Entity·픽스처

- [ ] **TASK-001**  
  - **단계:** RED  
  - **작업 제목:** 부분 보드 Entity·TD-01~TD-04 로더에 대한 실패 테스트 추가  
  - **Scenario Level:** L0  
  - **연결 Test:** `PartialMagicSquareTest`, `GoldenGridsTest#td01_invalidEmptyCount`  
  - **연결 Code:** `.../domain/model/PartialMagicSquare.java`, `.../test/fixtures/GoldenGrids.java`  
  - **ECB:** Entity  
  - **체크포인트:** To-Do → Scenario(TP/TD ID 주석) → Test → Code 링크; Logic 트랙에서 사용자 문구 assert 없음  

- [ ] **TASK-002**  
  - **단계:** GREEN  
  - **작업 제목:** G0(TD-02) 기반 `int[][]` 생성·스냅샷 비교 최소 구현  
  - **Scenario Level:** L1  
  - **연결 Test:** `GoldenGridsTest#loadG0_twoZeros_coordinatesRowMajor`  
  - **연결 Code:** `GoldenGrids`, `PartialMagicSquare`  
  - **ECB:** Entity  
  - **체크포인트:** NFR-04 — 호출자 배열 불변(복사본 사용)  

- [ ] **TASK-003**  
  - **단계:** REFACTOR  
  - **작업 제목:** `CellCoordinate`, `MagicConstant`(34) VO 추출 및 스캔 순서(BR-05) 문서화  
  - **Scenario Level:** L2  
  - **연결 Test:** `CellCoordinateTest`, 기존 `GoldenGridsTest`  
  - **연결 Code:** `CellCoordinate`, `MagicConstant`, `PartialMagicSquare`  
  - **ECB:** Entity  
  - **체크포인트:** Report/02 INV-10과 PRD §2.3 정합  

### Phase 1b — 보드 생성(테스트·데모용)

- [ ] **TASK-026**  
  - **단계:** RED → GREEN → REFACTOR (기능별로 커밋 분리 권장)  
  - **작업 제목:** 유효/무효 보드 `int[][]` 빌더(TestGridBuilder)로 TP·TD 재현성 확보  
  - **Scenario Level:** L1 / L3  
  - **연결 Test:** `TestGridBuilderTest`  
  - **연결 Code:** `src/test/.../TestGridBuilder.java`  
  - **ECB:** Entity (테스트 헬퍼; 프로덕션 진입은 Boundary 경유)  
  - **체크포인트:** Reporter/04 — PR마다 RED 범위 한 덩어리만  

---

## US-002 — Boundary: 보드 유효성 검사 (FR-01)

**스토리 완료 조건:** TP-05~TP-08, AC-FR01-6·7, Boundary에 **마방진 합 34 규칙 없음**.

### Phase 2 — Dual-Track 대칭 (§8.10)

- [ ] **TASK-004**  
  - **단계:** RED  
  - **작업 제목:** Track B — 검증 결과 타입·`errorCode`만 단언(메시지 없음)  
  - **Scenario Level:** L3  
  - **연결 Test:** `GridValidationResultTest` (크기·빈칸 수·범위·중복)  
  - **연결 Code:** `.../boundary/GridValidator.java`  
  - **ECB:** Boundary  
  - **체크포인트:** Report/02 D-T06~D-T11 매핑  

- [ ] **TASK-005**  
  - **단계:** RED  
  - **작업 제목:** Track A — Facade 경로에서 `errorCode`+**전체** `message` 실패 테스트  
  - **Scenario Level:** L3  
  - **연결 Test:** `MagicSquareFacadeContractTest#tp05` ~ `#tp08`  
  - **연결 Code:** `.../application/MagicSquareFacade.java`, `GridValidator`  
  - **ECB:** Boundary (+ Application 진입)  
  - **체크포인트:** §8.5.1 — Track A 테스트가 `**/domain/**` 내부 타입 **직접 import 금지**  

- [ ] **TASK-006**  
  - **단계:** GREEN  
  - **작업 제목:** `GridValidator` + Facade에서 실패 시 도메인 **0회** 호출  
  - **Scenario Level:** L3  
  - **연결 Test:** `GridValidatorTest`, `MagicSquareFacadeContractTest`  
  - **연결 Code:** `GridValidator`, `MagicSquareFacade`, `DomainResolvePort`(mock)  
  - **ECB:** Boundary, Control(Facade 조율)  
  - **체크포인트:** AC-FR01-6·7  

- [ ] **TASK-007**  
  - **단계:** REFACTOR  
  - **작업 제목:** `ErrorCode`·메시지 SoT 단일화(부분 문자열 assert 금지)  
  - **Scenario Level:** L2  
  - **연결 Test:** TP-05~08 전부 Green  
  - **연결 Code:** `ErrorCode`, `ErrorMessages`  
  - **ECB:** Boundary  
  - **체크포인트:** Report/03 — Green에서 구조 리팩터 금지; Report/04 — 단계 혼선 시 PR 분리  

---

## US-003 — 빈칸 탐지·누락 숫자·후보값 공간 (FR-02, FR-03)

**스토리 완료 조건:** BR-05·BR-06, P-01·P-02; 후보값은 `{min,max}` 두 배치로 한정(FR-05 전제).

### Phase 3 — Logic (Track B)

- [ ] **TASK-008**  
  - **단계:** RED  
  - **작업 제목:** row-major 첫·둘째 `0` 좌표 결정성 실패 테스트  
  - **Scenario Level:** L1  
  - **연결 Test:** `EmptyCellLocatorTest#rowMajor_extremePositions`  
  - **연결 Code:** `.../domain/EmptyCellLocator.java`  
  - **ECB:** Control (도메인 유스케이스 단계; Entity는 그리드 상태만)  
  - **체크포인트:** D-T03, §8.4 Track B — **message assert 금지**  

- [ ] **TASK-009**  
  - **단계:** GREEN  
  - **작업 제목:** `EmptyCellLocator` 구현  
  - **Scenario Level:** L1  
  - **연결 Test:** `EmptyCellLocatorTest`  
  - **연결 Code:** `EmptyCellLocator`  
  - **ECB:** Control  
  - **체크포인트:** AC-FR02-1  

- [ ] **TASK-010**  
  - **단계:** RED  
  - **작업 제목:** `{1..16} \ 표시값` 누락 쌍·min/max **후보값 필터링** 테스트  
  - **Scenario Level:** L1  
  - **연결 Test:** `MissingNumberResolverTest#goldenPartial_missingPair`  
  - **연결 Code:** `.../domain/MissingNumberResolver.java`  
  - **ECB:** Control  
  - **체크포인트:** FR-03, BR-06  

- [ ] **TASK-011**  
  - **단계:** GREEN  
  - **작업 제목:** `MissingNumberResolver` 구현  
  - **Scenario Level:** L1  
  - **연결 Test:** `MissingNumberResolverTest`  
  - **연결 Code:** `MissingNumberResolver`  
  - **ECB:** Control  
  - **체크포인트:** AC-FR03-1·2  

- [ ] **TASK-012**  
  - **단계:** REFACTOR  
  - **작업 제목:** 시도용 완전 격자 복사 유틸 추출(NFR-04)  
  - **Scenario Level:** L2  
  - **연결 Test:** `GridCopyImmutabilityTest`  
  - **연결 Code:** `GridCopier` 또는 `PartialMagicSquare#filledCopy`  
  - **ECB:** Entity  
  - **체크포인트:** DEC-05  

---

## US-004 — 완성 로직: 판정 + 두 시도 (FR-04, FR-05)

**스토리 완료 조건:** TP-01~TP-04, INV-C1~C5, DEC-01~04.

### Phase 4 — 완성·해결

- [ ] **TASK-013**  
  - **단계:** RED  
  - **작업 제목:** 0 없는 격자 마방진 판정 true/false 실패 테스트(TD-03)  
  - **Scenario Level:** L2  
  - **연결 Test:** `MagicSquareCompletenessCheckerTest#td03_falseOnBrokenDiagonal`  
  - **연결 Code:** `.../domain/MagicSquareCompletenessChecker.java`  
  - **ECB:** Control  
  - **체크포인트:** FR-04, D-T14·D-T15  

- [ ] **TASK-014**  
  - **단계:** GREEN  
  - **작업 제목:** FR-04 최소 구현  
  - **Scenario Level:** L2  
  - **연결 Test:** `MagicSquareCompletenessCheckerTest`  
  - **연결 Code:** `MagicSquareCompletenessChecker`  
  - **ECB:** Control  
  - **체크포인트:** AC-FR04-1~4, 0 포함 입력 정책  

- [ ] **TASK-015**  
  - **단계:** RED  
  - **작업 제목:** 시도1·시도2·시도1 성공 시 시도2 미호출·`int[6]` 골든  
  - **Scenario Level:** L1  
  - **연결 Test:** `ResolveTwoPlacementsTest#tp01`, `#tp02`, 스파이 `try2NeverCalledWhenTry1Success`  
  - **연결 Code:** `.../domain/MagicSquareResolver.java`, `MagicSquareCompletenessChecker`  
  - **ECB:** Control  
  - **체크포인트:** DEC-03, TP-01·TP-02  

- [ ] **TASK-016**  
  - **단계:** GREEN  
  - **작업 제목:** FR-05 해 결정 로직 구현  
  - **Scenario Level:** L1  
  - **연결 Test:** `ResolveTwoPlacementsTest`  
  - **연결 Code:** `MagicSquareResolver`  
  - **ECB:** Control  
  - **체크포인트:** AC-FR05-1~5, BR-11·BR-12  

- [ ] **TASK-017**  
  - **단계:** RED  
  - **작업 제목:** `NO_SOLUTION`·`AMBIGUOUS_SOLUTION` 도메인 결과(코드만, 문구 없음)  
  - **Scenario Level:** L3  
  - **연결 Test:** `ResolveTwoPlacementsTest#tp03`, `#tp04`  
  - **연결 Code:** `ResolutionResult`, `MagicSquareResolver`  
  - **ECB:** Control  
  - **체크포인트:** TP-03·TP-04 Track B  

- [ ] **TASK-018**  
  - **단계:** GREEN  
  - **작업 제목:** TD-04 등으로 무해·모호 케이스 Track B Green  
  - **Scenario Level:** L3  
  - **연결 Test:** `ResolveTwoPlacementsTest`, `GoldenGridsTest`  
  - **연결 Code:** `MagicSquareResolver`, `GoldenGrids`  
  - **ECB:** Control  
  - **체크포인트:** DEC-01·DEC-02  

- [ ] **TASK-019**  
  - **단계:** REFACTOR  
  - **작업 제목:** Facade가 검증→`MagicSquareResolver`만 호출하도록 의존성·이름 정리  
  - **Scenario Level:** L0  
  - **연결 Test:** 통합 스위트 전체  
  - **연결 Code:** `MagicSquareFacade`, `MagicSquareResolver`  
  - **ECB:** Control  
  - **체크포인트:** §10.3 의존 방향  

---

## US-005 — 잘못된 입력·도메인 실패의 외부 계약 (Track A)

**스토리 완료 조건:** TP-01~TP-04에서 A측 메시지 전문·성공 시 `int[6]` 동등성.

### Phase 5 — 계약 통합

- [ ] **TASK-020**  
  - **단계:** RED  
  - **작업 제목:** 성공·`NO_SOLUTION`·`AMBIGUOUS_SOLUTION` Facade 계약 실패 테스트  
  - **Scenario Level:** L1 / L3  
  - **연결 Test:** `MagicSquareFacadeContractTest#tp01_tp04`  
  - **연결 Code:** `MagicSquareFacade`, `GridValidator`, `MagicSquareResolver`  
  - **ECB:** Boundary + Control  
  - **체크포인트:** §8.3 UX vs Logic 매핑  

- [ ] **TASK-021**  
  - **단계:** GREEN  
  - **작업 제목:** 도메인 실패 → BR-ERR-05·06·07 Boundary 매핑  
  - **Scenario Level:** L3  
  - **연결 Test:** `MagicSquareFacadeContractTest`  
  - **연결 Code:** `MagicSquareFacade`, `ErrorMessages`  
  - **ECB:** Boundary  
  - **체크포인트:** BR-ERR-05~07 전문 일치  

- [ ] **TASK-022**  
  - **단계:** REFACTOR  
  - **작업 제목:** 단일 `resolve` 진입·Result/예외 정책 통일  
  - **Scenario Level:** L2  
  - **연결 Test:** `MagicSquareFacadeContractTest`, `DeterminismTest#sameInputTwice`  
  - **연결 Code:** `MagicSquareFacade`  
  - **ECB:** Control  
  - **체크포인트:** NFR-03, P-05  

---

## US-006 — 테스트 커버리지 체크포인트·CI (NFR·§8.5)

**스토리 완료 조건:** NFR-01·02·06, DEC-06, §9.5 로그 접두사.

### Phase 6 — 품질 게이트

- [ ] **TASK-023**  
  - **단계:** RED  
  - **작업 제목:** Domain ≥95%·Boundary ≥85% 미달 시 빌드 실패(스크립트 또는 플러그인 설정)  
  - **Scenario Level:** L0  
  - **연결 Test:** CI `coverage` job (로컬에서 동일 명령 재현)  
  - **연결 Code:** `pom.xml` / `build.gradle.kts`, JaCoCo 설정  
  - **ECB:** Control (품질 게이트·빌드 조율)  
  - **체크포인트:** NFR-01·NFR-02  

- [ ] **TASK-024**  
  - **단계:** GREEN  
  - **작업 제목:** Job A(UX Contract)·Job B(Logic) 분리, 병합 조건 A∧B  
  - **Scenario Level:** L0  
  - **연결 Test:** CI 전체  
  - **연결 Code:** `.github/workflows/*.yml` (또는 동등 CI)  
  - **ECB:** Control  
  - **체크포인트:** §9.5 `[logic]` / `[ux-contract]` 접두사, DEC-06  

- [ ] **TASK-025**  
  - **단계:** REFACTOR  
  - **작업 제목:** ArchUnit 등 — Track A가 domain 패키지 직접 의존 금지  
  - **Scenario Level:** L2  
  - **연결 Test:** `ArchitectureTest#trackA_noDirectDomainImports`  
  - **연결 Code:** `src/test/.../ArchitectureTest.java`  
  - **ECB:** Boundary (경계 규칙을 테스트로 고정)  
  - **체크포인트:** §8.5.1·§8.9  

---

## Scenario Level 정의 (적용)

| Level | 의미 |
|-------|------|
| **L0** | 기능 개요·파이프라인·진입점 |
| **L1** | 정상 흐름(골든·성공 해) |
| **L2** | 경계(판정 false, 좌표 극단, 불변·복사) |
| **L3** | 실패(검증 거부·NO_SOLUTION·AMBIGUOUS) |

---

## ECB 역할 고정 (요청 제약 반영)

| 스테레오타입 | 책임 |
|--------------|------|
| **Entity** | 4×4 보드 상태·복사본·(필요 시) VO |
| **Boundary** | FR-01만; 표준 `errorCode`·**전체** `message`; UI/문자열은 여기서만 관측 계약 |
| **Control** | 검증 통과 후 빈칸·누락·판정·두 시도·결과 조합; **Facade + Domain 서비스/Resolver** |

**Logic과 UI 분리:** Logic(Track B) 테스트는 도메인 타입·코드·불변만; UX Contract(Track A)는 Facade·Boundary만 호출.

---

## Concept-to-Code 추적 한눈에

| PRD | Scenario | 대표 Test | Code |
|-----|----------|-------------|------|
| FR-01 | TP-05~08 | `MagicSquareFacadeContractTest`, `GridValidatorTest` | `GridValidator`, `Facade` |
| FR-02 | TP-01 데이터 | `EmptyCellLocatorTest` | `EmptyCellLocator` |
| FR-03 | TP-01 | `MissingNumberResolverTest` | `MissingNumberResolver` |
| FR-04 | TD-03 | `MagicSquareCompletenessCheckerTest` | `MagicSquareCompletenessChecker` |
| FR-05 | TP-01~04 | `ResolveTwoPlacementsTest`, `FacadeContract` | `MagicSquareResolver` |

---

**Reporter/04 참고:** IDE가 RED→GREEN→REFactor를 강제하지 않으므로, **태스크·PR 단위로 RED 범위를 잘라** 인간 루프로 집행하는 것이 안전합니다.

---

**User**

Reporter 폴더에  지금 작업한 내용을 보고서로 내보내줘.

---

**Cursor**

Reporter 폴더의 보고서 명명 규칙을 확인한 뒤, To-Do 구조 작업을 정리한 보고서를 작성합니다.



보고서 `Reporter/18_magic-square-implementation-todo-structure-export-report.md` 작성 중입니다.



다음 파일을 추가했습니다.

**경로:** `Reporter/18_magic-square-implementation-todo-structure-export-report.md`

**포함 내용:**
- 보내기 일자·작업 요약(구현용 To-Do 구조, 적용 방법론)
- 주·보조 소스(`docs/PRD_MagicSquare_4x4_TDD.md`, Reporter/02·03·04, PRD 경로 명 참고)
- **Epic-001** 및 **US-001~006** 완료 조건 요약
- **TASK-001~026** 인덱스 표(R/G/R, US, 제목, Scenario Level, ECB)
- L0~L3 정의, ECB·Dual-Track 요약, PRD↔Task 매핑 표
- `Reporter/17` 등 연계 문서
- 본문은 **전체 체크리스트의 복제본이 아니라** 인덱스·메타데이터 아카이브이며, 상세 항목은 채팅 산출을 원본으로 한다는 문구

전체 Task 블록을 같은 파일에 이어 붙이길 원하면 알려 주세요.

