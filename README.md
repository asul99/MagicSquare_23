# MagicSquare (4×4)

**4×4 부분 채움 격자**에서 빈칸 두 곳에 누락된 두 수를 규칙대로 배치해 **마방진 불변조건**(행·열·주·부대각선 합 34, 1~16 각 1회)을 만족하는지 판단하고, 성공 시 **1-index 좌표와 배치 값이 고정된 6원소 벡터**(`int[6]` / PRD의 논리 출력)로 표현한다. 목적은 알고리즘 난이도보다 **TDD·계약·불변조건을 테스트로 고정하는 훈련**이다.

**요구사항·검증의 단일 근거(SoT):** [`docs/PRD_MagicSquare_4x4_TDD.md`](docs/PRD_MagicSquare_4x4_TDD.md)

**구현 스택(본 저장소):** Python 3.10+, 패키지 `magic_square`, 테스트는 [`pyproject.toml`](pyproject.toml)의 pytest 설정과 루트 [`.cursorrules`](.cursorrules)의 ECB·TDD 규칙을 따른다. PRD 본문은 JVM·JUnit·JaCoCo 등 예시 표현을 포함할 수 있으나, **기능·오류 문구·AC는 PRD와 동일**하게 맞추고, 빌드·커버리지 도구는 Python 쪽 설정으로 대응하면 된다.

---

## 문서 맵

### Reporter (각 한 줄)

| 문서 | 역할 |
|------|------|
| [`Reporter/01_magic-square-problem-definition-report.md`](Reporter/01_magic-square-problem-definition-report.md) | 문제 인식·정의·훈련 맥락(구현·설계 전 단계). |
| [`Reporter/02_magic-square-clean-architecture-tdd-design-report.md`](Reporter/02_magic-square-clean-architecture-tdd-design-report.md) | Clean Architecture·Dual-Track·Boundary 계약·DA/UC·트레이서빌리티 골격. |
| [`Reporter/03_magic-square-cursorrules-tdd-rules-report.md`](Reporter/03_magic-square-cursorrules-tdd-rules-report.md) | Red–Green–Refactor 단계 품질 원칙(PR·에이전트 루프와 정합). |
| [`Reporter/04_magic-square-cursorrules-tdd-rules-review-report.md`](Reporter/04_magic-square-cursorrules-tdd-rules-review-report.md) | TDD 규칙 검토·PR 단위 RED 범위·자동 단계 전이 한계. |
| [`Reporter/05_magic-square-cursorrules-completion-report.md`](Reporter/05_magic-square-cursorrules-completion-report.md) | Cursor 규칙 완료·정리 산출 보고. |
| [`Reporter/06_magic-square-cursorrules-dual-track-mlops-expansion-report.md`](Reporter/06_magic-square-cursorrules-dual-track-mlops-expansion-report.md) | Dual-Track·MLOps 관점 규칙 확장 기록. |
| [`Reporter/07_magic-square-cursorrules-core-domain-ecb-report.md`](Reporter/07_magic-square-cursorrules-core-domain-ecb-report.md) | 핵심 도메인·ECB 규칙 기준선. |
| [`Reporter/08_magic-square-user-entity-ecb-implementation-report.md`](Reporter/08_magic-square-user-entity-ecb-implementation-report.md) | ECB `entity` 예시 구현·pytest·`pyproject.toml` 연계 작업 보고. |
| [`Reporter/09_magic-square-user-journey-epic-business-goal-report.md`](Reporter/09_magic-square-user-journey-epic-business-goal-report.md) | Epic·비즈니스 목표·Level 2 사용자 여정. |
| [`Reporter/10_magic-square-user-journey-epic-level2-export-report.md`](Reporter/10_magic-square-user-journey-epic-level2-export-report.md) | Level 2 여정보내기·상위 레벨과 정합. |
| [`Reporter/11_magic-square-user-journey-epic-level3-user-stories-report.md`](Reporter/11_magic-square-user-journey-epic-level3-user-stories-report.md) | Level 3 **User Story**(`As a` / 수용 기준). |
| [`Reporter/12_magic-square-user-journey-epic-level3-export-report.md`](Reporter/12_magic-square-user-journey-epic-level3-export-report.md) | Level 3보내기. |
| [`Reporter/12_magic-square-user-journey-epic-level4-technical-scenarios-report.md`](Reporter/12_magic-square-user-journey-epic-level4-technical-scenarios-report.md) | Level 4 기술 시나리오. |
| [`Reporter/13_magic-square-user-journey-epic-level4-export-report.md`](Reporter/13_magic-square-user-journey-epic-level4-export-report.md) | Level 4보내기. |
| [`Reporter/14_magic-square-user-journey-epic-level5-scenario-verification-report.md`](Reporter/14_magic-square-user-journey-epic-level5-scenario-verification-report.md) | Level 5 시나리오·검증. |
| [`Reporter/15_magic-square-user-journey-epic-level5-export-report.md`](Reporter/15_magic-square-user-journey-epic-level5-export-report.md) | Level 5보내기. |
| [`Reporter/16_magic-square-prd-export-report.md`](Reporter/16_magic-square-prd-export-report.md) | PRD 작성 산출·SoT 경로·근거 Reporter 요약. |
| [`Reporter/17_magic-square-prd-dual-track-mlops-alignment-report.md`](Reporter/17_magic-square-prd-dual-track-mlops-alignment-report.md) | PRD Dual-Track·§8·CI Job A/B·ArchUnit 권장과의 정렬. |
| [`Reporter/18_magic-square-implementation-todo-structure-export-report.md`](Reporter/18_magic-square-implementation-todo-structure-export-report.md) | Epic / US / TASK 인덱스·시나리오 레벨·ECB·PRD 매핑표. |
| [`Reporter/19_magic-square-readme-root-export-report.md`](Reporter/19_magic-square-readme-root-export-report.md) | 루트 `README.md` 작성·문서 맵·To-Do 이관 메타 보내기. |
| [`Reporter/20_magic-square-readme-todo-traceability-session-export-report.md`](Reporter/20_magic-square-readme-todo-traceability-session-export-report.md) | README·`Reporter/18`·추적 매트릭스(RTM) 정합·슬라이드 예시와 TASK ID 대응 보내기. |

