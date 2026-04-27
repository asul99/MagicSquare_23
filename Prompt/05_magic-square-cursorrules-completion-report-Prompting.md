# MagicSquare project cursorrules completion
_Exported on 4/27/2026 at 17:17:59 GMT+9 from Cursor (3.2.11)_

---

**User**

@Reporter/04_magic-square-cursorrules-tdd-rules-review-report.md 에서 만든 .cursorrules 뼈대의 빈 섹션을 모두 채워줘.
MagicSquare 프로젝트 기준으로 작성해.

각 섹션 작성 규칙:

code_style:
  - python_version: "3.10+"
  - style_guide: PEP8 엄격 준수
  - type_hints: 모든 함수 파라미터와 반환값에 필수
  - docstring: Google 스타일, 모든 public 메서드에 필수
  - max_line_length: 88 (Black 기준)

architecture:
  ECB 패턴 3 레이어를 각각 정의해줘:
  - boundary: 외부 입출력 담당 (UI, API, CLI)
  - control: 비즈니스 로직 담당
  - entity: 도메인 데이터 및 규칙 담당
  레이어 간 의존성 방향도 명시해줘.

tdd_rules:
  지금은 문자열 1줄인데, 하위 항목으로 세분화해줘.
  각 phase마다:
    - description: 단계 설명
    - rules: 지켜야 할 규칙 목록
    - must_not: 이 단계에서 하면 안 되는 것

testing:
  - framework: pytest
  - pattern: AAA (Arrange-Act-Assert)
  - coverage_minimum: 80%
  - fixture_scope: 규칙 정의
  - naming_convention: test_ 접두사 필수

forbidden:
  항목마다 아래 구조로 작성:
    pattern: 금지 패턴
    reason: 금지 이유
    alternative: 대신 써야 할 것
  최소 포함 항목: print(), 하드코딩 상수, except 단독 사용

file_structure:
  ECB 기준 폴더 구조를 트리 형태 주석으로 작성해줘.
  boundary/, control/, entity/, tests/ 포함.

ai_behavior:
  Cursor AI가 코드 생성 전·중·후에 반드시 따라야 할 규칙.
  최소 포함:
    - 코드 작성 전 관련 테스트 파일 확인
    - ECB 레이어 경계 위반 금지
    - 타입힌트 없는 함수 생성 금지
    - tdd_rules 위반 시 경고 출력

완성된 .cursorrules 전체 파일을 출력해줘.


---

**Cursor**

리뷰 리포트와 기존 `.cursorrules` 확인 중입니다.



MagicSquare 프로젝트 기준으로 `.cursorrules`를 작성해 저장합니다.



‘1–34’ 표현이 모호해 마방진 맥락(1–16, 합 34)으로 명확히 수정합니다.



워크스페이스 루트에 `c:\DEV\MagicSquare_XXX\.cursorrules`로 저장했고, 04 보고서에서 지적된 **Unicode 곱따옴표**는 쓰지 않았습니다. `forbidden`의 `reason`에 있던 오타성 표현(1–34)은 **1–16·마방진 합 34**로 바로잡았습니다.

아래가 **완성된 `.cursorrules` 전체**입니다.

