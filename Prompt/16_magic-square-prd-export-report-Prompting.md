# PRD 작성 지침 및 요구사항
_Exported on 4/28/2026 at 08:45:11 GMT+9 from Cursor (3.2.11)_

---

**User**

당신은 시니어 제품/소프트웨어 아키텍트이며 Dual-Track UI + Logic TDD 및 Concept-to-Code Traceability 전문가입니다.
PRD 본문 골격은 Report/4를 축으로 하고, Report/1로 문제·동기를 보강하며, 기능·계약·성공 정의는 Report/2, 품질·개발 원칙은 Report/3(및 cursor 규칙) 에서 가져오는 방식으로 다음 내용을 고려해 docs 폴더에 PRD를 작성해 주세요.

프로젝트: Magic Square (4x4) — TDD 연습용
목적:
알고리즘 난이도보다 TDD 훈련이 목적
Invariant 기반 설계/검증 사고를 체득
입력/출력 계약을 명확히 고정
UI/DB/Web 의존성 없이 순수 로직 중심으로 구현 가능하게 PRD 작성
⚠️ 중요 규칙
구현 코드를 작성하지 마십시오.
새로운 기능을 추가하지 마십시오. (요구사항 범위 유지)
모호한 표현(“적절히”, “충분히” 등)을 사용하지 마십시오.
모든 요구사항은 테스트/검증 가능해야 합니다.
Dual-Track(경계/도메인) 분리를 문서 구조에 반영하십시오.
Concept → Rule → Use Case → Contract → Test → Component 추적성을 반드시 포함하십시오.
출력은 구조화된 Markdown으로 작성하십시오.
---
[입력/출력 계약(고정)]
입력(Input):
4x4 정수 행렬 int[][]
0은 빈칸
빈칸(0)은 정확히 2개
값 범위: 0 또는 1~16
0을 제외한 중복 숫자 금지
첫 번째 빈칸 정의: row-major(행 우선) 스캔 시 먼저 발견되는 0
출력(Output):
int[6]
좌표는 1-index
포맷: [r1, c1, n1, r2, c2, n2]
n1,n2는 누락 숫자 2개
시도 1: 작은 수 → 첫 빈칸, 큰 수 → 둘째 빈칸
마방진이면 그 순서 반환
시도 2: (시도 1 실패 시) 큰 수 → 첫 빈칸, 작은 수 → 둘째 빈칸
마방진이면 역순 반환
두 시도 모두 실패 시 오류 정책에 따라 처리(명시 필수)
마방진 상수(Magic Constant):
n=4 → 34
---
[PRD 작성 지시]
아래 구조를 반드시 지켜 PRD를 작성하십시오.
1. Executive Summary
한 문단 요약
프로젝트가 훈련하려는 핵심 역량(불변조건/계약/TDD)
2. Problem Statement (문제 정의)
“마방진을 만든다”가 아니라 “불변조건을 검증 가능한 형태로 완성한다” 관점으로 정의
왜 입력/출력 계약이 핵심인지 설명
3. Target Users
TDD 학습자/리뷰어 관점
사용 목적/사용 환경(콘솔/테스트 실행)
4. Scope
4.1 In-Scope
빈칸 좌표 찾기
누락 숫자 찾기
마방진 판정
두 조합 시도 후 결과 반환
입력 검증(경계 레이어)
4.2 Out-of-Scope
UI 화면 개발
DB 저장/조회
N×N 일반화(기본 PRD 범위 제외, 확장 항목으로만)
마방진 “생성” 알고리즘(완전 생성 문제)
5. Functional Requirements (기능 요구사항)
각 기능마다 아래 템플릿을 반복해서 작성하십시오:
Feature ID
설명(1~2문장)
입력
처리 규칙(불변조건 포함)
출력
승인 기준(AC) — 반드시 테스트 가능 문장으로
관련 오류/예외 정책
필수 기능 목록:
FR-01 입력 검증 (Boundary)
FR-02 빈칸 탐색
FR-03 누락 숫자 탐색
FR-04 마방진 판정
FR-05 해 찾기(solution): 두 조합 시도 및 반환
6. Business Rules (도메인 규칙)
BR-01 ~ 형태로 나열
“항상 참이어야 하는 규칙”으로 서술
예: 중복 금지, 합 규칙, 좌표 인덱스 규칙, row-major 규칙 등
7. Non-Functional Requirements
테스트 커버리지 목표:
Domain Logic 95%+
Boundary Validation 85%+
결정론적 실행(동일 입력 → 동일 출력)
부작용 금지(입력 행렬 변경 정책 명시)
성능 기준(선택): 4x4 기준 즉시 처리(예: 50ms 내)
8. Dual-Track TDD Strategy
8.1 Track A — Boundary(UI) TDD
Contract-first 테스트 항목 목록
실패 정책(예외 타입/메시지 표준)
8.2 Track B — Domain(Logic) TDD
메서드 단위 테스트 목록
불변조건 테스트 목록
8.3 병렬 진행 규칙
UI RED & Logic RED → UI GREEN & Logic GREEN → REFACTOR
“도메인 먼저 다 구현 후 경계 추가” 금지
9. Test Plan (QA)
시나리오 기반 테스트 목록(정상/역순 성공/실패/입력오류)
회귀 테스트 정책
테스트 데이터(대표 4x4 예시 행렬) 포함
Property/Invariant 기반 체크 항목
10. Architecture Overview (High-Level)
레이어 정의:
Boundary Layer(입력검증/출력형식)
Domain Layer(순수 로직)
책임 분리(SRP)와 확장(OCP) 전략
의존성 방향(도메인이 경계를 모르게)
11. Risks & Ambiguities
모호한 부분을 “결정 항목”으로 명시(예: 두 시도 모두 실패 시 정책)
자주 실수하는 포인트(1-index, row-major, 입력 변경 여부 등)
12. Traceability Matrix (필수)
다음 형식으로 표를 제공하십시오:
Concept/Invariant → Business Rule → Feature(FR) → Acceptance Criteria → Test Case → Component
---
출력 요구사항
전체를 Markdown으로 출력
번호/ID 체계 일관성 유지
구현 코드 작성 금지
모든 요구사항은 검증 가능 문장으로