PRD 서두의 근거 문서(01·02·03·04)와 [`Reporter/16`](Reporter/16_magic-square-prd-export-report.md)·[`Reporter/18`](Reporter/18_magic-square-implementation-todo-structure-export-report.md)의 교차 참조를 유지한다. **루트 README 작업 이력**은 [`Reporter/19`](Reporter/19_magic-square-readme-root-export-report.md), **체크리스트·요구사항 추적 표 세션 정리**는 [`Reporter/20`](Reporter/20_magic-square-readme-todo-traceability-session-export-report.md)을 병행한다.

### Prompt (`Reporter/17`~`20` 대응)

| 파일 | 역할 |
|------|------|
| [`Prompt/17_magic-square-prd-dual-track-mlops-alignment-report-Prompting.md`](Prompt/17_magic-square-prd-dual-track-mlops-alignment-report-Prompting.md) | Dual-Track·MLOps 정렬 보고서 재생성·검토용 프롬프트. |
| [`Prompt/18_magic-square-implementation-todo-structure-export-report-Prompting.md`](Prompt/18_magic-square-implementation-todo-structure-export-report-Prompting.md) | 구현 To-Do 구조 보고서 재생성·검토용 프롬프트. |
| [`Prompt/19_magic-square-readme-root-export-report-Prompting.md`](Prompt/19_magic-square-readme-root-export-report-Prompting.md) | 루트 README 보내기 보고서 재생성·검토용 프롬프트. |
| [`Prompt/20_magic-square-readme-todo-traceability-session-export-report-Prompting.md`](Prompt/20_magic-square-readme-todo-traceability-session-export-report-Prompting.md) | To-Do·추적 매트릭스 세션 보고서 재생성·검토용 프롬프트. |

---

## 스토리·에픽 (표현)

- **PRD:** 범위·FR-01~05·AC·§12 추적.
- **여정·스토리 서술:** [`Reporter/09`](Reporter/09_magic-square-user-journey-epic-business-goal-report.md)(Epic·목표), [`Reporter/11`](Reporter/11_magic-square-user-journey-epic-level3-user-stories-report.md)(User Story), 상위 레벨은 `Reporter/10`~`15` 시리즈.
- **구현용 식별자:** [`Reporter/18`](Reporter/18_magic-square-implementation-todo-structure-export-report.md)의 **Epic-001**, **US-001~006**와 아래 To-Do. 요약 **Task→FR→시나리오→테스트** 표는 [`Reporter/20`](Reporter/20_magic-square-readme-todo-traceability-session-export-report.md) §4.

