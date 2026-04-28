# Magic Square (4×4) — D2 단위 테스트 케이스·`red` 브랜치·GitHub 푸시 세션 보내기 보고서

**보내기 일자:** 2026-04-28  
**산출물 유형:** Reporter 폴더 아카이브용 **교육 슬라이드(D2) 정합 단위 TC 문서**, **브랜치 전략 안내**, **`red` 브랜치·원격 동기화** 작업 정리 보고서  
**관련 대화 산출:** Cursor 세션 — 원격/로컬 정합 확인, README 작업용 브랜치 전략 조언, `red` 생성, 슬라이드 형식 TC 샘플 작성, `origin` 푸시

---

## 0. 이 문서로 “직접 테스트”하기 (실습 가이드)

아래 순서대로 진행하면 **원격 정합 → pytest 실행 → TC 문서와 코드 대응 확인 → (선택) 브랜치·푸시**까지 한 번에 검증할 수 있다. 명령은 **Windows PowerShell** 기준이다. 저장소 루트는 `c:\DEV\MagicSquare_23` 등 로컬 클론 경로로 바꿔 쓴다.

**명령 표기:** **가상환경을 켠 뒤**에는 `python`·`pytest`를 쓰면 된다. 가상환경 없이 진행할 때는 같은 자리에 **`py -3`** 와 **`py -3 -m pytest`** 를 대입하면 된다.

**가상환경에서 끝까지 실행 (복사용 요약, PowerShell):**

```powershell
cd c:\DEV\MagicSquare_23
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
pytest tests\entity -q
```

위에서 `Activate.ps1`이 막히면 §0.2의 `Set-ExecutionPolicy`를 참고한다. 이후 터미널을 새로 열 때마다 **활성화 한 줄**만 다시 실행하면 된다: `cd c:\DEV\MagicSquare_23; .\.venv\Scripts\Activate.ps1`

### 0.1 사전 준비

| 항목 | 확인 방법 |
|------|-----------|
| Python | `py -3 --version` — **3.10 이상** (`pyproject.toml` `requires-python`) |
| 저장소 위치 | `cd c:\DEV\MagicSquare_23` (또는 본인 클론 경로) |

### 0.2 가상환경(venv) — 권장

프로젝트 전용 패키지를 전역 Python과 섞지 않으려면 루트에 **`.venv`** 를 두는 방식이 일반적이다. (저장소 [`.gitignore`](../.gitignore)에 `.venv/`·`venv/` 가 이미 제외되어 있다.)

**1) 한 번만: 가상환경 만들기**

```powershell
cd c:\DEV\MagicSquare_23
py -3 -m venv .venv
```

**2) 매 터미널 세션: 활성화 (PowerShell)**

```powershell
cd c:\DEV\MagicSquare_23
.\.venv\Scripts\Activate.ps1
```

활성화되면 프롬프트 앞에 `(.venv)` 가 붙는다. 이후 이 터미널에서는 `python`이 `.venv` 안의 인터프리터를 가리킨다.

**실행 정책 오류** (`Activate.ps1`이 막힐 때) — 현재 사용자에만 허용 예:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**3) 의존성 설치·pytest 확인 (가상환경 활성화 상태에서)**

```powershell
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m pytest --version
```

**4) 작업 끝낼 때 (선택)**

```powershell
deactivate
```

**가상환경을 쓰지 않는 경우:** 위 설치·실행 단계에서 `python -m pip` → `py -3 -m pip`, `python -m pytest` → `py -3 -m pytest` 로 바꿔도 된다.

### 0.3 pytest로 단위 테스트 실행 (필수 검증)

아래는 **가상환경을 활성화한 뒤** 저장소 루트에서 실행한다.

**전체 entity 테스트 (TC 문서와 직접 대응):**

```powershell
cd c:\DEV\MagicSquare_23
.\.venv\Scripts\Activate.ps1
pytest tests\entity -q
```

venv 없이: `py -3 -m pytest tests\entity -q`