---

**Cursor**

Report/1–4와 프로젝트 구조를 확인한 뒤 PRD를 작성합니다.



Report 01–04를 반영해 `docs` 폴더에 PRD를 작성합니다. 사용자가 고정한 입·출력 계약(시도 2 성공 시 `n1,n2` 역순)을 명시하고, Data 레이어는 Out-of-Scope로 두어 순수 로직 중심으로 맞춥니다.



`docs` 폴더에 PRD Markdown 파일을 생성합니다.



작업을 마쳤습니다. `Reporter/01`~(문제·불변·계약 동기), `Reporter/02`~(레이어·계약·에러·트레이서빌리티·Dual-Track), `Reporter/03`~(Red–Green–Refactor), `Reporter/04`~(규칙 검토·에이전트 한계)를 반영해 **`docs/PRD_MagicSquare_4x4_TDD.md`**에 요청하신 12개 절 구조로 PRD를 두었습니다.

**반영한 요지**

- **문제 정의:** “마방진을 만든다”가 아니라 **불변조건을 검증 가능한 완성 상태로 판정·출력한다**는 틀(`Reporter/01` 정합).
- **고정 계약:** 입력 `int[][]`, 빈칸 2·row-major 첫/둘째 0, 출력 `int[6]` 1-index, 시도 1→시도 2, 시도 2 성공 시 **`n1`=큰 수, `n2`=작은 수**(DEC-04로 문장 고정).
- **실패·모호:** 둘 다 실패 → `NO_SOLUTION`; 둘 다 성공 → `AMBIGUOUS_SOLUTION`(`Reporter/02`와 동일); 시도 1 성공 시 시도 2 **미실행**(DEC-03).
- **Out-of-Scope:** UI·DB·Web·N×N·완전 생성; Data 레이어는 본 PRD에서 **다루지 않음**(순수 로직·경계 중심).
- **NFR:** Domain 95%+ / Boundary 85%+ / 결정론 / **호출자 배열 불변** / 선택 50ms.
- **§12 매트릭스:** Concept/Invariant → BR → FR → AC → Test → Component 표 형식.

구현 코드는 넣지 않았고, 요청 범위 밖의 새 기능은 추가하지 않았습니다. 수정이 필요하면 원하는 절 번호만 짚어 주시면 됩니다.

---

**User**

Reporter 폴더에  지금 작업한 내용을 보고서로 내보내줘.

---

**Cursor**

Reporter 폴더의 번호 체계를 확인한 뒤 PRD 작업을 요약한 보고서를 추가합니다.



PRD 산출물을 Reporter 번호 체계에 맞춰 `16`번으로보내는 보고서를 작성합니다.



`Reporter/16_magic-square-prd-export-report.md`에 **PRD 작성 작업**을 Reporter용으로 정리해 두었습니다.

**포함 내용**

- **보내기 일자·원본 SoT:** `docs/PRD_MagicSquare_4x4_TDD.md`
- **요약 표:** 목적, 범위, 근거 Reporter(01~04)
- **PRD 12개 절 목차**와 **FR-01~05·DEC-01~05** 요약
- **Report/3·4**와 §7·§8의 연계 한 줄 정리
- **Reporter ↔ PRD** 추적 표
- PRD 전문을 복붙하지 않고 **인덱스·요약**만 두었다는 점 명시

전문은 계속 `docs/PRD_MagicSquare_4x4_TDD.md`를 보면 됩니다.