---

## 오류·계약 요약 (상세는 PRD §6·FR 표)

Boundary 실패 시 **`errorCode` + 전문 `message` 문자열 전체 일치**가 PRD **BR-ERR-01~07** 및 FR-01 AC로 고정된다.

| 코드 | 메시지(전문 일치) |
|------|-------------------|
| `INVALID_GRID_SIZE` | `Grid must be 4x4.` |
| `INVALID_EMPTY_CELL_COUNT` | `Exactly two cells must be empty (value 0).` |
| `VALUE_OUT_OF_RANGE` | `Each cell must be 0 or an integer from 1 to 16.` |
| `DUPLICATE_NONZERO_VALUE` | `Non-zero values must not repeat.` |
| `NO_SOLUTION` | `No valid magic-square completion exists for this grid.` |
| `AMBIGUOUS_SOLUTION` | `Multiple valid orderings satisfy the rule; input is rejected.` |
| `DOMAIN_UNEXPECTED` | `An unexpected domain error occurred.` |

성공 시 **`[r1,c1,n1,r2,c2,n2]`**(1-index, `n1`/`n2`는 각 좌표에 배치된 값) 및 시도 1·2 규칙은 **PRD FR-05·§2.3 INV-C1~C5**가 근거다. 입력·레이어 분리·용어는 [`Reporter/02`](Reporter/02_magic-square-clean-architecture-tdd-design-report.md)와 PRD **§4·§8**을 병행한다.

---

## 검증 기준 (PRD 중심)

| 구분 | 기준(요지) | PRD 위치 |
|------|------------|-----------|
| 완성 정의 | INV-C1~C5 동시 만족·0 없는 완전 격자 | §2.3, FR-04 |
| 기능 | FR-01~05 및 각 AC | §5 |
| 오류 | 위 표 + FR-01 AC-FR01-6·7(도메인 미호출·격자 불변) | §6, FR-01 |
| 비기능 | NFR-01~06(커버리지·결정론·부작용·재현 빌드 등) | §7 |
| 추적 | Concept → … → Test → Component | §12, TP/TD 시나리오 |
| 듀얼 트랙 | Track A: 경계·Facade 계약 / Track B: 도메인 단위(도메인 테스트에서 사용자 메시지 전문 assert 금지 등) | §8, §8.4~8.5 |

시나리오 레벨(L0~L3) 정의는 [`Reporter/18`](Reporter/18_magic-square-implementation-todo-structure-export-report.md) §4.

---

## 실행 · ECB · TDD

**실행**

```bash
pip install -e ".[dev]"
pytest
```

- 테스트 경로·옵션: [`pyproject.toml`](pyproject.toml) `[tool.pytest.ini_options]` (`testpaths = ["tests"]`, `pythonpath = ["."]`).
- 패키지 발견: `include = ["magic_square*"]`, `requires-python = ">=3.10"`.

**ECB·TDD**

- 레이어·의존성·금지 사항·Red/Green/Refactor 단계: 루트 [`.cursorrules`](.cursorrules) (`architecture`, `tdd_rules`, `testing`).
- pytest, AAA, **entity → control → boundary** 테스트 우선순위, **커버리지 하한 80%**(`.cursorrules` `testing.coverage_minimum`). PRD **NFR-01·02**의 수치(95%/85%)는 제품 게이트로 두고, 저장소에서는 도구에 맞게 이중 기준을 문서화할 수 있다.
- Dual-Track·MLOps·Job A/B 아이디어: PRD §8.5, [`Reporter/06`](Reporter/06_magic-square-cursorrules-dual-track-mlops-expansion-report.md), [`Reporter/17`](Reporter/17_magic-square-prd-dual-track-mlops-alignment-report.md).

| ECB | 책임(요지) |
|-----|------------|
| **Entity** | 격자 상태·VO·복사·불변 |
| **Boundary** | FR-01, `errorCode`·전문 `message`, 비즈니스 “합 34” 규칙은 여기서 직접 구현하지 않음 |
| **Control** | 검증 통과 후 빈칸·누락·판정·두 시도·Facade 조율 |

---

## To-Do (구현 체크리스트)