**한 파일만 상세 출력:**

```powershell
pytest tests\entity\test_user.py -v
```

**테스트 수집만 확인 (실행 없이 이름 나열):**

```powershell
pytest tests\entity --collect-only -q
```

**특정 케이스만 (TC 표의 “비고” 열 함수명과 동일):**

```powershell
pytest tests\entity\test_user.py::test_create_user_strips_whitespace -v
```

**기대 결과:** 위 명령들이 **exit code 0**, 실패 0건. `docs/TC_D2_unit_magic_square_entity_user_sample.md`의 테스트 단계 표에 적힌 각 행이 `tests/entity/test_user.py`의 `test_*` 함수와 1:1로 맞는지 보면서 교육용으로 교차 검증한다.

**RED 단계 스텁** (`tests/red_phase/` 하위 **`logic/`**·**`boundary/`**·**`ui/`**, `pytest.mark.red_phase`): ECB에 맞춰 순수 규칙·유스케이스는 `logic`, 외부 계약·오류 코드는 `boundary`, 입력·표현은 `ui`에 둔다. 기본 `pytest`는 이들을 제외하고(`pyproject.toml` `addopts`) GREEN만 검증한다. **의도적으로 RED만 돌릴 때**도 가상환경을 켠 뒤 루트에서 실행한다.

```powershell
cd c:\DEV\MagicSquare_23
.\.venv\Scripts\Activate.ps1
pytest -m red_phase tests\red_phase -v
```

venv 없이: `py -3 -m pytest -m red_phase tests\red_phase -v` — **전부 실패**가 정상(`logic`·`boundary`·`ui` 스텁이 각각 `pytest.fail` 한 줄만 가짐; 건수는 스텁 추가에 따라 변동).

### 0.3a 가상환경에서 평가(검증) 방법

**전제:** §0.2대로 `.venv`를 만들고 **활성화**한 뒤 `python -m pip install -e ".[dev]"`까지 완료했다고 본다. 평가는 **항상 활성화된 터미널**에서 수행한다.

| 단계 | 하는 일 | 합격(통과) 기준 |
|------|---------|-----------------|
| 1. 도구 확인 | `python -c "import sys; print(sys.executable)"` | 경로에 **`.venv`**가 포함됨 (전역 Python이 아님). |
| 2. GREEN 회귀 | `pytest tests\entity -q` | **exit code 0**, 실패 0, 경고만으로 중단되지 않음. |
| 3. 전체 스위트(선택) | `pytest tests -q` | **8 passed**, `red_phase`는 deselect(기본 설정). |
| 4. TC 추적성 | `docs/TC_D2_unit_magic_square_entity_user_sample.md` 표 **비고** 열과 `tests\entity\test_user.py`의 `test_*` 이름 대조 | 행마다 1:1 대응(누락·이름 불일치 없음). |
| 5. RED 스텁(의도 실패) | `pytest -m red_phase tests\red_phase -q` | **전부 실패**가 정상(스켈레톤 유지 시). GREEN 구현 후에는 이 항목을 평가에서 제외하거나 마커를 조정한다. |
| 6. 커버리지(선택) | `python -m pip install pytest-cov` 후 `pytest tests\entity --cov=magic_square.entity --cov-report=term-missing -q` | 팀·`.cursorrules`의 하한(예: 80%) 이상이면 통과로 기록. |

**실패 시 기록:** 터미널에 남은 **마지막 30줄**과 `pytest … -v` 한 번 재실행 결과를 제출물에 붙인다.

**수강·자기점검용 한 줄:** “가상환경 켰는지 → `pytest tests\entity -q`가 0인지 → TC 표와 함수명이 맞는지” 순으로 보면 된다.

### 0.4 TC 문서 열고 따라 읽기

