# 마방진 과제 — `.cursorrules` 확장 설계(Dual-Track · MLOps) 작업 보고서

**작성 목적:** 사용자 요청에 따라 MagicSquare용 `.cursorrules`를 **YAML 구조·추가 섹션·방법론(Dual-Track UI + Logic TDD with MLOps)** 관점에서 재설계한 내용을 문서화한다.  
**범위:** 규격 설계·섹션 정의·금지 패턴 스키마 정리. 이 보고서 작성 시점의 저장소 루트 `.cursorrules` 파일과의 **차이**를 명시한다.  
**참고 문서:** `Reporter/05_magic-square-cursorrules-completion-report.md`(기존 ECB+TDD 완성본), `Prompt/` 내 관련 프롬프트(해당 시).

---

## 1. 작업 요약

| 항목 | 내용 |
|------|------|
| 요청 배경 | 프로젝트명 MagicSquare, 방법론 **Dual-Track UI + Logic TDD with MLOps**, ECB, pytest AAA, RED–GREEN–REFACTOR, `forbidden` 항목별 `reason`·`alternative`, YAML·2스페이스 들여쓰기, 80자 `#` 구분선, 키 영어·설명 한국어. |
| 설계 산출 | 채팅 세션에서 **완성형 규격 텍스트**로 출력한 `.cursorrules` 초안(다음 절의 섹션 구성과 동일). |
| 저장소 상태 | 루트 `.cursorrules`는 **05 보고서 기준 ECB+TDD 완성본** 형태이며, 본 보고서 §2에 나열한 **확장 섹션(예: `core_principles`, `ui_logic_dual_track_rules`, `methodology` 필드, `review_checklist` 등)은 아직 파일에 반영되지 않았다.** |
| 권장 후속 | 확장안을 단일 SoT로 채택할 경우, 루트 `.cursorrules`에 병합·정렬 후 `pytest` 및 팀 리뷰로 문구·중복을 한 번 더 점검한다. |

---

## 2. 설계안에 포함된 상위 섹션

아래는 채팅에서 제시한 확장 규격의 **최상위 키** 목록이다. 저장소 현재 파일(05 스타일)과 비교할 때 **추가·강화**된 축이다.

1. **`project`** — `name`, `description`, **`methodology`**, `language`
2. **`core_principles`** — 도메인 우선, 입출력 분리, ECB 의존성 방향
3. **`code_style`** — Python 3.10+, PEP8, 타입 힌트, Google docstring, 줄 길이, 함수·클래스 책임·네이밍
4. **`architecture`** — ECB `boundary` / `control` / `entity` 역할·금지 사항
5. **`ui_logic_dual_track_rules`** — UI 트랙 vs 로직 트랙 테스트 분리, 경량 **MLOps** 가이드(실험·재현성, entity 레이어 오염 금지)
6. **`tdd_rules`** — `red_phase` / `green_phase` / `refactor_phase` 동일 깊이, 단계별 `rules`·`must_not`·전환 조건
7. **`refactoring_rules`** — 리팩터 범위·실무(추출·명명·경계 재확인)
8. **`testing`** — pytest, AAA, fixture 스코프, 커버리지 하한, `tests/` 미러 구조
9. **`forbidden`** — 항목마다 **`pattern`**, **`reason`**, **`alternative`**
10. **`file_structure`** — `magic_square/` 및 `tests/` ECB 폴더 예시
11. **`ai_behavior`** — 코딩 전·중·후 에이전트 행동, TDD 위반 시 `[TDD_RULE_WARNING]` 안내
12. **`review_checklist`** — PR·셀프리뷰용 체크 항목

**형식 규칙(설계안):** 각 주요 섹션 앞 **80자 해시(`#`) 구분선**과 섹션 제목 주석 라인을 두는 형태로 정의했다.

---

## 3. 저장소 `.cursorrules`와의 차이(요점)

| 영역 | 현재 저장소 `.cursorrules` (요지) | 확장 설계안 (요지) |
|------|-----------------------------------|---------------------|
| 머리말 | `# MagicSquare …` 2줄 주석 헤더 | 동일 유지 가능; 구분선 스타일은 설계안이 더 장문 |
| `project` | `name`, `description`만 | **`methodology`**, **`language`** 추가 |
| 원칙 | `architecture.dependency_direction` 등에 분산 | **`core_principles`**로 한곳에 요약 |
| Dual-Track / MLOps | 없음 | **`ui_logic_dual_track_rules`** 신설 |
| 리팩터 일반 | `tdd_rules.refactor_phase`에 집중 | **`refactoring_rules`** 보완 섹션 추가 |
| 금지 패턴 | `forbidden`에 reason/alternative **있음** | 동일 스키마 유지 + **boundary 도메인 직구현·테스트 트랙 혼합** 등 항목 **추가** |
| 리뷰 | 없음 | **`review_checklist`** 추가 |
| `ai_behavior` | 상세 bullet + `tdd_violation_warning` | 유사 + Dual-Track·MLOps 준수 문구 반영 설계 |

---

## 4. 방법론·테스트 관점 정리

- **Dual-Track:** boundary(UI·CLI·표현) 변경과 entity/control 로직 변경을 **서로 다른 테스트 트랙**으로 나누고, 동일 시나리오의 중복 단언을 피하도록 규칙화했다.
- **MLOps:** 마방진 본연 로직과 분리된 **실험·메트릭·재현성**만 언급 수준이며, entity에 인프라 SDK를 직접 두지 않도록 **금지 방향**을 명시했다.
- **TDD:** RED → GREEN → REFACTOR 순서와 각 단계에서 **허용·금지·전환 조건**을 05본과 호환되게 유지하면서, 요청에 맞춰 키 구조를 정렬했다.

---

## 5. 산출물·경로

| 구분 | 경로 |
|------|------|
| 본 보고서 | `Reporter/06_magic-square-cursorrules-dual-track-mlops-expansion-report.md` |
| 기존 규칙 파일(비교 대상) | `.cursorrules` |
| 이전 완성 작업 기록 | `Reporter/05_magic-square-cursorrules-completion-report.md` |

---

## 6. 결론

이번 작업은 **저장소 파일을 덮어쓴 커밋이 아니라**, 사용자가 요청한 조건을 모두 반영한 **확장형 `.cursorrules` 설계안**을 한 번에 정리한 것이다. 운영 SoT를 확장안으로 통일하려면 **루트 `.cursorrules`에 해당 YAML을 반영**하고, 기존 헤더 주석·`tdd_rules` 세부 문구와 **중복·충돌**을 수동으로 조정하는 것이 좋다.
