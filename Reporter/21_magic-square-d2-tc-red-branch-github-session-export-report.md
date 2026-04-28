# Magic Square (4×4) — D2 단위 테스트 케이스·`red` 브랜치·GitHub 푸시 세션 보내기 보고서

**보내기 일자:** 2026-04-28  
**산출물 유형:** Reporter 폴더 아카이브용 **교육 슬라이드(D2) 정합 단위 TC 문서**, **브랜치 전략 안내**, **`red` 브랜치·원격 동기화** 작업 정리 보고서  
**관련 대화 산출:** Cursor 세션 — 원격/로컬 정합 확인, README 작업용 브랜치 전략 조언, `red` 생성, 슬라이드 형식 TC 샘플 작성, `origin` 푸시

---

## 1. 보내기 요약

| 구분 | 내용 |
|------|------|
| **작업명** | (1) GitHub `asul99/MagicSquare_23`와 로컬 커밋 정합 확인, (2) README·문서 작업용 브랜치 전략 제안, (3) **`red`** 브랜치 생성·체크아웃, (4) D2 실습 슬라이드와 동일 항목 구조의 **단위 테스트 케이스 문서** 추가, (5) **`origin/red`** 푸시 |
| **핵심 산출 파일** | [`docs/TC_D2_unit_magic_square_entity_user_sample.md`](../docs/TC_D2_unit_magic_square_entity_user_sample.md) |
| **Git** | 로컬 브랜치 `red`; 원격 추적 `origin/red`; 문서 반영 커밋 `12fef42` |
| **요구·도메인 SoT** | 마방진 본 기능·FR·오류 코드는 [`docs/PRD_MagicSquare_4x4_TDD.md`](../docs/PRD_MagicSquare_4x4_TDD.md); 본 TC 샘플은 ECB 예시 **`magic_square.entity.user`** 및 [`tests/entity/test_user.py`](../tests/entity/test_user.py)에 대응 |
| **추적·README 맥락** | [`Reporter/20_magic-square-readme-todo-traceability-session-export-report.md`](20_magic-square-readme-todo-traceability-session-export-report.md) — 슬라이드·RTM·TASK ID 정합; 본 세션의 TC 표는 동일 교육 맥락(D2 실습)에서 **문서화 템플릿** 역할 |

---

## 2. 원격(GitHub)과 로컬 정합(세션 초기)

| 확인 항목 | 결과 |
|-----------|------|
| `origin` URL | `https://github.com/asul99/MagicSquare_23.git` — 요청 URL과 일치 |
| 기본 브랜치 | GitHub·로컬 모두 `main` |
| `main` 최신 커밋(세션 시점) | SHA `45f6538…` — 로컬 `HEAD`/`origin/main`과 일치 |
| 워킹 트리 | 세션 초기에는 루트 `README.md` 로컬 수정 가능성 언급; **`red`에서 문서 커밋 시점**에는 추적 대상이 TC 신규 파일 중심 |

**GitHub 저장소 메타(참고):** 설명 필드 예시 `작성자:정재훈, 리뷰어:홍길동`, 주 언어 Python — 클론 메타이며 TC 샘플 표지의 작성자·승인자 예시와 정렬.

---

## 3. 브랜치 전략(세션에서 제안한 요지)

| 상황 | 권장 |
|------|------|
| 혼자·즉시 반영 | `main`에서 README만 수정 후 푸시 가능 |
| PR·이력 분리 | `main` 갱신 후 `docs/readme-…` 등 **짧은 수명 브랜치** → PR → merge (**GitHub Flow**) |
| 장기 `develop`/Git Flow | 본 저장소 규모·README·문서 위주 작업에는 과함 |

사용자 요청에 따라 실제 작업 브랜치 이름은 **`red`** 로 고정(문서 작업·RED 단계 연상 등 팀 내 의미에 맞게 사용 가능).

---

## 4. `red` 브랜치 및 Git 이력

| 항목 | 값 |
|------|-----|
| 생성 명령 | `git checkout -b red` (이전 브랜치에서 분기) |
| 문서 커밋 | `12fef42` — *docs: add D2 unit test case sample for entity user (slide layout)* |
| 원격 푸시 | `git push -u origin red` — **`red` → `origin/red`** (최초 푸시 시 네트워크 재시도 후 성공) |
| PR 생성 URL(참고) | `https://github.com/asul99/MagicSquare_23/pull/new/red` |

`main`에 병합하려면 위 PR로 merge하거나, 로컬에서 `main`으로 merge 후 `git push origin main` 절차를 따르면 된다.

---

## 5. 단위 테스트 케이스 문서(`docs/TC_D2_…`) 구조

슬라이드 **「D2_2. Practice — Magic Square 테스트 케이스 작성」** 예시(프로젝트명·대상 시스템·단계·작성자·승인자·문서 상태·작성일·버전·테스트 범위·조직·테스트 ID·일자·목적·기능·입력값·**테스트단계 표**·환경·전제·성공·실패·특별 절차)를 **Markdown 표**로 재현.

| 절 | 내용 |
|----|------|
| 표지·식별 | Magic Square (4×4) TDD, 대상 `entity.user`, 단위 테스트, 작성자·승인자 예시(정재훈·홍길동), v1.0, 작성일 2026-04-28 |
| 테스트 단계 | 열: **테스트 케이스 / 예상값 / 중요도 / 성공·실패 / 비고** — 각 행을 `test_user.py`의 테스트 함수와 대응 |
| 환경·조건 | Python 3.10+, pytest, 전제·성공·실패 기준·특별 절차 |
| 빈 양식 | 마방진 PRD 기반 TC를 같은 형식으로 확장할 수 있도록 하단에 **복사용 뼈대** 포함 |

**범위:** 슬라이드의 **사칙연산** 수치 예는 본 저장소 코드와 무관하므로, 대신 **이미 존재하는 단위 테스트**로 치환해 실습 형식만 유지했다.

---

## 6. 연계 문서·코드

| 경로 | 본 세션과의 관계 |
|------|------------------|
| `docs/TC_D2_unit_magic_square_entity_user_sample.md` | 세션 산출 TC 문서 |
| `tests/entity/test_user.py` | TC 표의 근거 테스트 |
| `README.md` | 문서 맵·스택·Reporter 인덱스; **선택:** 문서 맵 표에 본 `Reporter/21` 한 줄 추가 |
| `Reporter/18` | TASK·FR 추적 SoT |
| `Reporter/20` | README·슬라이드·RTM 세션과 개념 연속 |
| `docs/PRD_MagicSquare_4x4_TDD.md` | 빈 TC 양식으로 확장할 마방진 요구의 근거 |

---

## 7. 후속 권장(선택)

- `README.md` **문서 맵**에 `Reporter/21`(본 보고서) 및 필요 시 `docs/TC_D2_…` 한 줄을 추가해 탐색성을 맞춘다.  
- `red`를 `main`에 합친 뒤에는 기본 작업 브랜치를 `main`으로 되돌리거나, 이후 문서 전용 브랜치 네이밍(`docs/…`)을 팀 규칙으로 통일한다.  
- PRD **FR·BR-ERR** 단위로 `TC_D2` 하단 빈 양식을 복사해 **마방진 전용 TC ID**(예: `TC-MS-GRID-001`)를 발급·추적한다.

---

## 8. 변경 이력(Reporter)

| 일자 | 내용 |
|------|------|
| 2026-04-28 | 초안: D2 TC 문서·`red`·GitHub 푸시·원격 정합·브랜치 전략 세션 보내기 |
