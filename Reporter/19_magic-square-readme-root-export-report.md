# Magic Square (4×4) — 루트 README 작성 산출물 보내기 보고서

**보내기 일자:** 2026-04-28  
**산출물 유형:** Reporter 폴더 아카이브용 **저장소 루트 `README.md` 추가** 작업 정리 보고서  
**산출 파일:** 저장소 루트 `README.md` (본 보고서는 해당 작업의 메타·인덱스 고정용)

---

## 1. 보내기 요약

| 구분 | 내용 |
|------|------|
| **작업명** | MagicSquare 프로젝트 **루트 README.md** 작성(본문·To-Do·검증 기준·문서 맵·실행 안내) |
| **저장 위치** | `README.md` (저장소 루트) |
| **중심 근거** | `docs/PRD_MagicSquare_4x4_TDD.md` — 요구사항·AC·NFR·Dual-Track·추적의 SoT |
| **To-Do·에픽·TASK 인덱스** | `Reporter/18_magic-square-implementation-todo-structure-export-report.md` — Epic-001, US-001~006, TASK-001~026 체크리스트로 이관 |
| **스토리 표현** | `Reporter/09`, `Reporter/11`, `Reporter/10`~`15` 시리즈 및 PRD §5와 README 내 교차 안내 |
| **오류·계약 요약** | PRD §6 BR-ERR·FR-01 + `Reporter/02` 보조 |
| **실행·ECB·TDD** | `pyproject.toml`(pytest·패키지), `.cursorrules`(ECB·Red/Green/Refactor·커버리지 하한), `Reporter/06`·`Reporter/17`(Dual-Track·MLOps·CI 정렬) |
| **문서 관계(한 줄)** | README §「문서 맵」표 — `Reporter/01`~`18` 각 파일당 역할 한 줄 + PRD 서두 근거(01·02·03·04)와 `Reporter/16`·`18` 교차 참조 문장 |

---

## 2. 작성 목적 및 범위

**목적:** 저장소 방문자·구현자가 **한 파일**에서 (1) 프로젝트 요지, (2) 어떤 문서가 무엇인지, (3) 무엇을 검증하면 되는지, (4) 어떤 순서로 구현 To-Do를 밟는지, (5) 로컬에서 어떻게 테스트하는지를 바로 찾을 수 있게 한다.

**범위(README에 포함한 것):**

- PRD 기준 **검증 기준** 요약 표(FR·INV·NFR·§8·§12·시나리오 레벨 L0~L3).
- **오류 코드·전문 메시지** 표(BR-ERR-01~07 요약).
- **Reporter 전체**에 대한 한 줄 역할 표(링크 포함).
- **Epic / US / TASK-001~026** 체크박스 목록(Reporter 18과 동일 식별자·R/G/R·시나리오·ECB 열은 README에서 US 블록 단위로 정리).
- **Python 스택**과 PRD의 JVM·JaCoCo 등 **예시 표기**의 차이를 명시하고, 제품 의미는 PRD에 맞춤.

**범위 밖(README에서 하지 않은 것):**

- PRD 본문 수정, Reporter 18의 TASK 표 전문 복제(인덱스는 18이 SoT, README는 실행용 체크리스트).
- 새 구현 코드·CI YAML 추가.

---

## 3. README 본문 구조 (절 대응)

| README 절(논리) | 내용 |
|-----------------|------|
| 머리말 | 4×4 완성 문제 요지, PRD SoT 링크, Python·pytest·`.cursorrules` 스택 고지 |
| 문서 맵 | Reporter `01`~`18` + `12_` 접두 중복 파일 구분( Level3 export vs Level4 technical ) |
| 스토리·에픽 | PRD + Reporter 09·11·10~15 + 18의 Epic/US |
| 오류·계약 | BR-ERR 표 + FR-05·INV·Reporter 02 |
| 검증 기준 | PRD §2.3·§5·§6·§7·§8·§12 및 Reporter 18 §4 |
| 실행·ECB·TDD | `pip install -e ".[dev]"`, `pytest`, `pyproject.toml`, `.cursorrules`, Reporter 06·17 |
| To-Do | TASK-001~026 체크박스, US별 그룹 |
| 라이선스 | `LICENSE` 없을 시 조직 정책 안내 한 줄 |

---

## 4. 연계 문서 (추적)

| 문서 | 본 README 작업과의 관계 |
|------|-------------------------|
| `docs/PRD_MagicSquare_4x4_TDD.md` | README 본문·검증·오류의 **최종 근거** |
| `Reporter/18_magic-square-implementation-todo-structure-export-report.md` | To-Do **구조·TASK 번호·시나리오·ECB**의 Reporter SoT |
| `Reporter/16_magic-square-prd-export-report.md` | PRD 파일 경로·작성 배경과 README의 PRD 링크 정합 |
| `Reporter/02_…clean-architecture…` | 계약·레이어 설명 README 「오류·계약」보조 |
| `Reporter/17_…mlops-alignment…` | Dual-Track·Job A/B README 「실행·ECB·TDD」보조 |
| `pyproject.toml` | `pytest` 경로·옵션·패키지 발견 — README 인용 |
| `.cursorrules` | ECB·TDD·커버리지 하한 — README 인용 |

---

## 5. 후속 권장

| 항목 | 권장 |
|------|------|
| **LICENSE** | 조직 정책에 맞게 루트에 추가 시 README 라이선스 절 보강 |
| **CI** | PRD §8.5 Job A/B를 GitHub Actions 등으로 두면 README의 TASK-024·025와 실제 빌드가 일치 |
| **Reporter 18** | TASK 완료 시 README 체크박스를 동기화하거나, 이슈 트래커로만 관리할지 팀 규칙 결정 |

---

## 6. 문서 이력

| 항목 | 내용 |
|------|------|
| 보고서 위치 | `Reporter/19_magic-square-readme-root-export-report.md` |
| 대상 산출물 | `README.md` (저장소 루트) |
| 성격 | README 추가·구성 결정의 **Reporter 보내기**; README 전문의 대체 저장소는 아님(원본은 Git 루트 파일) |

---

**문서 끝**
