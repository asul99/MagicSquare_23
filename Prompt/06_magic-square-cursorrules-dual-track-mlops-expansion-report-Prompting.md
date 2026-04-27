# .cursorrules file generation for MagicSquare project
_Exported on 4/27/2026 at 17:24:00 GMT+9 from Cursor (3.2.11)_

---

**User**

@.cursorrules 파일을 다음을 고려해서 생성해줘.

파일 내용만 출력해. 설명, 마크다운 코드블록 불필요.

--- 프로젝트 정보 ---
프로젝트명: MagicSquare
설명: [한 줄로 프로젝트 설명 작성]
방법론: Dual-Track UI + Logic TDD with MLOps

--- 반드시 포함할 섹션 ---

1. project          → 프로젝트명, 설명, 방법론
2. code_style       → PEP8 엄격 준수, 타입힌트 필수(Python 3.10+), Google 스타일 docstring
3. architecture     → ECB 패턴 (boundary / control / entity 레이어별 역할 정의)
4. tdd_rules        → red_phase / green_phase / refactor_phase 각 단계별 규칙
5. testing          → pytest AAA 패턴(Arrange-Act-Assert), fixture 규칙, 커버리지 기준
6. forbidden        → print() 디버깅 금지, 그 외 금지 패턴 목록
7. file_structure   → 레이어별 폴더 구조 예시
8. ai_behavior      → 코드 생성 시 Cursor AI가 반드시 따라야 할 행동 규칙

--- 형식 규칙 ---
- YAML 형식, 들여쓰기 2 스페이스
- 각 섹션 앞에 80자 # 구분선 + 섹션 제목 주석
- 키는 영어, 설명은 한국어로 작성
- tdd_rules 하위에 red_phase / green_phase / refactor_phase 동일 깊이로 작성
- forbidden 항목마다 reason(이유)과 alternative(대안)을 함께 명시
```
```
너는 Cursor.AI용 프로젝트 규칙 파일(.cursorrules)을 설계하는 시니어 소프트웨어 아키텍트다.

내 목표는 MagicSquare 프로젝트에 맞는 .cursorrules 파일을 만드는 것이다.
반드시 Cursor가 바로 해석하고 따를 수 있도록, 구조적이고 명확한 규칙 문서로 작성하라.

다음 조건을 반영하라.

[프로젝트 정보]
- project: MagicSquare
- style: PEP8 + 타입힌트
- testing: pytest, AAA 패턴
- architecture: ECB (boundary / control / entity)
- forbidden: print() 디버깅 금지
- methodology: Dual-Track UI + Logic TDD
- language: Python

[내가 원하는 결과]
1. 최종 출력은 .cursorrules 파일 내용만 제공한다.
2. 설명문 없이 바로 복붙 가능한 규칙 문서 형태로 작성한다.
3. 섹션은 계층형 YAML 스타일 또는 Cursor Rules에 적합한 구조적 텍스트로 작성한다.
4. 다음 항목을 반드시 포함한다:
   - project
   - core_principles
   - coding_style
   - architecture_rules
   - testing_rules
   - tdd_rules
   - ui_logic_dual_track_rules
   - forbidden_rules
   - refactoring_rules
   - file_organization
   - review_checklist
5. ECB 아키텍처를 기준으로 boundary, control, entity의 책임을 분리해서 명시한다.
6. pytest 테스트는 반드시 AAA(Arrange-Act-Assert) 패턴을 따르도록 규칙화한다.
7. print() 디버깅 금지, 대신 logging 또는 테스트로 검증하도록 규칙화한다.
8. 타입힌트는 모든 공개 함수/메서드에 필수로 강제한다.
9. PEP8 준수, 함수 길이/클래스 책임/네이밍 규칙도 포함한다.
10. TDD는 RED → GREEN → REFACTOR 순서를 강제하고, 각 단계에서 Cursor가 어떻게 행동해야 하는지 써라.
11. Dual-Track UI + Logic TDD 관점에서 UI 테스트와 로직 테스트를 분리하도록 규칙화하라.
12. MagicSquare 프로젝트에 맞게 “도메인 로직 우선, 입출력/표현 분리” 원칙을 강조하라.

[출력 형식 요구]
- 마크다운 코드블록 없이 순수 텍스트로만 출력
- 들여쓰기와 섹션 구분이 명확해야 함
- 실제 .cursorrules 파일처럼 보여야 함

이제 위 조건을 만족하는 완성형 .cursorrules를 다시 작성하라.


---

**Cursor**

################################################################################
# project
################################################################################
project:
  name: MagicSquare
  description: >
    4×4 격자에 1–16을 각각 한 번씩 배치하여 행·열·주대각선의 합이 동일한
    마방진을 탐색·검증·표현한다.
  methodology: Dual-Track UI + Logic TDD with MLOps
  language: Python

################################################################################
# core_principles
################################################################################
core_principles:
  domain_first: >
    도메인(마방진 규칙·탐색·검증) 로직을 최우선으로 설계하고,
    입출력·UI·CLI는 boundary에서 분리한다.
  separation_of_concerns: >
    표현·프레임워크·I/O는 boundary, 유스케이스·흐름은 control,
    순수 규칙·데이터는 entity에 둔다.
  dependency_direction: boundary → control → entity (역방향 금지)

