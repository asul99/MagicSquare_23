# 마방진 과제 — `.cursorrules` 완성 작업 보고서

**작성 목적:** `Reporter/04_magic-square-cursorrules-tdd-rules-review-report.md` 이후 수행한 `.cursorrules` 뼈대 채움 작업의 산출물·요구 충족 여부·관련 문서와의 관계를 기록한다.  
**범위:** 워크스페이스 루트에 생성·저장한 `.cursorrules` 한 파일과 그에 대응하는 규격 정리. 소스 코드 구현·테스트 실행 결과는 포함하지 않는다.  
**산출물 위치:** 저장소 루트 `c:\DEV\MagicSquare_XXX\.cursorrules` (프로젝트 상대 경로: `.cursorrules`).

---

## 1. 작업 요약

| 항목 | 내용 |
|------|------|
| 배경 | 04 보고서는 `tdd_rules` SoT(03 보고서)의 **검토**만 다루며, `forbidden`·`ai_behavior` 원문 부재 등 **완성된 단일 `.cursorrules`**는 저장소에 없었다. |
| 수행 | MagicSquare(4×4 마방진) 기준으로 **전 섹션을 YAML 형태로 작성**해 `.cursorrules`에 반영했다. |
| 정합 | 03의 Red–Green–Refactor 흐름(`proceed_when`·`next_phase`)을 유지하면서, 요청 스키마에 맞게 `description`·`rules`·`must_not`으로 **단계별 세분화**했다. |
| 보완 | 04에서 언급된 유니코드 곱따옴표는 **사용하지 않음**. 마방진 도메인 문구에서 혼동 가능한 표기는 **1–16·마방진 합 34**로 정리했다. |

---

## 2. 섹션별 반영 내용

### 2.1 `project`

프로젝트명 MagicSquare와 4×4·1–16·행·열·주대각선 합 동일·탐색·검증·표현·ECB 분리를 한 문단으로 정의했다.

### 2.2 `code_style`

요청대로 `python_version: 3.10+`, PEP8 엄격, 파라미터·반환값 타입 힌트 필수, Google 스타일 public docstring 필수, `max_line_length: 88`을 명시했고, Black(88)·ruff/isort를 권장 보조 항목으로 추가했다.

### 2.3 `architecture`

ECB 세 레이어를 **boundary / control / entity**로 각각 `role`·`contains`·`must_not`까지 구체화했다. **의존성 방향**은 `boundary → control → entity`, entity의 상위 비인지, control은 entity만 직접 의존, boundary는 control(또는 얇은 파사드)만 호출, 역방향 금지로 명시했다.

### 2.4 `tdd_rules`

문자열 한 줄이 아니라 **red_phase / green_phase / refactor_phase** 각각에 대해:

- `description`
- `rules` (목록)
- `must_not` (목록)

을 두었고, 03 보고서와 동일하게 `proceed_when`·`next_phase`를 유지했다. refactor 단계에는 03과 같이 `coverage` 블록을 포함했다.

### 2.5 `testing`

`framework: pytest`, AAA 패턴, `coverage_minimum: 80%`, `fixture_scope`를 function(기본)·module·session·package 정책으로 정의했고, `naming_convention`에 **test_ 접두사** 및 클래스형 `Test*`를 명시했다.

### 2.6 `forbidden`

요청 구조(`pattern` / `reason` / `alternative`)로 최소 세 항목을 포함했다.

- `print()` 기반 출력
- 비즈니스 상수·매직 넘버 하드코딩
- `except` 단독·광범위 삼키기

### 2.7 `file_structure`

ECB 기준 **주석 트리**로 `boundary/`, `control/`, `entity/`, `tests/`(및 하위 미러)를 기술했다. 패키지 루트 디렉터리명은 예시로 `magic_square/`를 사용했다.

### 2.8 `ai_behavior`

코드 작성 **전·중·후**에 대한 규칙을 `before_coding`·`during_coding`·`after_coding`으로 나누었고, 요청한 최소 항목(관련 테스트 확인, ECB 경계 위반 금지, 타입 힌트 없는 함수 금지, TDD 위반 시 경고)을 반영했다. 경고 형식으로 `tdd_violation_warning`에 **`[TDD_RULE_WARNING]`** 접두를 정의했다.

---

## 3. 선행 문서와의 관계

| 문서 | 본 작업과의 관계 |
|------|------------------|
| `Reporter/03_magic-square-cursorrules-tdd-rules-report.md` | `tdd_rules`의 의미·순환 구조의 SoT로 삼고, 필드를 확장해 반영했다. |
| `Reporter/04_magic-square-cursorrules-tdd-rules-review-report.md` | 검토에서 지적된 “에이전트가 기계적으로 보장하기 어려운 규칙”은 **`ai_behavior`·경고 접두**로 완화·가시화했으나, IDE가 상태 머신으로 집행하지는 않는 한계는 그대로다. |
| `Reporter/01_magic-square-problem-definition-report.md` | 도메인 불변(1–16 각 한 번, 행·열·대각선 합 동일 등)을 `project`·`entity` 설명에 반영했다. |

---

## 4. 후속 권장 사항

- 실제 패키지 디렉터리명이 `magic_square`가 아니면 `file_structure` 예시와 프로젝트 트리를 맞춘다.
- CI에서 `pytest` 및 커버리지 80% 게이트를 두면 `testing`·`tdd_rules.refactor_phase.coverage`와 실행 가능한 정합이 생긴다.
- 04의 “`forbidden` vs green 단계 최소 수정” 긴장은 본 `.cursorrules`에 **단계별 `must_not`**으로 구분해 두었으나, 팀 운영 시 충돌이 나면 문장을 한 번 더 조정하는 것이 좋다.

---

**문서 끝**
