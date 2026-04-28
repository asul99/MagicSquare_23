# Magic Square (4×4) 완성 시스템 — 구현용 To-Do 구조 보내기 보고서

**보내기 일자:** 2026-04-28  
**산출물 유형:** Reporter 폴더 아카이브용 **구현 To-Do 구조 설계** 작업 정리 보고서  
**관련 대화 산출:** 시니어 아키텍트·TDD 코치 역할로 요청받은 **Epic / User Story / Phase별 Task** 체계 및 식별자·추적 규칙 정의

---

## 1. 보내기 요약

| 구분 | 내용 |
|------|------|
| **작업명** | 「Magic Square 4×4 완성 시스템」**구현용 To-Do 구조** 작성 |
| **형식** | Markdown, 체크박스, 식별자 `Epic-001` / `US-001` / `TASK-001` … |
| **적용 방법론** | Concept-to-Code Traceability, Dual-Track UI + Logic TDD, To-Do → Scenario → Test → Code, ECB, RED → GREEN → REFACTOR |
| **주 소스** | `docs/PRD_MagicSquare_4x4_TDD.md` (FR-01~05, §6~§10, §12, §13, TP-01~08, TD-01~04, NFR, §8.5.1) |
| **보조 소스** | `Reporter/02`(계약·DA/UC·D-T), `Reporter/03`·`Reporter/04`(TDD 단계·PR 단위 루프), Cursor 규칙(대화 지침) |
| **명명 참고** | 요청 시 `docs/5.PRD_MagicSquare_4x4_TDD.md`로 기재되었으나, 저장소 SoT 파일명은 **`docs/PRD_MagicSquare_4x4_TDD.md`** |

**본 보고서의 범위:** To-Do **전문 본문의 대체 저장소는 아님**. 채팅 산출의 **구조·식별자·추적 표**를 Reporter에 고정하고, 반복 실행 시 PRD·본 보고서의 인덱스로 되돌아갈 수 있게 한다.

---

## 2. 에픽·스토리 골격

| ID | 제목 | 완료 조건(요지) |
|----|------|-----------------|
| **Epic-001** | Magic Square 4×4 완성 시스템 | TP-01~08, FR-01~05 AC, NFR-01·02(측정 시)·03·04, Job A·B Green, §12 추적 유지 |
| **US-001** | 보드 표현·보드 생성·골든 픽스처 | Entity·TD-01~04, NFR-04 불변 |
| **US-002** | Boundary 보드 유효성 검사 (FR-01) | TP-05~08, AC-FR01-6·7, Boundary에 합 34 규칙 없음 |
| **US-003** | 빈칸·누락·후보 공간 (FR-02, FR-03) | BR-05·06, P-01·P-02; 후보는 min/max 두 배치 |
| **US-004** | 완성 판정·두 시도 (FR-04, FR-05) | TP-01~04, INV-C1~C5, DEC-01~04 |
| **US-005** | 잘못된 입력·도메인 실패의 외부 계약 | Track A에서 `errorCode`+전문 `message`·성공 `int[6]` |
| **US-006** | 커버리지·CI·품질 게이트 | NFR-01·02·06, DEC-06, §9.5 로그 접두사 |

---

## 3. Task 인덱스 (TASK-001 ~ TASK-026)

| Task ID | R/G/R | US | 작업 제목(한 줄) | Scenario | ECB(주) |
|---------|-------|-----|------------------|----------|---------|
| TASK-001 | RED | US-001 | Entity·TD 로더 실패 테스트 | L0 | Entity |
| TASK-002 | GREEN | US-001 | G0·TD-02 최소 구현 | L1 | Entity |
| TASK-003 | REFACTOR | US-001 | VO·스캔 순서 정리 | L2 | Entity |
| TASK-026 | R→G→R | US-001 | `TestGridBuilder` 등 보드 생성 헬퍼 | L1/L3 | Entity |
| TASK-004 | RED | US-002 | Track B 검증 결과(코드만) | L3 | Boundary |
| TASK-005 | RED | US-002 | Track A Facade 계약 실패 테스트 | L3 | Boundary |
| TASK-006 | GREEN | US-002 | `GridValidator`·도메인 0회 호출 | L3 | Boundary / Control |
| TASK-007 | REFACTOR | US-002 | 오류 SoT 단일화 | L2 | Boundary |
| TASK-008 | RED | US-003 | 빈칸 row-major 결정성 | L1 | Control |
| TASK-009 | GREEN | US-003 | `EmptyCellLocator` | L1 | Control |
| TASK-010 | RED | US-003 | 누락 쌍·min/max 후보 | L1 | Control |
| TASK-011 | GREEN | US-003 | `MissingNumberResolver` | L1 | Control |
| TASK-012 | REFACTOR | US-003 | 시도용 복사·불변 | L2 | Entity |
| TASK-013 | RED | US-004 | FR-04 판정 실패 테스트 | L2 | Control |
| TASK-014 | GREEN | US-004 | FR-04 구현 | L2 | Control |
| TASK-015 | RED | US-004 | 두 시도·시도2 미호출·골든 | L1 | Control |
| TASK-016 | GREEN | US-004 | FR-05 구현 | L1 | Control |
| TASK-017 | RED | US-004 | NO_SOLUTION·AMBIGUOUS 도메인 결과 | L3 | Control |
| TASK-018 | GREEN | US-004 | TD-04 등 Track B | L3 | Control |
| TASK-019 | REFACTOR | US-004 | Facade–Resolver 의존성 정리 | L0 | Control |
| TASK-020 | RED | US-005 | Facade 성공·실패 계약 | L1/L3 | Boundary+Control |
| TASK-021 | GREEN | US-005 | BR-ERR 매핑 | L3 | Boundary |
| TASK-022 | REFACTOR | US-005 | 단일 resolve·결정론 | L2 | Control |
| TASK-023 | RED | US-006 | 커버리지 임계 실패(빌드) | L0 | Control |
| TASK-024 | GREEN | US-006 | Job A/B 분리·JaCoCo | L0 | Control |
| TASK-025 | REFACTOR | US-006 | ArchUnit·domain 직접 import 금지 | L2 | Boundary |