################################################################################
# code_style
################################################################################
code_style:
  python_version: "3.10+"
  pep8: 엄격 준수 (공백, 네이밍, import 정렬, 줄 길이 제한 등)
  type_hints: 모든 공개·비공개 함수·메서드의 파라미터와 반환값에 필수 (Any 남용 금지)
  docstring: Google 스타일, 모든 public 클래스·함수·메서드에 필수
  max_line_length: 88
  formatter_linter: Black(88)·ruff/isort 권장
  function_length: 한 함수는 단일 책임을 유지하고 과도하게 길어지면 분리한다.
  class_responsibility: 클래스는 하나의 응집된 역할에 집중한다.
  naming: 의미 있는 전체 단어형 이름, 약어는 도메인에서 통용될 때만 사용한다.

################################################################################
# architecture
################################################################################
architecture:
  pattern: ECB (Entity–Control–Boundary)
  layers:
    boundary:
      role: 외부 입출력·표현 담당
      contains:
        - CLI 인자 파싱·프롬프트·표 형식 출력
        - UI 컴포넌트·뷰(해당 시)
        - HTTP/API 핸들러(해당 시)
        - 파일·스트림 어댑터
      must_not: 행/열/대각선 합·중복 등 도메인 규칙을 직접 구현하지 않는다. control/entity만 호출한다.
    control:
      role: 유스케이스·비즈니스 흐름 오케스트레이션
      contains:
        - 한 해 찾기, 전체 열거, 격자 검증 등 유스케이스
        - 탐색 전략 선택·가지치기 순서
      must_not: 콘솔 print, 프레임워크에 직접 결합하지 않는다.
    entity:
      role: 도메인 데이터·불변 규칙·순수 연산
      contains:
        - 격자 표현, 마방진 상수, 검증·합산·인덱스 규칙
      must_not: argparse, HTTP, UI 위젯, print 등 I/O에 의존하지 않는다.

################################################################################
# ui_logic_dual_track_rules
################################################################################
ui_logic_dual_track_rules:
  dual_track: >
    UI(또는 boundary 표현) 변경과 로직(control/entity) 변경을 트랙으로 분리한다.
    UI 테스트는 표시·입력 경계·상태 바인딩에 집중하고,
    로직 테스트는 entity/control의 순수 동작·경계값·회귀에 집중한다.
  ui_tests:
    - boundary·presenter·포맷터 단위에서 사용자 가시 동작을 검증한다.
    - 도메인 단언은 가능하면 로직 트랙의 테스트에 둔다.
  logic_tests:
    - pytest로 entity·control의 입력-출력·예외·불변 조건을 AAA로 검증한다.
    - 동일 시나리오를 UI에서 중복 검증하지 않도록 계층을 나눈다.
  mlops:
    description: >
      실험·메트릭·재현성이 필요한 경우(예: 탐색 휴리스틱·성능 비교) 파이프라인·
      아티팩트·설정을 버전 관리하고, 도메인 로직은 여전히 entity/control에 둔다.
    must_not: entity에 인프라 SDK를 직접 박아 넣어 레이어를 깨지 않는다.

################################################################################
# tdd_rules
################################################################################
tdd_rules:
  red_phase:
    description: 새 동작·버그 수정은 실패하는 테스트로 요구사항을 고정한다.
    rules:
      - 실패하는 테스트를 먼저 추가하거나 기대값을 의도적으로 수정한다.
      - 구체 기대값·경계(빈 격자, 중복, 범위 밖 등)를 넣는다.
      - 이 단계에서는 프로덕션 코드를 넓게 작성·수정하지 않는다.
    must_not:
      - green을 위해 구현을 먼저 대량 추가하는 것
      - 테스트를 약화·삭제해 통과시키는 것
    proceed_when: 테스트가 의도대로 assertion 실패한다.
    next_phase: green_phase
  green_phase:
    description: 현재 실패 테스트를 통과시키는 최소 구현만 한다.
    rules:
      - 해당 테스트(와 직접 연쇄 실패)만 통과시키는 범위로 코드를 추가한다.
      - 통과는 실제 로직에 의한 것이어야 한다.
    must_not:
      - 구조 리팩터·이름 변경·중복 제거 등 리팩터링을 섞지 않는다.
      - 요구를 넘는 일반화·사전 최적화를 하지 않는다.
    proceed_when: 관련 테스트가 모두 통과한다.
    next_phase: refactor_phase
  refactor_phase:
    description: 관찰 가능한 동작을 유지한 채 ECB·명명·중복만 정리한다.
    rules:
      - 전후 동일 테스트 스위트가 통과해야 한다.
      - ECB 의존성 방향을 유지한다.
    must_not:
      - 새 기능·버그 수정을 이 단계에 섞지 않는다.
      - 공개 API 시맨틱을 바꾸는 변경을 하지 않는다.
    proceed_when: 전체 관련 테스트 및 커버리지 조건을 만족한다.
    next_phase: red_phase