```yaml
# MagicSquare (4×4 마방진) — Cursor 프로젝트 규칙
# ECB + TDD + pytest. 본 파일은 에이전트·편집기 지침으로 사용한다.

project:
  name: MagicSquare
  description: >
    4×4 격자에 1–16을 한 번씩 배치해 행·열·주대각선 합이 동일한 마방진을
    탐색·검증·표현한다. 도메인 규칙과 입출력은 ECB로 분리한다.

code_style:
  python_version: "3.10+"
  style_guide: PEP8 엄격 준수 (공백, 네이밍, import 정렬 등)
  type_hints: 모든 함수·메서드의 파라미터와 반환값에 필수 (Any 남용 금지, 도메인에는 구체 타입)
  docstring: Google 스타일, 모든 public 클래스·함수·메서드에 필수
  max_line_length: 88
  formatter_linter: Black(88)·ruff/isort 권장, 저장 시 포맷 일관성 유지

architecture:
  pattern: ECB (Entity–Control–Boundary)
  layers:
    boundary:
      role: 외부 입출력 담당
      contains:
        - CLI 인자 파싱·프롬프트·표 형식 출력
        - HTTP/API 핸들러(해당 시)
        - 파일·스트림 읽기/쓰기 어댑터
      must_not: 행/열/대각선 합·중복 검사 등 도메인 규칙을 직접 구현하지 않는다. control/entity 호출만 한다.
    control:
      role: 유스케이스·비즈니스 흐름 담당
      contains:
        - "한 해 찾기", "모든 해 열거", "격자 검증" 등 오케스트레이션
        - 탐색 전략 선택·가지치기 호출 순서
      must_not: 프레임워크·콘솔에 직접 의존하지 않는다. boundary는 주입·호출 경계로만 둔다.
    entity:
      role: 도메인 데이터·불변 규칙 담당
      contains:
        - 격자 표현, 마방진 상수, 유효성·부분 배치 불변 조건
        - 순수 함수 위주의 검증·합산·인덱스 규칙
      must_not: argparse, HTTP, print 등 I/O에 의존하지 않는다.
  dependency_direction: >
    boundary → control → entity.
    entity는 다른 레이어를 알지 않는다.
    control은 entity만 직접 의존하고, boundary는 control(또는 얇은 파사드)만 호출한다.
    역방향 의존성(예: entity가 CLI 타입 참조)은 금지한다.

tdd_rules:
  red_phase:
    description: >
      새 동작·버그 수정은 반드시 “아직 통과하지 않는” 테스트로 시작한다.
      실패가 곧 요구사항의 계약이 된다.
    rules:
      - 새 기능·수정은 실패하는 테스트 추가(또는 기대값 수정)로 시작한다.
      - 테스트에 구체 기대값·경계(빈 격자, 거의 완성, 중복, 범위 밖 등)를 넣는다.
      - 프로덕션 코드는 이 단계에서 작성·수정하지 않는다(테스트만 추가·수정).
      - 실패는 컴파일/임포트 오류가 아니라 assertion·의도된 기대 실패여야 한다.
    must_not:
      - green을 위해 구현 코드를 먼저 쓰거나 대량 수정하지 않는다.
      - 테스트를 의미 없이 약화하거나 삭제해 “통과”로 만드는 행위.
      - 실패 원인이 환경·플레이크인데 구현 문제로 가장하는 것.
    proceed_when:
      - 해당 테스트가 실행되며 의도대로 실패한다.
      - 실패가 “미구현”과 일치하고 메시지가 다음 구현 대상을 가리킨다.
    next_phase: green_phase

  green_phase:
    description: >
      현재 실패 중인 테스트를 통과시키기 위한 최소 구현만 한다.
      구조 미화·일반화는 다음 refactor에서 한다.
    rules:
      - 목표는 오직 그 테스트(및 직접 연쇄 실패)를 통과시키는 것이다.
      - 필요한 만큼만 프로덕션 코드를 추가·수정한다.
      - 통과는 실제 로직에 의한 것이어야 하며, 테스트 완화로 얻지 않는다.
    must_not:
      - 리팩터링(이름 변경, 추출, 구조·스타일 정리, 중복 제거 미화)을 하지 않는다.
      - 요구를 넘는 일반화·추가 기능·사전 최적화.
      - 테스트 기대 완화·삭제로 통과시키기.
    proceed_when:
      - 관련 테스트 스위트가 모두 통과한다.
      - 통과가 구현에 의한 것임을 스스로 점검한다.
    next_phase: refactor_phase

  refactor_phase:
    description: >
      관찰 가능한 동작과 공개 계약은 유지한 채 ECB 경계·명명·중복만 정리한다.
    rules:
      - 모든 테스트가 리팩터 전후 동일하게 통과해야 한다.
      - ECB 의존성 방향을 지키며 control/entity 경계를 명확히 한다.
      - 중복 제거, 명명 개선, 작은 순수 함수 추출 등 구조만 변경한다.
    must_not:
      - 새 기능·버그 수정을 이 단계에 섞지 않는다(필요 시 red_phase로 돌아간다).
      - 공개 API 시맨틱·검증 결과 의미를 바꾸는 변경.
      - 커버리지·분기 커버를 의도적으로 줄이는 변경(측정 시).
    coverage:
      - 리팩터 전후 동일 테스트 통과.
      - 기존에 커버되던 분기가 약화되지 않도록 한다.
      - 측정 가능하면 프로젝트 testing.coverage_minimum 이상을 유지한다.
    proceed_when:
      - 전체 관련 테스트 통과 및 커버리지 조건 만족.
      - 다음 기능은 다시 red_phase부터 시작한다.
    next_phase: red_phase

testing:
  framework: pytest
  pattern: AAA (Arrange-Act-Assert); 한 테스트는 한 동작·한 주된 assertion에 집중
  coverage_minimum: 80%
  fixture_scope:
    function: 기본. 격자·솔버·임시 상태는 테스트 간 오염 방지를 위해 function 스코프 우선.
    module: 동일 모듈에서 비용 큰 불변 설정(예: 읽기 전용 참조 테이블)만 공유.
    session: 드물게만 사용. 전역 가변 상태를 session fixture로 두지 않는다.
    package: 사용하지 않는 것을 원칙으로 한다.
  naming_convention: 테스트 모듈·함수는 test_ 접두사 필수; 클래스 기반 테스트는 Test* 접두사.
  layout: 프로덕션은 src 또는 패키지 루트와 tests/ 미러 구조를 권장한다.

forbidden:
  - pattern: print()로 로깅·디버깅·사용자 메시지 출력
    reason: 테스트 불가·레이어 혼선·I/O가 entity/control에 스며듦
    alternative: boundary에서 logging 또는 명시적 presenter/formatter; 테스트는 capsys보다 반환값·예외 검증 우선
  - pattern: 비즈니스 상수·매직 넘버·문자열을 구현 본문에 하드코딩
    reason: 4×4·1–16·마방진 합 34 등 규칙 변경 시 오류·중복; 단일 진실 원천 부재
    alternative: entity의 명명된 상수(예: 크기 4, 값 범위 1–16, 마방진 합 34)·설정 객체로 한곳에 모은 뒤 참조
  - pattern: except 단독 사용 (except: 또는 except Exception 광범위 삼키기)
    reason: KeyboardInterrupt 등까지 삼키거나 원인 은닉으로 디버깅 불가
    alternative: 구체 예외 타입을 잡고 필요 시 로깅 후 재발생; 정말 광범위면 마지막에 한 줄 주석과 함께 매우 좁은 범위에서만

file_structure: |
  # MagicSquare — ECB 기준 권장 트리 (주석)
  #
  # magic_square/
  # ├── boundary/           # CLI, API, 파일 I/O
  # │   ├── __init__.py
  # │   └── cli.py
  # ├── control/            # 유스케이스, 탐색 오케스트레이션
  # │   ├── __init__.py
  # │   └── solve_magic_square.py
  # ├── entity/             # 격자, 규칙, 순수 검증
  # │   ├── __init__.py
  # │   ├── grid.py
  # │   └── validation.py
  # └── py.typed            # (선택) 패키지 타입 마커
  #
  # tests/
  # ├── boundary/
  # ├── control/
  # └── entity/

ai_behavior:
  before_coding:
    - 관련 도메인(마방진 검증·탐색)의 기존 테스트 파일·테스트 이름을 먼저 확인한다.
    - 변경 대상 레이어(ECB)와 의존성 방향을 확인한 뒤 그 범위 안에서만 수정한다.
    - red/green/refactor 중 어느 단계에 해당하는지 짧게 명시하고 그 단계의 tdd_rules를 적용한다.
  during_coding:
    - ECB 레이어 경계 위반 금지(entity에 I/O, boundary에 도메인 규칙 등).
    - 타입 힌트 없는 함수·메서드 생성 금지(public·private 모두).
    - Google 스타일 docstring을 public API에 유지한다.
  after_coding:
    - pytest 실행 경로를 안내하거나 실행해 관련 테스트가 통과함을 확인한다.
    - tdd_rules 위반(예: red 없이 구현만 추가, green에서 리팩터 혼입)이 있으면 응답에 경고 문구를 명시한다.
  tdd_violation_warning: >
    규칙 위반 가능성이 있으면 본문에 [TDD_RULE_WARNING] 접두로 한 줄 요약한 뒤
    어떤 phase 규칙을 어겼는지와 권장 수정 순서를 적는다.
```

