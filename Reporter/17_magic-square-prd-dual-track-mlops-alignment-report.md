# Magic Square (4×4) PRD — Dual-Track UI + Logic TDD · MLOps 정합 및 보완 작업 보고서

**작성 일자:** 2026-04-28  
**산출물 유형:** `docs/PRD_MagicSquare_4x4_TDD.md`에 대한 **방법론 정합·구멍 보완** 작업의 Reporter 아카이브  
**대상 PRD:** `docs/PRD_MagicSquare_4x4_TDD.md` (문서 이력 기준 **버전 1.2**)

---

## 1. 작업 요약

| 항목 | 내용 |
|------|------|
| **배경** | 사용자 요청에 따라 PRD를 **Dual-Track UI + Logic TDD with MLOps** 관점에 맞추고, 이후 **부족한 부분 보완**을 반복 반영했다. |
| **주요 결과** | PRD 제목·메타·§1·§4·§7~§13까지 확장; 완성 불변조건 **§2.3(INV-C1~C5)** 단일화; §8을 MLOps·계약·RACI·DoD·안티패턴까지 포함하는 **운영 가능한 가이드**로 보강했다. |
| **현재 PRD 버전** | **1.2** (2026-04-28) — Dual-Track 열·NFR-06·§13 Glossary·DEC-06 등 포함. |
| **선행 보고서와의 관계** | `Reporter/16_magic-square-prd-export-report.md`는 PRD **1.0** 시점 인덱스이다. 본 보고서는 **1.1~1.2** 구간 변경을 정리한다. |
| **연계 Reporter** | `Reporter/06_magic-square-cursorrules-dual-track-mlops-expansion-report.md`(방법론·.cursorrules 확장), `Reporter/02_magic-square-clean-architecture-tdd-design-report.md`(계약·레이어), `Reporter/16_magic-square-prd-export-report.md`(PRD 초기 export). |

---

## 2. 사용자 요청 대응 매핑

| 대화 단계 | 사용자 요청(요지) | PRD·문서 반영 |
|-----------|-------------------|----------------|
| 1 | Dual-Track UI + Logic TDD with MLOps에 대한 의견 | 방법론을 PRD 상단·§8에 **명문화**(UX Contract / Logic Rule, 독립성, CI 단계). |
| 2 | “Dual-Track UI + Logic TDD with MLOps 로 맞춰줘” | 제목·Executive Summary·§4 Out-of-Scope 정리·§8 전면 개편·§9·§10·§12 Dual-Track 문구. |
| 3 | “부족한 부분을 보완해서 PRD 업데이트” | §2.3, NFR-06, §8.5.1~8.10, §9.1 Dual-Track 열·§9.5, §10.4, DEC-06, §12 열·추적 정리, §13, 오류 참조·오타 수정. |

---

## 3. PRD 변경 내역 (절별)

### 3.1 메타·요약·문제 정의

- **제목:** `Magic Square (4×4) · Dual-Track UI + Logic TDD (MLOps 정합)`으로 변경; 방법론·범위(상용 UI vs UX Contract 테스트) 명시.
- **§1 Executive Summary:** Dual-Track·MLOps·**§2.3·§13** 교차 참조 문장 추가.
- **§2.1:** “완성” 정의를 외부 INV 번호 대신 **§2.3** 참조로 통일.
- **§2.3 (신설):** 완성 격자 불변조건 **INV-C1~C5** 표 — FR-04·BR-07·BR-08과 정합.

### 3.2 사용자·범위

- **§3:** CI에서 Job A/B 분리, UI 트랙을 계약 테스트로 수행 가능함을 명시.
- **§4.2:** 상용 UI는 Out-of-Scope이나 **UX Contract 테스트**는 In-Scope임을 구분.

### 3.3 기능·규칙

- **FR-01 오류 정책:** 잘못된 “§8.1” 참조를 **§6 BR-ERR** 근거로 수정.
- **FR-04 처리 규칙:** §2.3 INV-C1~C5 및 0 없는 1~16 입력과 명시적으로 연결.

### 3.4 비기능

- **NFR-06 (신설):** 재현 가능 빌드(CI JDK·빌드 도구 고정).
- **§8.5 품질 게이트:** NFR-06 포함.