################################################################################
# refactoring_rules
################################################################################
refactoring_rules:
  scope: 관찰 가능한 동작 불변
  practices:
    - 작은 순수 함수 추출, 명명 개선, 중복 제거
    - control과 entity 경계 재확인
  coupling: 리팩터 후에도 boundary → control → entity 단방향을 유지한다.

################################################################################
# testing
################################################################################
testing:
  framework: pytest
  pattern: AAA (Arrange-Act-Assert); 한 테스트는 한 동작·한 주된 assertion에 집중
  coverage_minimum: 80%
  fixture_scope:
    function: 기본. 격자·솔버 등 가변 상태는 function 스코프 우선
    module: 비용 큰 불변 설정만 공유
    session: 전역 가변 상태를 두지 않는다.
  naming_convention: 테스트 모듈·함수는 test_ 접두사; 클래스 기반은 Test* 접두사
  layout: tests/ 는 프로덕션 패키지 구조를 미러한다 (boundary/control/entity).

################################################################################
# forbidden
################################################################################
forbidden:
  - pattern: print()로 로깅·디버깅·사용자 메시지 출력
    reason: 테스트 불가·레이어 혼선·I/O가 entity/control에 스며든다.
    alternative: boundary에서 logging 또는 명시적 presenter; 테스트는 반환값·예외 검증
  - pattern: 비즈니스 상수·매직 넘버·문자열을 구현 본문에 하드코딩
    reason: 규격 변경 시 오류·중복·단일 진실 원천 부재
    alternative: entity의 명명된 상수·설정 객체로 한곳에 모은 뒤 참조
  - pattern: except 단독 또는 except Exception으로 광범위 삼키기
    reason: KeyboardInterrupt 등까지 삼키거나 원인 은닉으로 디버깅이 불가능해진다.
    alternative: 구체 예외를 잡고 필요 시 로깅 후 재발생; 정말 필요하면 매우 좁은 범위와 주석
  - pattern: boundary에서 행/열/대각선 합·중복 검사 등 도메인 규칙 직접 구현
    reason: ECB 위반이며 변경 시 이중 구현·불일치가 발생한다.
    alternative: entity의 순수 함수 또는 control 유스케이스를 호출한다.
  - pattern: UI 테스트와 로직 테스트를 한 거대 테스트에 뒤섞기
    reason: 실패 원인 파악이 어렵고 Dual-Track 원칙이 무너진다.
    alternative: boundary UI 테스트와 entity/control 테스트를 분리한다.

################################################################################
# file_structure
################################################################################
file_structure: |
  magic_square/
  ├── boundary/
  │   ├── __init__.py
  │   └── cli.py
  ├── control/
  │   ├── __init__.py
  │   └── solve_magic_square.py
  ├── entity/
  │   ├── __init__.py
  │   ├── grid.py
  │   └── validation.py
  └── py.typed
  tests/
  ├── boundary/
  ├── control/
  └── entity/

################################################################################
# ai_behavior
################################################################################
ai_behavior:
  before_coding:
    - 관련 테스트 파일·이름을 먼저 확인한다.
    - 변경 레이어(ECB)와 의존성 방향을 확인한다.
    - red / green / refactor 중 어느 단계인지 짧게 명시하고 해당 tdd_rules를 적용한다.
  during_coding:
    - ECB 경계 위반 금지
    - 타입 힌트·Google docstring을 public API에 유지한다.
    - Dual-Track에 맞게 UI 변경과 로직 변경을 구분한다.
  after_coding:
    - pytest로 관련 테스트를 실행해 통과를 확인한다.
    - tdd_rules 위반 시 응답에 [TDD_RULE_WARNING] 한 줄로 요약한다.

################################################################################
# review_checklist
################################################################################
review_checklist:
  - ECB 의존성 방향이 지켜졌는가
  - 공개 API에 타입 힌트와 Google docstring이 있는가
  - pytest 테스트가 AAA이고 의미 있는 assertion인가
  - UI 테스트와 로직 테스트가 적절히 분리되었는가
  - print·매직 넘버·광범위 except가 없는가
  - 커버리지 기준을 충족하는가

---

**User**

Reporter 폴더에  지금 작업한 내용을 보고서로 내보내줘.

---

**Cursor**

Reporter 폴더와 기존 보고서 형식, 현재 `.cursorrules`를 확인합니다.



채팅에서 설계한 확장 규격과 저장소의 `.cursorrules`를 비교해 보고서를 작성합니다.



`Reporter/06_magic-square-cursorrules-dual-track-mlops-expansion-report.md`에 보고서를 두었습니다.

**포함 내용:** 작업 목적·범위, 요약 표, 설계안 상위 섹션 12개 목록, 저장소 `.cursorrules`(05 스타일)와 채팅 확장안의 차이 표, Dual-Track·MLOps·TDD 요약, 관련 파일 경로, 결론(설계안은 아직 디스크 규칙 파일과 완전 일치하지 않음).