1. 브라우저 또는 에디터로 [`docs/TC_D2_unit_magic_square_entity_user_sample.md`](../docs/TC_D2_unit_magic_square_entity_user_sample.md)를 연다.  
2. **표지·식별** 표에서 테스트 ID `TC-MS-ENTITY-001` 등을 확인한다.  
3. **테스트 단계** 표의 **비고** 열에 있는 함수명을 복사해 `0.3`의 `::함수명` 실행으로 하나씩 돌려 본다.  
4. **환경·조건** 표의 전제 조건 문구대로 `pytest tests/entity -q`가 통과하는지 확인한다 (경로는 Windows에서 `tests\entity`로 동일). 가상환경을 쓰는 경우 **§0.2 활성화 후** 같은 명령을 실행하면 된다.

### 0.5 Git: 원격과 로컬 정합 확인 (세션 재현)

저장소가 GitHub `asul99/MagicSquare_23`를 `origin`으로 쓰는 경우 예시:

```powershell
cd c:\DEV\MagicSquare_23
git remote -v
git fetch origin
git status
git branch -vv
```

**확인 포인트:**

- `origin`의 fetch URL이 `https://github.com/asul99/MagicSquare_23.git` (또는 팀이 쓰는 동일 URL)인지  
- `git status`로 **추적 파일 미커밋 변경**이 있는지 (README만 다를 수 있음)  
- `main` 작업 시 `git rev-parse HEAD`와 `git rev-parse origin/main`이 같은지 (`git fetch` 후 비교)

> **참고:** 세션 초기에 보고된 커밋 SHA(`45f6538…` 등)는 **그 시점의 스냅샷**이다. 지금 로컬이 앞서 있거나 뒤처져 있으면 SHA는 다르다. “정합”의 의미는 **같은 브랜치 포인터가 같은 커밋을 가리키는지**로 판단하면 된다.

### 0.6 `red` 브랜치 실습 (선택)

문서·TC만 올리는 연습용으로 `red` 브랜치를 쓰려면:

```powershell
git checkout main
git pull origin main
git checkout -b red
# 파일 수정 후
git add docs\TC_D2_unit_magic_square_entity_user_sample.md
git commit -m "docs: D2 unit TC sample (example)"
git push -u origin red
```

GitHub에서 PR을 열려면(저장소·계정 기준):  
`https://github.com/asul99/MagicSquare_23/pull/new/red`

`main`에 합치기: PR에서 Merge 또는 로컬에서 `main`으로 merge 후 `git push origin main`.

### 0.7 문제 발생 시 빠른 점검

| 증상 | 조치 |
|------|------|
| `pytest`를 찾을 수 없음 | **가상환경 활성화 여부** 확인 (`(.venv)` 프롬프트). 활성화 후 `python -m pip install -e ".[dev]"` 재실행. venv 없이면 `py -3 -m pip install -e ".[dev]"` 및 `py -3 -m pytest` |
| `Activate.ps1` 실행 불가 | §0.2의 `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` 참고 |
| `ModuleNotFoundError: magic_square` | 루트에서 실행하는지 확인; `pyproject.toml`에 `pythonpath = ["."]` 설정됨 |
| 테스트가 수집되지 않음 | 파일명 `test_*.py`, 함수명 `test_*` 규칙 확인 ([`tests/entity/test_user.py`](../tests/entity/test_user.py) 참고) |

---

## 1. 보내기 요약

| 구분 | 내용 |
|------|------|
| **작업명** | (1) GitHub `asul99/MagicSquare_23`와 로컬 커밋 정합 확인, (2) README·문서 작업용 브랜치 전략 제안, (3) **`red`** 브랜치 생성·체크아웃, (4) D2 실습 슬라이드와 동일 항목 구조의 **단위 테스트 케이스 문서** 추가, (5) **`origin/red`** 푸시 |
| **핵심 산출 파일** | [`docs/TC_D2_unit_magic_square_entity_user_sample.md`](../docs/TC_D2_unit_magic_square_entity_user_sample.md) |
| **Git** | 로컬 브랜치 `red`; 원격 추적 `origin/red`; 문서 반영 커밋은 세션에서 `12fef42` (*시점별로 SHA는 변경될 수 있음*) |
| **요구·도메인 SoT** | 마방진 본 기능·FR·오류 코드는 [`docs/PRD_MagicSquare_4x4_TDD.md`](../docs/PRD_MagicSquare_4x4_TDD.md); 본 TC 샘플은 ECB 예시 **`magic_square.entity.user`** 및 [`tests/entity/test_user.py`](../tests/entity/test_user.py)에 대응 |
| **추적·README 맥락** | [`Reporter/20_magic-square-readme-todo-traceability-session-export-report.md`](20_magic-square-readme-todo-traceability-session-export-report.md) — 슬라이드·RTM·TASK ID 정합; 본 세션의 TC 표는 동일 교육 맥락(D2 실습)에서 **문서화 템플릿** 역할 |