**참고:** `control`의 `must_not`에 있는 “boundary는 주입·호출 경계로만 둔다”는 문장은 **control이 콘솔/API에 직접 달라붙지 말고 I/O 경계는 boundary 쪽으로만 둔다**는 뜻으로 읽으면 됩니다. 패키지 이름(`magic_square/`)은 실제 레포 루트에 맞게 바꿔도 됩니다.

---

**User**

Reporter 폴더에  지금 작업한 내용을 보고서로 내보내줘.

---

**Cursor**

기존 Reporter 문서 형식을 확인한 뒤 보고서를 작성합니다.



`Reporter/05_` 번호로 완료 보고서 작성 중입니다.



`Reporter/05_magic-square-cursorrules-completion-report.md`에 보고서를 두었습니다.

**포함 내용**
- **작업 요약:** 04 이후 `.cursorrules` 전체 작성·저장, 03과의 정합, 유니코드 따옴표 미사용·도메인 표기 정리
- **섹션별 반영:** `project`, `code_style`, `architecture`, `tdd_rules`, `testing`, `forbidden`, `file_structure`, `ai_behavior`가 요구사항에 어떻게 맞춰졌는지 표·문단으로 정리
- **선행 문서:** 01·03·04와의 관계
- **후속 권장:** 패키지명 정합, CI 커버리지, `forbidden` vs green 운영 시 조정

경로: `c:\DEV\MagicSquare_XXX\Reporter\05_magic-square-cursorrules-completion-report.md`

