# Magic Square (4×4) — README·To-Do·추적 매트릭스 보내기 보고서

**보내기 일자:** 2026-04-28  
**산출물 유형:** Reporter 폴더 아카이브용 **구현 체크리스트·Requirements 추적 매트릭스(RT M) 정합** 작업 정리 보고서  
**관련 대화 산출:** `README.md`와 교육용 슬라이드(체크박스·단계별 번호·Task→Req→Scenario→Test)를 참고해 **Epic / US / TASK** To-Do 목록을 재구성하고, 본 저장소 식별자(`Reporter/18`)와의 대응 관계를 명시한 세션

---

## 1. 보내기 요약

| 구분 | 내용 |
|------|------|
| **작업명** | README §「To-Do」·`Reporter/18`·PRD를 단일 축으로 두고, 슬라이드 형식(계층 체크박스 + RTM)에 맞춘 **실행용 To-Do·추적 표**보내기 |
| **주 소스** | 저장소 루트 [`README.md`](../README.md) — Epic-001, US-001~006, TASK-001~026 체크리스트 |
| **구조·인덱스 SoT** | [`Reporter/18_magic-square-implementation-todo-structure-export-report.md`](18_magic-square-implementation-todo-structure-export-report.md) — TASK 표·시나리오 레벨·ECB·PRD §6 매핑 |
| **요구사항 SoT** | [`docs/PRD_MagicSquare_4x4_TDD.md`](../docs/PRD_MagicSquare_4x4_TDD.md) |
| **참고 UI(개념)** | 세션 첨부 슬라이드 「1.3 체크박스·단계별 번호·Requirements 추적 체계」— Epic→US→Task→(RED/GREEN/REFACTOR) 및 RTM 표 형식; **슬라이드 내 예시 TASK 번호는 본 프로젝트 TASK-001~026과 동일하지 않을 수 있음** (아래 §2) |

**본 보고서의 범위:** 채팅에서 확정한 **체크리스트 본문·요약 RTM**을 Reporter에 고정한다. TASK별 세부 테스트 클래스명·파일 경로의 **최종 SoT**는 PRD **§10.4** 및 구현 진행에 따른다.

---

## 2. 슬라이드 예시와 본 저장소 식별자 정합

교육 슬라이드에는 예시로 **합 검증(`SquareValidator` / `is_valid`)**, **빈칸 탐색(`MissingFinder`, N-Queen 선택)** 등이 등장할 수 있다. 본 저장소의 공식 구현 단위는 `Reporter/18` 및 README와 같다.

| 슬라이드 개념 | 본 저장소 대응(요지) |
|----------------|----------------------|
| 격자·엔티티 정의 | **US-001**, TASK-001~003, TASK-026 — Entity·골든·TD |
| 경계/격자 유효성(합 34는 Boundary 비포함) | **US-002**, TASK-004~007 — `GridValidator` 등 FR-01 |
| 빈칸·누락 수·후보 | **US-003**, TASK-008~012 — `EmptyCellLocator`, `MissingNumberResolver`(PRD 후보 규칙; 슬라이드의 N-Queen은 **선택 알고리즘 예시**에 해당할 수 있음) |
| 완성 판정·해 탐색 | **US-004**, TASK-013~019 — FR-04·FR-05 |
| 외부 계약·오류 매핑 | **US-005**, TASK-020~022 |
| CI·커버리지·아키텍처 게이트 | **US-006**, TASK-023~025 |

**원칙:** 체크박스·진행률은 **`TASK-001`~`TASK-026`** 번호로만 추적한다.

---

## 3. 체크박스·단계별 번호 (Epic → User Story → Task)

### Epic-001 — Magic Square 4×4 완성 시스템

- [ ] **Epic-001** 완료: TP-01~08, FR-01~05 AC, NFR·Job A/B(또는 동등)·§12 추적 (`Reporter/18` §2)

#### US-001 — 보드 표현·골든 픽스처

- [ ] **TASK-001** (RED) Entity·TD 로더 실패 테스트 — L0 — Entity  
- [ ] **TASK-002** (GREEN) G0·TD-02 최소 구현 — L1 — Entity  
- [ ] **TASK-003** (REFACTOR) VO·스캔 순서 정리 — L2 — Entity  
- [ ] **TASK-026** (R→G→R) `TestGridBuilder` 등 보드 생성 헬퍼 — L1/L3 — Entity  

#### US-002 — Boundary 보드 유효성 (FR-01)

- [ ] **TASK-004** (RED) Track B 검증 결과(코드만) — L3 — Boundary  
- [ ] **TASK-005** (RED) Track A Facade 계약 실패 테스트 — L3 — Boundary  
- [ ] **TASK-006** (GREEN) `GridValidator`·도메인 0회 호출 — L3 — Boundary / Control  
- [ ] **TASK-007** (REFACTOR) 오류 SoT 단일화 — L2 — Boundary  

#### US-003 — 빈칸·누락·후보 (FR-02, FR-03)