---

## 2. 원격(GitHub)과 로컬 정합(세션 초기)

| 확인 항목 | 결과 |
|-----------|------|
| `origin` URL | `https://github.com/asul99/MagicSquare_23.git` — 요청 URL과 일치 |
| 기본 브랜치 | GitHub·로컬 모두 `main` |
| `main` 최신 커밋(세션 시점) | SHA `45f6538…` — 로컬 `HEAD`/`origin/main`과 일치 *(현재는 `git fetch` 후 비교로 재확인)* |
| 워킹 트리 | 세션 초기에는 루트 `README.md` 로컬 수정 가능성 언급; **`red`에서 문서 커밋 시점**에는 추적 대상이 TC 신규 파일 중심 |

**GitHub 저장소 메타(참고):** 설명 필드 예시 `작성자:정재훈, 리뷰어:홍길동`, 주 언어 Python — 클론 메타이며 TC 샘플 표지의 작성자·승인자 예시와 정렬.

---

## 3. 브랜치 전략(세션에서 제안한 요지)

| 상황 | 권장 |
|------|------|
| 혼자·즉시 반영 | `main`에서 README만 수정 후 푸시 가능 |
| PR·이력 분리 | `main` 갱신 후 `docs/readme-…` 등 **짧은 수명 브랜치** → PR → merge (**GitHub Flow**) |
| 장기 `develop`/Git Flow | 본 저장소 규모·README·문서 위주 작업에는 과함 |

사용자 요청에 따라 실제 작업 브랜치 이름은 **`red`** 로 고정(문서 작업·RED 단계 연상 등 팀 내 의미에 맞게 사용 가능).

---

## 4. `red` 브랜치 및 Git 이력

| 항목 | 값 |
|------|-----|
| 생성 명령 | `git checkout -b red` (이전 브랜치에서 분기) |
| 문서 커밋(세션) | `12fef42` — *docs: add D2 unit test case sample for entity user (slide layout)* |
| 원격 푸시 | `git push -u origin red` — **`red` → `origin/red`** (최초 푸시 시 네트워크 재시도 후 성공) |
| PR 생성 URL(참고) | `https://github.com/asul99/MagicSquare_23/pull/new/red` |

`main`에 병합하려면 위 PR로 merge하거나, 로컬에서 `main`으로 merge 후 `git push origin main` 절차를 따르면 된다.

---

## 5. 단위 테스트 케이스 문서(`docs/TC_D2_…`) 구조

슬라이드 **「D2_2. Practice — Magic Square 테스트 케이스 작성」** 예시(프로젝트명·대상 시스템·단계·작성자·승인자·문서 상태·작성일·버전·테스트 범위·조직·테스트 ID·일자·목적·기능·입력값·**테스트단계 표**·환경·전제·성공·실패·특별 절차)를 **Markdown 표**로 재현.

| 절 | 내용 |
|----|------|
| 표지·식별 | Magic Square (4×4) TDD, 대상 `entity.user`, 단위 테스트, 작성자·승인자 예시(정재훈·홍길동), v1.0, 작성일 2026-04-28 |
| 테스트 단계 | 열: **테스트 케이스 / 예상값 / 중요도 / 성공·실패 / 비고** — 각 행을 `test_user.py`의 테스트 함수와 대응 |
| 환경·조건 | Python 3.10+, pytest, 전제·성공·실패 기준·특별 절차 |
| 빈 양식 | 마방진 PRD 기반 TC를 같은 형식으로 확장할 수 있도록 하단에 **복사용 뼈대** 포함 |

