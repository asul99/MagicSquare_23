# 단위 테스트 케이스 (작성 예시)

> D2 실습 슬라이드(사칙연산 예)와 **동일한 항목 구조**를 따르되, 본 저장소는 **Magic Square 4×4 TDD** 및 ECB 예시 모듈 `magic_square.entity.user`에 맞춰 채움.  
> 실제 과제용 표는 이름·ID·일자·테스트단계 행을 복사해 확장하면 된다.

---

## 표지·식별

| 항목 | 내용 |
|------|------|
| **프로젝트명** | Magic Square (4×4) TDD 훈련 |
| **대상 시스템** | `magic_square` 패키지 — ECB `entity` 계층 (`user` 모듈) |
| **단계** | 단위 테스트 |
| **작성자** | 정재훈 |
| **승인자** | 홍길동 |
| **문서 상태** | 초안 |
| **작성일** | 2026-04-28 |
| **버전** | v1.0 |
| **테스트 범위** | 공통·도메인 엔티티 검증 (`create_user`, `validate_*`) |
| **테스트 조직** | 개발팀 |

| 항목 | 내용 |
|------|------|
| **테스트 ID** | TC-MS-ENTITY-001 |
| **테스트 일자** | 2026-04-28 |
| **테스트 목적** | 사용자 엔티티 생성 시 공백 제거·길이·문자 규칙이 계약대로 동작하는지 검증 |
| **테스트 기능** | `create_user(user_id, display_name)` — ID/표시명 정규화 및 검증 |
| **입력값** | `(user_id, display_name)` 쌍 예: `("  alice_1  ", "  Alice  ")`, `("a","B")`, `("   ","Name")`, `("valid_id","  \\t  ")`, `("bad id","X")`, `("x"*33,"ok")` 등 |

---

## 테스트 단계

| 테스트 케이스 | 예상값 | 중요도 | 성공/실패 | 비고 |
|---------------|--------|--------|-----------|------|
| `create_user("  alice_1  ", "  Alice  ")` | `User(user_id="alice_1", display_name="Alice")` | 상 | | `tests/entity/test_user.py` `test_create_user_strips_whitespace` |
| `create_user("a", "B")` | `User(user_id="a", display_name="B")` | 상 | | `test_create_user_valid_minimal` |
| `create_user("   ", "Name")` | `UserValidationError`, 메시지에 `user_id must not be empty` | 상 | | `test_create_user_rejects_empty_user_id_after_strip` |
| `create_user("valid_id", "  \\t  ")` | `UserValidationError`, 메시지에 `display_name must not be empty` | 상 | | `test_create_user_rejects_empty_display_name_after_strip` |
| `validate_user_id("bad id")` | `UserValidationError`, 메시지에 `letters, digits` | 중 | | `test_validate_user_id_rejects_invalid_characters` |
| `validate_user_id("x" * (USER_ID_MAX_LENGTH+1))` | `UserValidationError`, 메시지에 `at most` | 중 | | `test_validate_user_id_rejects_too_long` |
| `validate_display_name("n" * (DISPLAY_NAME_MAX_LENGTH+1))` | `UserValidationError`, 메시지에 `at most` | 중 | | `test_validate_display_name_rejects_too_long` |
| `User` 인스턴스 필드 재할당 시도 | `AttributeError` (frozen) | 하 | | `test_user_is_frozen` |

*(슬라이드의 `1+10` → `11` 형식과 같이, **케이스 / 기대 / 중요도 / 결과 / 비고** 열을 유지한다.)*

---

## 환경·조건

| 항목 | 내용 |
|------|------|
| **테스트 환경** | Python 3.10+ · pytest · OS: Windows 10 (또는 팀 표준) · IDE: 팀 표준 |
| **전제 조건** | 1) `pyproject.toml` 기준 의존성 설치 완료. 2) 저장소 루트에서 `pytest tests/entity -q` 가 실패 없이 수집됨. |
| **성공/실패 기준** | **성공:** 위 표의 모든 케이스가 예상값·예외·메시지와 일치. **실패:** 하나라도 불일치. |
| **특별 절차** | 실패 시 로그·스택을 이슈에 첨부하고 수정 후 동일 ID 케이스로 재실행. 문서의 성공/실패 열을 갱신. |

---

## 마방진 본체(FR)용 빈 양식 (복사용)

아래는 **격자 완성·오류 코드** 등 PRD 기반 TC를 추가할 때 같은 표를 쓰기 위한 뼈대다.

| 항목 | 내용 |
|------|------|
| **프로젝트명** | |
| **대상 시스템** | |
| **단계** | 단위 테스트 |
| **작성자** | |
| **승인자** | |
| **문서 상태** | |
| **작성일** | |
| **버전** | |
| **테스트 범위** | |
| **테스트 조직** | |
| **테스트 ID** | |
| **테스트 일자** | |
| **테스트 목적** | |
| **테스트 기능** | |
| **입력값** | |

### 테스트 단계

| 테스트 케이스 | 예상값 | 중요도 | 성공/실패 | 비고 |
|---------------|--------|--------|-----------|------|
| | | | | |
| | | | | |

근거 요구·오류 문구: [`docs/PRD_MagicSquare_4x4_TDD.md`](PRD_MagicSquare_4x4_TDD.md), 추적·Task 매핑: [`Reporter/20_magic-square-readme-todo-traceability-session-export-report.md`](../Reporter/20_magic-square-readme-todo-traceability-session-export-report.md).
