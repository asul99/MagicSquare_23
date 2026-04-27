# 마방진 과제 — `User` 엔티티(ECB·entity) 구현 및 pytest 보고서

**작성 목적:** 루트 `.cursorrules`의 ECB·코드 스타일(타입 힌트·Google docstring·매직 넘버 금지)에 맞춰 **MagicSquare용 `User` 도메인 엔티티**와 **entity 단위 테스트**를 추가한 작업을 문서화한다.  
**범위:** `magic_square/entity/user.py`, 패키지 초기화·`py.typed`, `tests/entity/test_user.py`, 루트 `pyproject.toml`(패키지 메타·pytest 설정). boundary/control 구현은 포함하지 않는다.  
**참고 문서:** `Reporter/07_magic-square-cursorrules-core-domain-ecb-report.md`(도메인·ECB 규칙 기준선), 저장소 루트 `.cursorrules`.

---

## 1. 작업 요약

| 항목 | 내용 |
|------|------|
| 요청 배경 | MagicSquare 애플리케이션 맥락에서 **사용자 식별**을 표현하는 **User 엔티티**를 ECB의 **entity 레이어**에만 두고, 타입 힌트·Google 스타일 docstring·pytest 테스트 파일을 함께 제공할 것. |
| 수행 | `magic_square` 패키지 트리를 권장 구조에 맞게 생성하고, **순수 검증·불변 값 객체**로 `User`를 정의했다. I/O·UI·프레임워크 의존은 두지 않았다. |
| 검증 | `tests/entity/test_user.py`에 8개 테스트를 두었으며, 로컬에서 `py -3 -m pytest tests/entity/test_user.py -v` 실행 시 전부 통과함을 확인했다. |

---

## 2. ECB 준수 요지

| 레이어 | 본 작업에서의 위치 |
|--------|-------------------|
| **entity** | `User`, `UserValidationError`, `validate_user_id`, `validate_display_name`, `create_user` 및 필드 한계·`user_id` 패턴 상수를 **한 모듈**에 모았다. |
| **control** | 미구현. 향후 “회원 등록 유스케이스” 등에서 `create_user`를 호출하는 형태로 조합 가능. |
| **boundary** | 미구현. CLI·웹 등에서 문자열을 받아 `create_user`에 넘기기만 하면 된다. |

`.cursorrules`의 **entity `must_not`**(argparse, HTTP, UI, print 등)을 지키기 위해, 본 모듈에는 입출력 코드가 없다.

---

## 3. 도메인 규칙(요약)

- **`User`**: `@dataclass(frozen=True, slots=True)` — 불변 값 객체.
- **`create_user(user_id, display_name)`**: 양 필드에 대해 **앞뒤 공백 제거(strip)** 후 검증하고 `User` 인스턴스를 반환한다.
- **`user_id`**: 길이 `USER_ID_MIN_LENGTH`–`USER_ID_MAX_LENGTH`(1–64), 문자 집합은 `USER_ID_PATTERN`(`^[A-Za-z0-9_-]+$`)으로 제한(slug 스타일).
- **`display_name`**: 길이 `DISPLAY_NAME_MIN_LENGTH`–`DISPLAY_NAME_MAX_LENGTH`(1–80).
- **예외**: 규칙 위반 시 `UserValidationError`( `ValueError` 하위 클래스).

한계·패턴 값은 코드 상수로 두어 **매직 넘버 산재를 피했다** (`.cursorrules` `forbidden` 대안과 정합).

---

## 4. 코드 스타일·공개 API

- **Python**: 3.10+ 전제 (`from __future__ import annotations`, `slots=True` 등).
- **타입 힌트**: 공개 함수·메서드의 매개변수·반환 타입 명시.
- **docstring**: Google 스타일 — `User`, `UserValidationError`, `validate_user_id`, `validate_display_name`, `create_user`에 `Args` / `Raises` / `Returns` 등을 기술.

패키지 외부에서의 권장 import 경로 예:

- `from magic_square.entity.user import User, create_user, UserValidationError`
- 또는 `from magic_square.entity import ...` (`entity/__init__.py`의 `__all__`과 정합)

---

## 5. 산출물 목록

| 경로 | 설명 |
|------|------|
| `magic_square/__init__.py` | 패키지 루트. |
| `magic_square/py.typed` | PEP 561 타입 마커(빈 파일). |
| `magic_square/entity/__init__.py` | entity 공개 심볼 재노출. |
| `magic_square/entity/user.py` | `User` 엔티티 및 검증·팩토리(본체 약 95줄). |
| `tests/__init__.py`, `tests/entity/__init__.py` | 테스트 패키지 구조. |
| `tests/entity/test_user.py` | entity 테스트 8건(공백 strip, 최소 유효값, 빈 필드, 패턴·길이 위반, frozen 여부). |
| `pyproject.toml` | 프로젝트 메타, setuptools 패키지 탐색, `[tool.pytest.ini_options]`의 `testpaths`·`pythonpath`, optional `dev`에 pytest 의존. |

---

## 6. 테스트 실행 방법

저장소 루트 `c:\DEV\MagicSquare_XXX`에서:

```text
py -3 -m pip install -e ".[dev]"
py -3 -m pytest tests/entity/test_user.py -v
```

(환경에 따라 `python` 대신 `py -3` 사용.)

---

## 7. TDD·프로세스 메모

이번 구현은 **요청 일괄 반영**으로 테스트와 프로덕션 코드를 동일 작업 단위에서 추가했다. 저장소 `.cursorrules`의 **red → green → refactor** 엄격 순서를 적용하려면, 이후 변경은 **실패 테스트 추가 후 최소 구현** 순으로 진행하는 것이 권장된다.

---

## 8. 향후 확장 아이디어(본 보고서 범위 밖)

- persistence·세션은 **boundary**(저장소 어댑터) 또는 **control**(유스케이스)에서 다루고, entity는 식별·표시명 규칙만 유지.
- 국제화 표시명 정책(문자 종류 제한 등)이 필요하면 **상수·함수 추가 + entity 테스트**로 확장.

---

**문서 끝.**