**범위:** 슬라이드의 **사칙연산** 수치 예는 본 저장소 코드와 무관하므로, 대신 **이미 존재하는 단위 테스트**로 치환해 실습 형식만 유지했다.

**TC ↔ pytest 매핑 빠른 참조**

| TC 표 “비고” (함수명) | 한 줄 실행 예 (venv 활성화 후) |
|------------------------|----------------|
| `test_create_user_strips_whitespace` | `pytest tests\entity\test_user.py::test_create_user_strips_whitespace -v` |
| `test_create_user_valid_minimal` | 동일 패턴으로 `::함수명` 교체 |
| 나머지 6개 | `test_user.py` 내 `def test_...` 이름과 동일하게 지정 |

venv 없이 실행할 때는 위에서 `pytest` → `py -3 -m pytest` 로 바꾼다.

---

## 6. 연계 문서·코드

| 경로 | 본 세션과의 관계 |
|------|------------------|
| `docs/TC_D2_unit_magic_square_entity_user_sample.md` | 세션 산출 TC 문서 |
| `tests/entity/test_user.py` | TC 표의 근거 테스트 |
| `README.md` | 문서 맵·스택·Reporter 인덱스; **선택:** 문서 맵 표에 본 `Reporter/21` 한 줄 추가 |
| `Reporter/18` | TASK·FR 추적 SoT |
| `Reporter/20` | README·슬라이드·RTM 세션과 개념 연속 |
| `docs/PRD_MagicSquare_4x4_TDD.md` | 빈 TC 양식으로 확장할 마방진 요구의 근거 |
| `pyproject.toml` | `[tool.pytest.ini_options]` — `testpaths = ["tests"]`, `pythonpath = ["."]` |

---

## 7. 후속 권장(선택)

- `README.md` **문서 맵**에 `Reporter/21`(본 보고서) 및 필요 시 `docs/TC_D2_…` 한 줄을 추가해 탐색성을 맞춘다.  
- `red`를 `main`에 합친 뒤에는 기본 작업 브랜치를 `main`으로 되돌리거나, 이후 문서 전용 브랜치 네이밍(`docs/…`)을 팀 규칙으로 통일한다.  
- PRD **FR·BR-ERR** 단위로 `TC_D2` 하단 빈 양식을 복사해 **마방진 전용 TC ID**(예: `TC-MS-GRID-001`)를 발급·추적한다.

---

## 8. 변경 이력(Reporter)

| 일자 | 내용 |
|------|------|
| 2026-04-28 | 초안: D2 TC 문서·`red`·GitHub 푸시·원격 정합·브랜치 전략 세션 보내기 |
| 2026-04-28 | 개정: **§0 실습 가이드** 추가 — 환경 준비, pytest·Git 명령, TC 문서 교차 검증, 트러블슈팅, SHA 스냅샷 주의, TC↔pytest 표 |
| 2026-04-28 | 개정: **§0.2 가상환경(venv)** 절차 — 생성·활성화·의존성·`deactivate`, PowerShell 실행 정책, venv 없을 때 `py -3` 대안; §0.3~번호 정렬 및 트러블슈팅 보강 |
| 2026-04-28 | 개정: **가상환경 복사용 요약 블록** 및 **§0.3 RED 스텁** (`pytest -m red_phase`) venv / 비venv 명령 |
| 2026-04-28 | 개정: RED 스텁 경로를 `tests/red_phase/logic|boundary|ui`(ECB 정렬)로 분리·보강 |
| 2026-04-28 | 개정: **§0.3a 가상환경에서 평가(검증) 방법** — 실행 경로 확인, GREEN/RED·TC·커버리지(선택) 기준 표 |
