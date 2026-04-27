# TDD rules section in YAML
_Exported on 4/27/2026 at 16:58:51 GMT+9 from Cursor (3.2.11)_

---

**User**

위 .cursorrules 파일의 tdd_rules 섹션을 채워줘.
  - red_phase: 테스트 먼저 작성, 실패 확인 후 다음 단계 진행 조건
  - green_phase: 최소 코드로만 테스트 통과, 이 단계에서 리팩터링 금지
  - refactor_phase: 기능 변경 없이 구조 개선, 커버리지 유지 조건
YAML 형식 유지. tdd_rules 블록만 출력해.


---

**Cursor**

`.cursorrules` 파일에서 `tdd_rules` 섹션 구조 확인 중입니다.



워크스페이스에 `.cursorrules`가 없어, 요청하신 Red–Green–Refactor 규칙을 YAML로 정리했습니다. 아래 `tdd_rules` 블록만 사용하시면 됩니다.

```yaml
tdd_rules:
  red_phase:
    summary: 실패하는 테스트를 먼저 작성한다.
    steps:
      - 새 동작·버그 수정은 항상 실패하는 테스트로 시작한다.
      - 테스트는 구체적인 기대값·경계 조건을 포함한다.
      - 프로덕션 코드는 이 단계에서 작성·수정하지 않는다(테스트만 추가·수정).
    proceed_when:
      - 해당 테스트가 실행되며 실패한다(컴파일 오류가 아닌, 의도된 assertion/기대 실패).
      - 실패 원인이 “아직 구현되지 않음”과 일치한다(거짓 실패·환경 문제가 아님).
      - 실패 메시지가 다음 구현 대상을 명확히 가리킨다.
    next_phase: green_phase

  green_phase:
    summary: 테스트를 통과시키는 데 필요한 최소한의 프로덕션 코드만 작성한다.
    rules:
      - 목표는 오직 현재 실패 중인 테스트를 통과시키는 것이다.
      - 이 단계에서는 리팩터링을 하지 않는다(이름 변경, 추출, 구조 정리, 스타일 정리 금지).
      - 필요 이상의 일반화·추가 기능·사전 최적화를 하지 않는다.
      - 테스트를 약하게 만들거나 삭제하여 통과시키지 않는다.
    proceed_when:
      - 관련 테스트 스위트가 모두 통과한다.
      - 통과가 테스트 완화가 아닌 실제 구현에 의한 것이다.
    next_phase: refactor_phase

  refactor_phase:
    summary: 동작은 그대로 두고 구조만 개선한다.
    rules:
      - 관찰 가능한 동작·공개 API 시맨틱을 바꾸지 않는다.
      - 버그 수정·새 기능은 이 단계에 넣지 않는다(필요하면 red_phase로 돌아간다).
      - 중복 제거, 명명 개선, 모듈 경계 정리, 의존성 방향 정리 등 구조 개선만 수행한다.
    coverage:
      - 리팩터 전후로 동일 테스트가 통과해야 한다.
      - 기존 테스트로 커버되던 분기·경로가 약화되지 않도록 한다(필요 시 테스트 보강은 동작 동일 전제 하에서만).
      - 커버리지 지표는 리팩터 전 대비 낮아지지 않는 것을 조건으로 한다(측정 가능한 경우).
    proceed_when:
      - 전체 관련 테스트가 통과하고, 커버리지 조건을 만족한다.
      - 다음 기능은 다시 red_phase부터 시작한다.
    next_phase: red_phase
```

---

**User**

Reporter 폴더에  지금 작업한 내용을 보고서로 내보내줘.

---

**Cursor**

Reporter 폴더의 기존 보고서 명명 규칙을 확인한 뒤 TDD 규칙 보고서를 추가합니다.



작업 내용(`.cursorrules`의 `tdd_rules` 정의)을 Reporter에 `03` 번호로 보고서로 저장합니다.



`Reporter`에 아래 보고서를 추가했습니다.

**파일:** [Reporter/03_magic-square-cursorrules-tdd-rules-report.md](c:\DEV\MagicSquare_XXX\Reporter\03_magic-square-cursorrules-tdd-rules-report.md)

**구성:** 작성 목적·범위, red/green/refactor 요약 표, 채워 둔 `tdd_rules` 전체 YAML, `.cursorrules`에 붙일 때 들여쓰기·도구 연동용 짧은 메모입니다. 기존 `01_`·`02_` 보고서와 같은 톤으로 맞춰 두었습니다.