### 3.5 §8 Dual-Track · MLOps (핵심 확장)

| 소절 | 내용 |
|------|------|
| 8.1~8.4 | 기존 원리·언어 표·3단 매핑·Track A/B 가이드 유지·정돈. |
| 8.5 | MLOps 표 + 비결정론 확장 시 주의. |
| **8.5.1** | CI 잡·아티팩트·병렬·병합 조건·`domain` 직접 import 금지 등 **체크리스트**. |
| **8.6** | 외부 JSON 성공/실패 스키마 예시; 로그 시 격자 노출 자제. |
| **8.7** | RACI 요약(`errorCode`, `message`, 골든 데이터, CI 분리). |
| **8.8** | Track A/B 및 병합 Definition of Done. |
| **8.9** | 금지 의존성·안티패턴 표. |
| **8.10** | 병렬 인간 루프(기존 §8.6 내용, 번호만 조정). |

### 3.6 §9 테스트 플랜

- **§9.1:** 시나리오 표에 **Dual-Track** 열(`B`, `A+B` 등) 및 필수 검증 트랙 설명.
- **§9.5 (신설):** CI 실행 순서·로그 접두사·스모크 권장.

### 3.7 §10 아키텍처

- **§10.1:** Boundary/Domain/Application 설명에 Dual-Track·Facade 역할 보강(기존 보완 유지).
- **§10.4 (신설):** 테스트·소스 레이아웃 권장 표.

### 3.8 §11 리스크·결정

- **DEC-06 (신설):** 게이트 실패 시 병합 금지·revert 우선.

### 3.9 §12 추적성 매트릭스

- **Dual-Track** 열 추가(A / B / A+B / —).
- 불명확 참조(`U계열`, `D-T03` 등)를 **TP-*, TD-*** 중심으로 정리.
- NFR-06에 대응하는 **재현 가능 빌드** 행 추가.

### 3.10 §13 Glossary (신설)

- UX Contract, Logic Rule, Track/Job, Boundary, Domain, Facade, SoT, 골든 데이터, INV-C*, MLOps 정합(본 PRD 의미) 정의.

### 3.11 품질 수정

- **BR-ERR-01:** “공밍” → “**공백**” 오타 수정.

---

## 4. PRD 목차 구조 변화 (Reporter/16 대비)

`Reporter/16`은 PRD를 **12개 절**로 요약했다. 현재 PRD는 **§13 Glossary**가 추가되어 **13개 본문 절 + 문서 이력** 구조다.

| 절 | 비고 |
|----|------|
| 1~7 | 기존과 동일 축; §7에 NFR-06 추가. |
| 8 | Dual-Track + MLOps + 계약·RACI·DoD·안티패턴·루프(소절 8.1~8.10). |
| 9 | Dual-Track 열·§9.5 추가. |
| 10 | §10.4 추가. |
| 11 | DEC-06 추가. |
| 12 | Dual-Track 열·행 정리. |
| **13** | **Glossary** 신설. |

---

## 5. 구현·CI에 대한 권장 후속 (본 보고서 범위 밖)

PRD는 구현을 요구하지 않으나, 문서가 이미 요구하는 바에 맞추려면 다음이 자연스럽다.

1. **CI:** Job A(UX Contract)·Job B(Logic) 분리, 병합 조건 A∧B, 아티팩트에 커버리지·테스트 리포트(§8.5.1).
2. **테스트 패키지:** Track A에서 `**/domain/**` 직접 import 금지를 소스·리뷰 규칙 또는 ArchUnit 등으로 보강(§10.4).
3. **Reporter/16 갱신(선택):** PRD 버전·절 개수·DEC-06·§13을 반영한 짧은 부록 커밋.

---

## 6. 문서 이력

| 항목 | 내용 |
|------|------|
| 보고서 위치 | `Reporter/17_magic-square-prd-dual-track-mlops-alignment-report.md` |
| PRD 위치 | `docs/PRD_MagicSquare_4x4_TDD.md` (v1.2) |
| 성격 | Dual-Track·MLOps 정합 및 **1.1~1.2 보완** 작업의 **Reporter보내기**; PRD 전문의 대체 본문 아님 |

---

**문서 끝**