**연결 Test·Code 명명**은 채팅 산출에 따라 예시로 고정함: `GoldenGridsTest`, `GridValidatorTest`, `MagicSquareFacadeContractTest`, `EmptyCellLocatorTest`, `MissingNumberResolverTest`, `MagicSquareCompletenessCheckerTest`, `ResolveTwoPlacementsTest`, `ArchitectureTest` 등. 실제 패키지는 PRD **§10.4** 권장(`domain` / `boundary` / `application`)에 맞출 것.

---

## 4. Scenario Level 정의 (보내기 시 합의)

| Level | 의미 |
|-------|------|
| **L0** | 기능 개요·진입점·CI 게이트 |
| **L1** | 정상 흐름·골든 성공 |
| **L2** | 경계·판정 false·불변·복사 |
| **L3** | 실패·검증 거부·NO_SOLUTION·AMBIGUOUS |

---

## 5. ECB·Dual-Track 정리

| 스테레오타입 | 책임(요청 제약 반영) |
|--------------|----------------------|
| **Entity** | 4×4 보드 상태·복사·VO |
| **Boundary** | FR-01; `errorCode`·전문 `message`; 비즈니스 합 34 규칙 **비포함** |
| **Control** | 검증 통과 후 빈칸·누락·판정·두 시도·Facade 조율 |

- **Track A:** Facade·Boundary 계약 테스트; `**/domain/**` 직접 import 금지(§8.5.1).  
- **Track B:** 도메인 단위; 사용자 메시지 전문 assert 금지(§8.4).

---

## 6. PRD·시나리오 추적 표 (요약)

| PRD | PRD 시나리오(예) | Task 군 |
|-----|-------------------|---------|
| FR-01 | TP-05~08 | TASK-004~007 |
| FR-02 | TP-01 데이터 | TASK-008~009 |
| FR-03 | TP-01 | TASK-010~011 |
| FR-04 | TD-03, D-T14~15 | TASK-013~014 |
| FR-05 | TP-01~04 | TASK-015~018 |
| §7 NFR | CI | TASK-023~025 |

---

## 7. Reporter 연계

| 문서 | 본 To-Do 구조에서의 역할 |
|------|-------------------------|
| `Reporter/17_magic-square-prd-dual-track-mlops-alignment-report.md` | PRD v1.2·§8 보강 이력; CI Job A/B·ArchUnit 권장과 TASK-024·025 정합 |
| `Reporter/02_magic-square-clean-architecture-tdd-design-report.md` | Entity/VO/DA-01~06, D-T01~15, Boundary 계약 |
| `Reporter/03_magic-square-cursorrules-tdd-rules-report.md` | RED/GREEN/REFACTOR 단계 조건 |
| `Reporter/04_magic-square-cursorrules-tdd-rules-review-report.md` | PR·태스크 단위 RED 범위 — 에이전트 자동 단계 전이 한계 |

---

## 8. 문서 이력

| 항목 | 내용 |
|------|------|
| 보고서 위치 | `Reporter/18_magic-square-implementation-todo-structure-export-report.md` |
| PRD SoT | `docs/PRD_MagicSquare_4x4_TDD.md` |
| 성격 | 구현용 To-Do **구조·인덱스·방법론**의 Reporter보내기; **체크리스트 전문**은 채팅 산출을 원본으로 하고 필요 시 별도 `docs/` 또는 이슈 트래커로 이관 가능 |

---

**문서 끝**
