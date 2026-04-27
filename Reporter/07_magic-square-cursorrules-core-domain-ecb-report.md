# 마방진 과제 — `.cursorrules` 핵심 도메인·ECB·테스트 우선순위 반영 작업 보고서

**작성 목적:** 사용자 요청에 따라 루트 `.cursorrules`에 **MagicSquare 핵심 도메인**, **레이어 역할 정교화**, **테스트 우선순위·UI 이후 규칙**, **mock·숨은 상태 관련 설계 원칙**을 반영한 변경 내용을 문서화한다.  
**범위:** `c:\DEV\MagicSquare_XXX\.cursorrules` 단일 파일의 편집 내역. 이 시점의 소스 코드 구현·pytest 실행 결과는 포함하지 않는다.  
**참고 문서:** `Reporter/05_magic-square-cursorrules-completion-report.md`(ECB+TDD 완성본 기준선), `Reporter/06_magic-square-cursorrules-dual-track-mlops-expansion-report.md`(별도 확장 설계 메모).

---

## 1. 작업 요약

| 항목 | 내용 |
|------|------|
| 요청 배경 | 4×4 마방진 핵심 도메인(입력 검증·누락값 계산·합 34 검증·UI와 순수 로직 분리)을 규칙에 명시하고, boundary / control / entity 책임을 한 줄씩 재정의하며, 테스트는 entity → control → boundary 순, UI 구현 전 순수 로직 테스트 강제, mock 남용 금지·순수 함수·명시적 데이터 전달을 규칙화할 것. |
| 수행 | 기존 YAML 구조를 유지한 채 **`domain`**, **`design_principles`**, **`testing.layer_test_priority`·`before_ui_implementation`**, **`forbidden` 신규 항목**, **`architecture.layers`·`file_structure`·`ai_behavior` 보강**을 반영했다. |
| 산출물 위치 | 저장소 루트 `.cursorrules`(프로젝트 상대 경로 동일). |

---

## 2. 섹션별 반영 내용

### 2.1 `domain` (신규)

`domain.core` 목록으로 다음을 SoT에 고정했다.

- 4×4 마방진(크기 4, 값 1–16, 마방진 상수 34).
- 입력 검증(형식·범위·중복·부분 완성 격자 일관성; 구체 규칙은 entity).
- 누락값 계산(제약 하 유일 후보·후보 집합 등 순수 계산).
- 합 34 검증(완성·부분 구간).
- 사용자 입력 UI와 순수 계산 로직의 분리(UI는 boundary, 계산·규칙은 entity/control).

### 2.2 `architecture.layers` (정교화)

| 레이어 | 변경 요지 |
|--------|-----------|
| **boundary** | 역할을 **UI·사용자 입력·출력만**으로 명시. `contains`에 웹·TUI 등 사용자 입력 UI 추가. `must_not`에 누락값 계산·34 검증 등 도메인 직접 구현 금지 및 control/entity 호출·DTO·표현만 허용하도록 문장화. |
| **control** | 역할을 **유스케이스 조합과 흐름 제어만**으로 명시. `contains`에 `"입력→검증→누락값 계산"` 등 단계 조합 예시 추가. `must_not`에 콘솔뿐 아니라 **UI 위젯** 직접 의존 금지 추가. |
| **entity** | 역할을 **순수 규칙·검증·계산만**으로 명시. `contains`에 누락값 계산·마방진 상수(합 34) 명시. `must_not`에 **UI** 추가. |

`dependency_direction` 문구는 기존과 동일하게 유지했다.

### 2.3 `design_principles` (신규)

- **`pure_functions_first`:** entity(및 control의 순수 부분)를 부작용 없는 함수·값 객체 중심으로 하여 동일 입력→동일 출력, 테스트에서 mock 없이 검증 가능하게 한다.
- **`mocking_policy`:** mock·스텁 남용 금지; 외부 시스템·시간·랜덤·프레임워크 훅 등 boundary 근처만 최소 사용. control/entity는 가짜 이중 구현 대신 실제 순수 로직과 명시적 입력으로 검증.
- **`explicit_over_hidden_state`:** 전역 가변·숨은 설정·암묵적 공유 컨텍스트보다 인자·반환·불변 DTO로 의도를 드러낸다.

### 2.4 `testing` (보강)

- **`layer_test_priority`:** 테스트 추가·보강·Red 시작 우선순위 **entity → control → boundary**. 규칙·누락값·합 34는 entity에 먼저 고정한다는 운영 원칙을 문장으로 명시.
- **`before_ui_implementation`:** 사용자 입력 UI 구현 **전에** 동일 요구의 entity(필요 시 control) 순수 로직 테스트를 먼저 작성하고 Red→Green 후 boundary에서 어댑팅하도록 강제.

기존 `framework`·AAA·`coverage_minimum`·`fixture_scope`·`naming_convention`·`layout`은 변경 없이 유지했다.

### 2.5 `forbidden` (신규 항목)

- **entity/control 테스트에서 도메인 로직을 mock으로 대체·우회하는 남용**을 `pattern` / `reason` / `alternative` 형식으로 추가. `design_principles.mocking_policy`와 상호 참조되도록 작성했다.

### 2.6 `file_structure` (주석만)

- `boundary`·`control`·`entity` 디렉터리 주석을 위 역할 정의(UI만 / 유스케이스 조합·흐름만 / 순수 규칙·검증·계산)에 맞게 갱신했다.

### 2.7 `ai_behavior` (보강)

- **before_coding:** 도메인 키워드에 입력 검증·누락값·합 34 추가; 테스트 우선순위 및 UI 이전 순수 로직 규칙 준수를 명시.
- **during_coding:** 경계 위반 예시에 **UI**·**도메인 규칙·계산**을 boundary 금지 쪽에 명시; **순수 함수·명시적 데이터·mock 최소화**를 `design_principles`와 연결한 불릿 추가.

---

## 3. 이전 보고서와의 관계

- **05 보고서**에서 정의한 ECB·TDD·pytest·`forbidden` 스키마·`ai_behavior`의 골격은 그대로 두고, **도메인·설계 원칙·테스트 순서·mock 금지**를 **추가·세분화**한 것이 본 작업이다.
- **06 보고서**는 Dual-Track·MLOps 등 **별도 확장 설계안**을 기록한 문서이며, 본 변경은 06에 나열된 확장 키 전체를 루트 `.cursorrules`에 반영한 것은 아니다. 향후 06안과 병합할 경우 중복 문구·우선순위를 한 번 정리하는 것이 좋다.

---

## 4. 권장 후속

- `magic_square/` 패키지 및 `tests/` 미러가 생기면, **`tests/entity` → `tests/control` → `tests/boundary`** 순으로 스위트를 채우는지 CI 또는 체크리스트로 점검할 수 있다.
- 실제 UI(boundary)를 도입할 때는 **`before_ui_implementation`**에 맞춰 entity 테스트가 먼저 존재하는지 PR 리뷰에서 확인한다.

---

**문서 버전:** 1.0 (채팅 세션에서 `.cursorrules` 편집 직후 기준)
