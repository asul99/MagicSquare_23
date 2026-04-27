# User entity class in ECB pattern
_Exported on 4/27/2026 at 17:33:42 GMT+9 from Cursor (3.2.11)_

---

**User**

.cursorrules를 읽고
MagicSquare의 User 엔티티 클래스를 ECB 패턴으로 작성해줘.
타입힌트, Google docstring, pytest 테스트 파일도 함께 만들어줘.


---

**Cursor**

`.cursorrules`와 프로젝트 구조를 확인한 뒤 User 엔티티와 테스트를 ECB에 맞게 추가합니다.



Python 패키지가 없어 `.cursorrules`의 ECB 권장 구조로 `magic_square` 패키지와 `User` 엔티티를 추가합니다.



`test_user.py`의 들여쓰기 오류를 수정하고, `pyproject.toml`에서 없는 `README.md` 참조를 제거합니다.



## 요약

`.cursorrules`의 ECB 권장 구조에 맞춰 **entity 레이어만** `User` 값 객체와 검증 함수를 두었습니다. I/O·UI·프레임워크 없이 순수 도메인 규칙만 담습니다.

### 추가된 파일

| 경로 | 역할 |
|------|------|
| `magic_square/entity/user.py` | `User` frozen dataclass, `UserValidationError`, `validate_user_id`, `validate_display_name`, `create_user`, 명명된 상수 |
| `magic_square/entity/__init__.py` | public 심볼 재노출 |
| `magic_square/__init__.py`, `magic_square/py.typed` | 패키지 루트·타입 마커 |
| `tests/entity/test_user.py` | 8개 pytest 케이스 |
| `pyproject.toml` | 패키지 메타·pytest `pythonpath`·optional `dev` |

### 설계 요점

- **`User`**: `@dataclass(frozen=True, slots=True)` — 불변 값 객체.
- **`create_user`**: 양 끝 공백 제거 후 검증하고 `User` 반환.
- **`user_id`**: 길이 1–64, `^[A-Za-z0-9_-]+$` (slug 스타일, 상수·패턴으로 한곳 관리).
- **`display_name`**: strip 후 길이 1–80.
- **예외**: `UserValidationError(ValueError)` — 경계에서 잡기 쉽게.

핵심 코드는 다음과 같습니다.

```1:95:c:\DEV\MagicSquare_XXX\magic_square\entity\user.py
"""Domain entity for an application user (MagicSquare context).

This module is entity-layer only: no I/O, frameworks, or UI dependencies.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

# Single source of truth for user field limits (see .cursorrules: no magic numbers).
USER_ID_PATTERN: re.Pattern[str] = re.compile(r"^[A-Za-z0-9_-]+\Z")
USER_ID_MIN_LENGTH: int = 1
USER_ID_MAX_LENGTH: int = 64
DISPLAY_NAME_MIN_LENGTH: int = 1
DISPLAY_NAME_MAX_LENGTH: int = 80


class UserValidationError(ValueError):
    """Raised when ``User`` invariants are violated."""


@dataclass(frozen=True, slots=True)
class User:
    """Immutable identity for a person using MagicSquare.

    Attributes:
        user_id: Stable account identifier (slug-style, ASCII).
        display_name: Human-readable name shown in the app.
    """

    user_id: str
    display_name: str


def validate_user_id(user_id: str) -> None:
    ...


def validate_display_name(display_name: str) -> None:
    ...


def create_user(user_id: str, display_name: str) -> User:
    ...
```

### 테스트 실행

프로젝트 루트에서:

`py -3 -m pip install -e ".[dev]"`  
`py -3 -m pytest tests/entity/test_user.py -v`

로컬에서 **8 passed** 확인했습니다.

---

**[TDD_RULE_WARNING]** 이번 작업은 요청대로 엔티티와 테스트를 한 번에 반영했습니다. 엄격한 Red→Green 순서를 지키려면, 다음 변경부터는 실패하는 테스트를 먼저 추가한 뒤 구현을 맞추는 흐름을 권장합니다.

---

**User**

Reporter 폴더에  지금 작업한 내용을 보고서로 내보내줘.

---

**Cursor**

Reporter 폴더의 기존 보고서 형식을 확인한 뒤 동일한 스타일로 보고서를 작성합니다.



기존 보고서(07번) 형식에 맞춰 `08`번 보고서를 작성합니다.



`Reporter` 폴더에 **08번** 보고서를 추가했습니다.

- **파일:** `c:\DEV\MagicSquare_XXX\Reporter\08_magic-square-user-entity-ecb-implementation-report.md`

**포함 내용:** 작성 목적·범위·참고 문서, 작업 요약 표, ECB(entity만) 정리, `User` 도메인 규칙 요약, 타입/docstring 정책, 생성·수정 파일 목록, pytest 실행 명령, TDD 프로세스 메모, 향후 확장 메모. 기존 `07_...` 보고서와 같은 톤·표 중심 구조로 맞춰 두었습니다.

