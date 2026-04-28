# Magic Square (4×4) TDD 연습 — PRD 작성 산출물 보내기 보고서

**보내기 일자:** 2026-04-28  
**산출물 유형:** Reporter 폴더 공유·아카이브용 **PRD 작성 작업** 정리 보고서  
**원본 PRD 위치:** `docs/PRD_MagicSquare_4x4_TDD.md` (본 보고서의 단일 제품 요구사항 SoT)

---

## 1. 보내기 요약

| 구분 | 내용 |
|------|------|
| **작업명** | Magic Square (4×4) TDD 연습용 **제품 요구사항 문서(PRD)** 작성 |
| **저장 위치** | `docs/PRD_MagicSquare_4x4_TDD.md` |
| **문서 버전** | PRD 본문 이력: 1.0 (2026-04-28) |
| **제외 사항** | 구현 소스 코드, UI·DB 구현 명세, N×N 일반화 **요구** (PRD Out-of-Scope로 명시) |
| **근거 Reporter** | `Reporter/01`(문제·동기), `Reporter/02`(계약·Dual-Track·에러·트레이서빌리티), `Reporter/03`(TDD 단계), `Reporter/04`(tdd_rules 검토 관점) |

---

## 2. 작성 목적 및 범위

**목적:** 알고리즘 난이도보다 **TDD·불변조건·입출력 계약 고정** 훈련을 전제로, UI·DB·Web 없이 **Boundary + Domain** 중심 구현이 가능하도록 요구사항을 **검증 가능한 문장**으로 한곳에 모은다.

**범위:** 4×4 `int[][]` 입력(0은 빈칸, 빈칸 정확히 2개, 값 0 또는 1~16, 0 제외 중복 없음), row-major 첫·둘째 빈칸, 출력 `int[6]` 1-index `[r1,c1,n1,r2,c2,n2]`, 시도 1(작은 수→첫 빈칸)·시도 2(실패 시 큰 수→첫 빈칸, 성공 시 `n1,n2` 역순), 마법 상수 34, 실패·모호 시 **고정 `errorCode`·`message`**.

---

## 3. PRD 본문 구조 (목차 대응)

PRD는 아래 **12개 절**을 포함하며, Dual-Track(경계/도메인) 분리와 **Concept → Rule → Use Case → Contract → Test → Component** 추적은 **§12 Traceability Matrix**로 고정한다.

| 절 | 제목 |
|----|------|
| 1 | Executive Summary |
| 2 | Problem Statement |
| 3 | Target Users |
| 4 | Scope (In / Out) |
| 5 | Functional Requirements (FR-01 ~ FR-05) |
| 6 | Business Rules (BR-01 ~ BR-12, BR-ERR-01 ~ 07) |
| 7 | Non-Functional Requirements (커버리지, 결정론, 부작용 금지, 선택 성능) |
| 8 | Dual-Track TDD Strategy (Track A/B, 병렬 진행 규칙) |
| 9 | Test Plan (시나리오, 회귀, 테스트 데이터, Property) |
| 10 | Architecture Overview |
| 11 | Risks & Ambiguities (DEC-01 ~ DEC-05) |
| 12 | Traceability Matrix |

---

## 4. 기능·식별자 요약 (FR / 핵심 결정)

| ID | 요약 |
|----|------|
| FR-01 | Boundary 입력 검증; 실패 시 도메인 미호출; 원본 배열 불변 |
| FR-02 | row-major 두 빈칸 1-index 좌표 |
| FR-03 | 누락 숫자 2개 산출 |
| FR-04 | 완전 격자 마방진 판정(합 34, 1~16 순열) |
| FR-05 | 두 조합 시도 후 `int[6]` 또는 `NO_SOLUTION` / `AMBIGUOUS_SOLUTION` |

| 결정 ID | 요약 |
|---------|------|
| DEC-01 | 두 시도 모두 실패 → `NO_SOLUTION` + 고정 메시지 |
| DEC-02 | 두 시도 모두 성공 → `AMBIGUOUS_SOLUTION` + 고정 메시지 |
| DEC-03 | 시도 1 성공 시 시도 2 미실행 |
| DEC-04 | 시도 2 성공 시 `n1`=큰 수, `n2`=작은 수(좌표 순서는 FR-02와 동일) |
| DEC-05 | 호출자 `int[][]` 불변(NFR-04와 정합) |

에러 코드·문장 전문은 PRD **§6** 및 `Reporter/02` §2.4와 동일 계열로 맞춰 두었다.

---

## 5. 품질·개발 원칙 연계 (Report/3·4)

| 출처 | PRD 반영 |
|------|-----------|
| `Reporter/03` | Red–Green–Refactor: 실패 우선 테스트, Green은 최소 변경, Refactor는 관측 동작 불변·커버리지 약화 금지(측정 시) |
| `Reporter/04` | 단계 전이는 IDE가 강제하지 않으므로 **짧은 루프·PR 단위**로 Dual-Track RED→GREEN→REFACTOR를 인간이 집행한다는 주의 |

---

## 6. 추적성 (Reporter ↔ PRD)

| Reporter 문서 | PRD에서의 역할 |
|----------------|----------------|
| `01_magic-square-problem-definition-report.md` | §2 문제 정의, 불변·계약 중요성 서술 |
| `02_magic-square-clean-architecture-tdd-design-report.md` | FR/BR/에러 스키마, INV 개념, Dual-Track·테스트 ID 정합 |
| `03_magic-square-cursorrules-tdd-rules-report.md` | §7 품질·§8.3 진행 규칙 |
| `04_magic-square-cursorrules-tdd-rules-review-report.md` | 문서 메타·에이전트 한계 인지(구조 골격) |

---

## 7. 다음 작업 제안 (본 보고서 범위 밖)

PRD는 **구현을 요구하지 않는다.** 구현 착수 시에는 PRD **§5 AC**, **§9 Test Plan**, **§12 매트릭스**를 테스트 코드 ID와 1:1로 매핑하는 것을 권장한다.

---

## 8. 문서 이력

| 항목 | 내용 |
|------|------|
| 보고서 위치 | `Reporter/16_magic-square-prd-export-report.md` |
| PRD 위치 | `docs/PRD_MagicSquare_4x4_TDD.md` |
| 성격 | PRD 작성 작업의 **Reporter보내기(인덱스·요약)**; PRD 전문의 대체 본문 아님 |

---

**문서 끝**
