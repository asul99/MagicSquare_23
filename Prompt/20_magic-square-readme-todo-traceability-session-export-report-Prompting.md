# 요구사항 추적 시스템
_Exported on 4/28/2026 at 10:58:08 GMT+9 from Cursor (3.2.11)_

---

**User**

@README.md 첨부한 파일 참조하여 To-Do list를 작성해줘.

---

**Cursor**

README.md를 읽어 프로젝트 맥락에 맞춘 To-Do 목록을 작성합니다.



Reporter/18에서 REQ·시나리오 매핑을 확인해 추적 매트릭스를 정확히 맞춥니다.



[`README.md`](c:\DEV\MagicSquare_23\README.md)의 To-Do 구간(106–157행)과 [`Reporter/18`](c:\DEV\MagicSquare_23\Reporter\18_magic-square-implementation-todo-structure-export-report.md) 인덱스를 기준으로, 첨부 슬라이드의 **체크박스·단계 번호·Task→Req→Scenario→Test** 형식을 맞춰 정리했습니다.

**참고:** 슬라이드의 예시(TASK-002 = `SquareValidator`, TASK-003 = N-Queen `MissingFinder`)는 **개념용**이고, 이 저장소의 공식 식별자는 README·Reporter/18의 **TASK-001~026 / US-001~006**입니다. 아래 목록은 README·18을 SoT로 따릅니다.

---

## 1. 체크박스 · 단계별 번호 (Epic → User Story → Task)

### Epic-001 — Magic Square 4×4 완성 시스템

- [ ] **Epic-001** 완료: TP-01~08, FR-01~05 AC, NFR·Job A/B(또는 동등)·§12 추적 ([Reporter/18 §2](c:\DEV\MagicSquare_23\Reporter\18_magic-square-implementation-todo-structure-export-report.md))

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

## 2. Requirements 추적 매트릭스 (요약)

**추적성:** Task → Req(PR FR/TP) → Scenario(L0~L3) → Test → 상태. (C2C Traceability 실천)

| Task ID | Req ID (PRD) | Scenario | 테스트(예시·Reporter/18) | 상태 |
|:--------|:-------------|:---------|:-------------------------|:-----|
| TASK-001~003, 026 | FR 보조·TD | L0~L3 | `GoldenGridsTest` 등 Entity/TD | ⬜ TODO |
| TASK-004~007 | FR-01, TP-05~08 | L2~L3 | `GridValidatorTest`, Facade 계약 | ⬜ TODO |
| TASK-008~012 | FR-02, FR-03, TP-01 | L1~L2 | `EmptyCellLocatorTest`, `MissingNumberResolverTest` | ⬜ TODO |
| TASK-013~019 | FR-04, FR-05, TD-03·04 | L1~L3 | Completeness/Resolve/Track B | ⬜ TODO |
| TASK-020~022 | FR-01·05·BR-ERR | L1~L3 | `MagicSquareFacadeContractTest` | ⬜ TODO |
| TASK-023~025 | NFR-01·02·06, §8.5 | L0~L2 | Coverage CI, `ArchitectureTest` | ⬜ TODO |

실제 테스트 클래스명·파일 배치는 PRD **§10.4**와 구현 진행에 맞춰 위 예시를 바꿔도 됩니다.

---

## 3. 실행·검증 (README와 동일)

```bash
pip install -e ".[dev]"
pytest
```

상세 오류 코드·메시지는 README **오류·계약 요약** 표, 검증 기준은 PRD·Reporter/18을 따르면 됩니다.

원하면 이 블록을 `README.md`의 To-Do 절 아래에 **한국어 제목 버전**으로 붙여 넣는 패치까지 해 줄 수 있습니다.

---

**User**

Reporter 폴더에  지금 작업한 내용을 보고서로 내보내줘.

---

**Cursor**

기존 Reporter 보고서 형식을 확인한 뒤 새 보고서를 작성합니다.



Reporter에 `20`번 보고서를 추가합니다. 대화에서 정리한 README·슬라이드·Reporter/18 정합 To-Do와 추적 매트릭스를 아카이브합니다.



다음 파일을 추가해 두었습니다.

**[`Reporter/20_magic-square-readme-todo-traceability-session-export-report.md`](c:\DEV\MagicSquare_23\Reporter\20_magic-square-readme-todo-traceability-session-export-report.md)**

포함 내용은 다음과 같습니다.

1. **보내기 요약** — 작업명, `README.md` / `Reporter/18` / PRD / 슬라이드 역할  
2. **슬라이드 vs 저장소 TASK** — 교육용 예시(`SquareValidator`, N-Queen 등)와 US-001~006·TASK-001~026 대응 표  
3. **§3** — Epic → US → Task 체크리스트 전문(README와 동일 식별자)  
4. **§4** — Task 군 × FR × L0~L3 × 예시 테스트명 × 상태(요약 RTM)  
5. **§5~7** — 실행 명령, 교차 참조, 선택적 후속(README 문서 맵에 20번 한 줄 추가)

번호는 기존 `19_magic-square-readme-root-export-report.md` 다음인 **20**을 사용했습니다. README 문서 맵에 이 보고서 한 줄을 넣고 싶으면 말해 주면 그에 맞춰 수정하겠습니다.