아래는 [`Reporter/18`](Reporter/18_magic-square-implementation-todo-structure-export-report.md) **TASK-001~026**을 PRD·시나리오와 맞춘 체크리스트다. 완료 의미·테스트 이름·패키지 배치는 **PRD §10.4** 및 Reporter 18 본문을 따르며, 동일 목록·추적 매트릭스 요약은 [`Reporter/20`](Reporter/20_magic-square-readme-todo-traceability-session-export-report.md)에도 아카이브되어 있다.

### Epic-001 — Magic Square 4×4 완성 시스템

- [ ] **Epic-001** 완료: TP-01~08, FR-01~05 AC, NFR·Job A/B(또는 동등 분리)·§12 추적 ([`Reporter/18`](Reporter/18_magic-square-implementation-todo-structure-export-report.md) §2).

### US-001 — 보드 표현·골든 픽스처

- [ ] **TASK-001** (RED) Entity·TD 로더 실패 테스트 — L0 — Entity  
- [ ] **TASK-002** (GREEN) G0·TD-02 최소 구현 — L1 — Entity  
- [ ] **TASK-003** (REFACTOR) VO·스캔 순서 정리 — L2 — Entity  
- [ ] **TASK-026** (R→G→R) `TestGridBuilder` 등 보드 생성 헬퍼 — L1/L3 — Entity  

### US-002 — Boundary 보드 유효성 (FR-01)

- [ ] **TASK-004** (RED) Track B 검증 결과(코드만) — L3 — Boundary  
- [ ] **TASK-005** (RED) Track A Facade 계약 실패 테스트 — L3 — Boundary  
- [ ] **TASK-006** (GREEN) `GridValidator`·도메인 0회 호출 — L3 — Boundary / Control  
- [ ] **TASK-007** (REFACTOR) 오류 SoT 단일화 — L2 — Boundary  

### US-003 — 빈칸·누락·후보 (FR-02, FR-03)

- [ ] **TASK-008** (RED) 빈칸 row-major 결정성 — L1 — Control  
- [ ] **TASK-009** (GREEN) `EmptyCellLocator` — L1 — Control  
- [ ] **TASK-010** (RED) 누락 쌍·min/max 후보 — L1 — Control  
- [ ] **TASK-011** (GREEN) `MissingNumberResolver` — L1 — Control  
- [ ] **TASK-012** (REFACTOR) 시도용 복사·불변 — L2 — Entity  

### US-004 — 완성 판정·두 시도 (FR-04, FR-05)

- [ ] **TASK-013** (RED) FR-04 판정 실패 테스트 — L2 — Control  
- [ ] **TASK-014** (GREEN) FR-04 구현 — L2 — Control  
- [ ] **TASK-015** (RED) 두 시도·시도2 미호출·골든 — L1 — Control  
- [ ] **TASK-016** (GREEN) FR-05 구현 — L1 — Control  
- [ ] **TASK-017** (RED) NO_SOLUTION·AMBIGUOUS 도메인 결과 — L3 — Control  
- [ ] **TASK-018** (GREEN) TD-04 등 Track B — L3 — Control  
- [ ] **TASK-019** (REFACTOR) Facade–Resolver 의존성 정리 — L0 — Control  

### US-005 — 외부 계약 (성공 `int[6]` / 실패 코드·메시지)

- [ ] **TASK-020** (RED) Facade 성공·실패 계약 — L1/L3 — Boundary+Control  
- [ ] **TASK-021** (GREEN) BR-ERR 매핑 — L3 — Boundary  
- [ ] **TASK-022** (REFACTOR) 단일 resolve·결정론 — L2 — Control  

### US-006 — 커버리지·CI·품질 게이트

- [ ] **TASK-023** (RED) 커버리지 임계 실패(빌드) — L0 — Control  
- [ ] **TASK-024** (GREEN) Job A/B 분리·(JaCoCo 등) 커버리지 도구 연동 — L0 — Control  
- [ ] **TASK-025** (REFACTOR) ArchUnit·`domain` 직접 import 금지 등 아키텍처 게이트 — L2 — Boundary  

*(PRD §8.5.1의 “Track A에서 domain 직접 import 금지”는 Python 트리에서 동등 규칙·정적 검사로 옮긴다.)*

---

## 라이선스

저장소에 `LICENSE`가 없다면 조직 정책에 맞게 추가한다.
