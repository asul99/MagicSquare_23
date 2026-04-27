# Magic square implementation requirements
_Exported on 4/27/2026 at 17:29:26 GMT+9 from Cursor (3.2.11)_

---

**User**

@.cursorrules 추가 요구사항:
- MagicSquare의 핵심 도메인을 반영하라:
  - 4x4 magic square
  - 입력 검증
  - 누락값 계산
  - 합 34 검증
  - 사용자 입력 UI와 순수 계산 로직 분리
- boundary는 UI/입력/출력만 담당
- control은 유스케이스 조합과 흐름 제어만 담당
- entity는 순수 규칙/검증/계산 책임만 담당
- 테스트는 entity → control → boundary 순으로 우선순위를 둔다
- UI 구현 전 순수 로직 테스트를 먼저 작성하도록 강제한다
- mock 남용 금지, 순수 함수 우선 설계를 명시하라
- 숨은 상태보다 명시적 데이터 전달을 선호하도록 규칙화하라


---

**Cursor**

Reading `.cursorrules` to integrate the new domain and architecture requirements.



`.cursorrules`에 핵심 도메인, 레이어 역할, 테스트 우선순위, mock·명시적 데이터 규칙을 반영합니다.



`.cursorrules`에 요청하신 내용을 반영했습니다. 변경 요약만 정리합니다.

### 추가·강화된 섹션

1. **`domain.core`**  
   4×4·1–16·합 34, 입력 검증, 누락값 계산, 합 34 검증, UI와 순수 계산 분리를 항목으로 명시했습니다.

2. **`architecture.layers`**  
   - **boundary**: 역할을 “UI·사용자 입력·출력만”으로 좁히고, 웹/TUI UI를 `contains`에 포함했습니다. `must_not`에 누락값·34 검증 등 도메인 직접 구현 금지를 넣었습니다.  
   - **control**: “유스케이스 조합과 흐름 제어만”, `contains`에 “입력→검증→누락값 계산” 예시를 추가했습니다.  
   - **entity**: “순수 규칙·검증·계산만”, `contains`에 누락값 계산을 명시하고 `must_not`에 UI를 추가했습니다.

3. **`design_principles`** (신규)  
   - `pure_functions_first`: 순수 함수·동일 입출력으로 mock 없이 검증 가능하게.  
   - `mocking_policy`: mock 남용 금지, boundary 근처·최소 사용.  
   - `explicit_over_hidden_state`: 전역/숨은 설정보다 인자·반환·불변 DTO 선호.

4. **`testing`**  
   - `layer_test_priority`: entity → control → boundary.  
   - `before_ui_implementation`: UI 구현 전 entity(필요 시 control) 테스트를 먼저 Red→Green.

5. **`forbidden`**  
   entity/control 테스트에서 도메인을 mock으로 대체하는 남용을 한 항목으로 금지했습니다.

6. **`ai_behavior`**  
   도메인 키워드·테스트 우선순위·`design_principles` 준수를 `before_coding` / `during_coding`에 연결했습니다.

7. **`file_structure` 주석**  
   boundary/control/entity 설명을 위 역할과 맞췄습니다.

추가로 `tests/` 디렉터리 네이밍 순서까지 강제하진 않았습니다(미러 구조는 기존 `layout` 유지). 폴더 명 규칙까지 쓰고 싶으면 그때 한 줄 더 넣으면 됩니다.

---

**User**

Reporter 폴더에  지금 작업한 내용을 보고서로 내보내줘.

---

**Cursor**

기존 Reporter 보고서 형식을 확인한 뒤 동일한 스타일로 새 보고서를 작성합니다.



번호 체계에 맞춰 `07_...` 보고서를 작성합니다.



`Reporter/07_magic-square-cursorrules-core-domain-ecb-report.md`에 보고서를 두었습니다.

**구성:** 작성 목적·범위·참고 문서 → 작업 요약 표 → `domain` / `architecture` / `design_principles` / `testing` / `forbidden` / `file_structure` / `ai_behavior`별 반영 내용 → 05·06 보고서와의 관계 → 권장 후속.

파일 경로: `c:\DEV\MagicSquare_XXX\Reporter\07_magic-square-cursorrules-core-domain-ecb-report.md`