- [ ] **TASK-008** (RED) 빈칸 row-major 결정성 — L1 — Control  
- [ ] **TASK-009** (GREEN) `EmptyCellLocator` — L1 — Control  
- [ ] **TASK-010** (RED) 누락 쌍·min/max 후보 — L1 — Control  
- [ ] **TASK-011** (GREEN) `MissingNumberResolver` — L1 — Control  
- [ ] **TASK-012** (REFACTOR) 시도용 복사·불변 — L2 — Entity  

#### US-004 — 완성 판정·두 시도 (FR-04, FR-05)

- [ ] **TASK-013** (RED) FR-04 판정 실패 테스트 — L2 — Control  
- [ ] **TASK-014** (GREEN) FR-04 구현 — L2 — Control  
- [ ] **TASK-015** (RED) 두 시도·시도2 미호출·골든 — L1 — Control  
- [ ] **TASK-016** (GREEN) FR-05 구현 — L1 — Control  
- [ ] **TASK-017** (RED) NO_SOLUTION·AMBIGUOUS 도메인 결과 — L3 — Control  
- [ ] **TASK-018** (GREEN) TD-04 등 Track B — L3 — Control  
- [ ] **TASK-019** (REFACTOR) Facade–Resolver 의존성 정리 — L0 — Control  

#### US-005 — 외부 계약 (성공 `int[6]` / 실패 코드·메시지)

- [ ] **TASK-020** (RED) Facade 성공·실패 계약 — L1/L3 — Boundary+Control  
- [ ] **TASK-021** (GREEN) BR-ERR 매핑 — L3 — Boundary  
- [ ] **TASK-022** (REFACTOR) 단일 resolve·결정론 — L2 — Control  

#### US-006 — 커버리지·CI·품질 게이트

- [ ] **TASK-023** (RED) 커버리지 임계 실패(빌드) — L0 — Control  
- [ ] **TASK-024** (GREEN) Job A/B 분리·커버리지 도구 연동 — L0 — Control  
- [ ] **TASK-025** (REFACTOR) ArchUnit·`domain` 직접 import 금지 등 아키텍처 게이트 — L2 — Boundary  

---

## 4. Requirements 추적 매트릭스 (요약)

**추적성:** Task → Req(PR FR / TP) → Scenario(L0~L3) → Test → 상태. Concept-to-Code Traceability 실천 형식으로, 세션에서 제시한 표를 **US·FR 군** 단위로 압축했다.

| Task 군 | Req ID (PRD) | Scenario | 테스트(예시·`Reporter/18` §3) | 상태 |
|:--------|:-------------|:---------|:------------------------------|:-----|
| TASK-001~003, 026 | TD·FR 보조 | L0~L3 | `GoldenGridsTest` 등 Entity/TD | ⬜ TODO |
| TASK-004~007 | FR-01, TP-05~08 | L2~L3 | `GridValidatorTest`, Facade 계약 | ⬜ TODO |
| TASK-008~012 | FR-02, FR-03, TP-01 | L1~L2 | `EmptyCellLocatorTest`, `MissingNumberResolverTest` | ⬜ TODO |
| TASK-013~019 | FR-04, FR-05, TD-03·04 | L1~L3 | Completeness/Resolve/Track B | ⬜ TODO |
| TASK-020~022 | FR-01·05·BR-ERR | L1~L3 | `MagicSquareFacadeContractTest` | ⬜ TODO |
| TASK-023~025 | NFR-01·02·06, §8.5 | L0~L2 | Coverage CI, `ArchitectureTest` | ⬜ TODO |

**상태 열:** 세션 시점에는 구현 저장소에 **고정 완료 TASK가 없음**으로 두었으며, 실제 PR·커밋 진행에 따라 ✅/🔴 등으로 갱신한다.

`Reporter/18` §6의 **FR ↔ Task 군** 요약 표와 1:1 대응한다.

---

## 5. 실행·교차 참조

**로컬 검증(README와 동일):**

```bash
pip install -e ".[dev]"
pytest
```

| 문서 | 본 보고서와의 관계 |
|------|-------------------|
| `README.md` | 동일 체크리스트의 루트 노출; SoT 문장·오류 표·검증 기준 |
| `Reporter/18` | TASK 인덱스·시나리오 레벨·ECB·예시 테스트명 |
| `Reporter/19` | 루트 README 작성 메타(본 세션과 별도 작업) |
| `docs/PRD_MagicSquare_4x4_TDD.md` | FR·AC·NFR·§12·§10.4 패키지 권장 |

---

## 6. 후속 권장(선택)

- 루트 `README.md` **문서 맵** 표에 본 파일 `Reporter/20_...` 한 줄을 추가하면 아카이브 탐색이 쉬워진다.  
- TASK 완료 시 **§4 상태 열**만 갱신해도 RTM으로 활용 가능하다.

---

## 7. 변경 이력(Reporter)

| 일자 | 내용 |
|------|------|
| 2026-04-28 | 초안: README·18·세션 슬라이드 정합 To-Do 및 요약 RTM 보내기 |
