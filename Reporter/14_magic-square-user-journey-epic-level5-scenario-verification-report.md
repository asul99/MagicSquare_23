# Magic Square 사용자 여정 — Level 5 시나리오 검증 및 정리

**작성 일자:** 2026-04-28  
**산출물 유형:** Reporter 폴더 — Epic 하위 **시나리오 완성도·엣지·사용자 중심·구현 가능성** 검증 체크리스트  
**관련 원본:**  
`Reporter/09_magic-square-user-journey-epic-business-goal-report.md` ~ `Reporter/13_magic-square-user-journey-epic-level4-export-report.md` (Level 1~4와 정합)

---

**작성 목적:** Level 1(Epic) → Level 2(Journey) → Level 3(Story) → Level 4(Gherkin Technical)까지의 **추적 가능성**과 **테스트·구현 준비도**를 한 장으로 점검한다.

**범위:** 본 Epic(Invariant 기반 사고 훈련, 4×4 Magic Square 도메인)에 한정한다. 순수 도메인·TDD 훈련 맥락이므로, **현장/네트워크형 제품** 항목은 해당 시 **범위 외(N/A)** 또는 **동등 검증**으로 치환하여 표기한다.

---

## 시나리오 완성도 체크리스트 (요약 형식)

### ✅ 4레벨 일관성 확인

**Epic → Journey**

- [x] Epic의 성공 지표가 Journey에 반영됨
- [x] Journey의 모든 단계가 Epic 목표 달성에 기여
- [x] Pain Points가 명확히 정의됨 (여정 서술 내 마찰 요인; 별도 Pain 표는 선택)

**Journey → Story**

- [x] Journey의 각 Stage마다 최소 1개 Story (흐름상 전 구간을 Story 집합이 포괄)
- [x] Story가 구체적인 기능으로 변환됨
- [x] Acceptance Criteria가 측정 가능

**Story → Technical**

- [x] 모든 AC가 Gherkin 시나리오로 변환 (핵심 AC 포괄; 일부는 Background·Then에 통합)
- [x] Given-When-Then이 명확
- [x] 테스트 자동화 가능

### ✅ Edge Case 커버리지

**정상 케이스**

- [x] Happy Path 시나리오 존재

**예외 케이스**

- [ ] 네트워크 오류 (순수 도메인 범위에서는 N/A; 경계 연계 시 추가)
- [ ] 권한 없음 (동일; 인증 유스케이스 연계 시 추가)
- [x] 잘못된 입력
- [x] 중복 실행 (순·역 두 조합 시도)

**경계 케이스**

- [x] 최솟값, 최댓값
- [x] 빈 값 (빈칸 `0` 개수·전제)
- [ ] 특수 문자 (숫자 격자 전제; 문자열 경계 시 확장)

### ✅ 사용자 중심성

**실제 사용자 검증**

- [ ] 현장 엔지니어 1명과 시나리오 리뷰
- [ ] 관리자 1명과 Journey 검증
- [ ] 피드백 반영

**감정 흐름**

- [x] 각 Journey Stage마다 감정 표시 (서술상 흐름: 혼란 → 구조화 → 안정)
- [x] 부정 → 긍정 전환 명확

### ✅ 구현 가능성

**기술 검증**

- [x] QR 스캔 라이브러리 조사 완료 → **본 Epic 치환:** 4×4 격자·빈칸·좌표·결과 배열 계약 확정
- [x] 오프라인 DB 방식 결정 → **본 Epic 치환:** 순수 도메인 + pytest 검증 경로
- [x] 자동 검증 알고리즘 설계 (Validator·Solver·탐색 조합)

**데이터 요구사항**

- [x] 필요한 Entity 모두 정의됨 (Mission 2) — `User` 및 격자 계약
- [x] API 스펙 초안 작성 → **본 Epic 치환:** 입·출력 스키마·예외 정책 (Level 2 표)

---

## 시나리오 완성도 체크리스트 (상세)

### 4레벨 일관성 확인

#### Epic → Journey

| 항목 | 상태 | 근거·비고 |
|------|:----:|-----------|
| Epic의 성공 지표가 Journey에 반영됨 | [x] | DoD(커버리지·계약 테스트·하드코딩·매직넘버·Invariant↔Test 추적)가 Step 2(계약)·4(Dual-Track)·5(회귀)에 분산 반영됨 (`09`/`10`). |
| Journey의 모든 단계가 Epic 목표 달성에 기여 | [x] | 문제 인식 → 계약 → Domain 분리 → Dual-Track → 회귀 보호가 Invariant·TDD·Clean Architecture 목적과 직접 대응 (`09` §Level 2). |
| Pain Points가 명확히 정의됨 | [x] | 전용 “Pain” 표는 없으나, Step 1·2·5에서 **암묵적 동작·계약 불명확·회귀 부재** 등 마찰이 서술됨. (별도 Pain 표 추가 시 가독성 향상 가능) |

#### Journey → Story

| 항목 | 상태 | 근거·비고 |
|------|:----:|-----------|
| Journey의 각 Stage마다 최소 1개 Story | [x] | 5 Step과 5 Story가 1:1 라벨은 아니나, **흐름상** Step 1~2→Story 1, Step 3→Story 2·3·4, Step 4~5→Story 5 및 회귀·계약 스토리로 **전 구간 커버** (`10`·`11`). |
| Story가 구체적인 기능으로 변환됨 | [x] | 입력 검증·빈칸·누락 숫자·판정·두 조합 시도로 경계가 나뉨 (`11`). |
| Acceptance Criteria가 측정 가능 | [x] | AC가 예외/개수/정렬/합 일치/배열 길이 등 **검증 가능한 서술**로 기술됨 (`11`). |

#### Story → Technical

| 항목 | 상태 | 근거·비고 |
|------|:----:|-----------|
| 모든 AC가 Gherkin 시나리오로 변환 | [x] | Level 4의 Background·시나리오 5건이 Story 1~5와 매핑 표로 대응 (`12`/`13` §Level 3 매핑). (세부 AC 일부는 Background·Then 절에 통합 표현) |
| Given-When-Then이 명확 | [x] | Feature·Background·Data Table·단계별 And/Then 구조 명시 (`12`). |
| 테스트 자동화 가능 | [x] | pytest·Cucumber 등 **결정적 입력·기대값**으로 자동화 가능한 서술 (`12`). |

---

### Edge Case 커버리지

#### 정상 케이스

| 항목 | 상태 | 근거·비고 |
|------|:----:|-----------|
| Happy Path 시나리오 존재 | [x] | 작은 수→큰 수 순 배치 완성, 역순 배치 완성 (`12` 시나리오 2건). |

#### 예외 케이스

| 항목 | 상태 | 근거·비고 |
|------|:----:|-----------|
| 네트워크 오류 | [ ] | 본 Epic **순수 도메인·로컬 테스트** 범위에서는 N/A. API·경계 레이어 도입 시 별도 시나리오 추가 권장. |
| 권한 없음 | [ ] | 도메인 Solver 퍼즐 범위에서는 N/A. **인증·RBAC** 유스케이스 연계 시 `User`/boundary와 함께 정의 (`08` 참고). |
| 잘못된 입력 | [x] | 빈칸 개수 오류·범위 위반·중복 (`12` 시나리오 3~5). |
| 중복 실행 | [x] | “두 조합 시도”(순·역 배치)로 **동일 입력에 대한 전략적 재시도**가 시나리오화됨 (`11` Story 5, `12`). |

#### 경계 케이스

| 항목 | 상태 | 근거·비고 |
|------|:----:|-----------|
| 최솟값, 최댓값 | [x] | 값 도메인 1~16, 상수 34, 16 초과 시 실패 (`12` Background·범위 시나리오). |
| 빈 값 | [x] | 빈칸 `0` 정확히 2개 전제; 1개만 있을 때 실패 (`12`). |
| 특수 문자 | [ ] | **숫자 격자** 전제로 Gherkin에 미포함. 문자열 경계 입력 시 boundary 파싱 시나리오로 확장 권장. |

---

### 사용자 중심성

#### 실제 사용자 검증

| 항목 | 상태 | 근거·비고 |
|------|:----:|-----------|
| 현장 엔지니어 1명과 시나리오 리뷰 | [ ] | 페르소나는 **개발 학습자** 중심; 현장 엔지니어 리뷰는 미실시. |
| 관리자 1명과 Journey 검증 | [ ] | 동일 이유로 미실시. 교육·코치 역할자 리뷰로 치환 가능. |
| 피드백 반영 | [ ] | 상기 리뷰 미수행으로 본 항목 보류. |

#### 감정 흐름

| 항목 | 상태 | 근거·비고 |
|------|:----:|-----------|
| 각 Journey Stage마다 감정 표시 | [x] | 서술상 **혼란(암묵적 목표) → 구조화(계약·분리) → 안정(회귀)** 흐름이 단계 목표로 읽힘. (별도 이모지·감정 맵 미첨부) |
| 부정 → 긍정 전환 명확 | [x] | “그림 그리기” 수준에서 **불변·계약 중심 문제**로의 전환(Step 1), 실패 입력 처리·완성 시나리오(Step 5)로 **불안정 → 검증 가능** 전환이 명시됨 (`09`). |

---

### 구현 가능성

#### 기술 검증

| 항목 | 상태 | 근거·비고 |
|------|:----:|-----------|
| QR 스캔 라이브러리 조사 완료 | [x] | **치환:** 4×4 격자·`0` 빈칸·1-index 좌표·길이 6 결과 등 **입력·출력 계약**이 Level 2~4에 고정됨 (본 도메인에 QR 없음). |
| 오프라인 DB 방식 결정 | [x] | **치환:** 외부 DB 없이 **순수 도메인 + pytest**로 검증·회귀 경로 확보 (Epic 성격과 정합). |
| 자동 검증 알고리즘 설계 | [x] | BlankFinder·MissingNumberFinder·Validator·Solver 조합 및 순·역 시도가 Story·Gherkin에 반영 (`09` Step 3, `11`·`12`). |

#### 데이터 요구사항

| 항목 | 상태 | 근거·비고 |
|------|:----:|-----------|
| 필요한 Entity 모두 정의됨 (Mission 2) | [x] | `User` 엔티티 및 ECB entity 레이어 보고 (`08`); 격자·빈칸은 도메인 타입·계약으로 Level 2~4에 정의. |
| API 스펙 초안 작성 | [x] | **치환:** 공개 경계 API가 없어도 **입력 스키마·출력 스키마·예외 정책**이 Level 2 표로 초안화됨 (`09` Step 2). REST/OpenAPI 추가 시 본 항목 확장. |

---

## 요약

| 구역 | 완료 요지 |
|------|-----------|
| **4레벨 일관성** | Epic ↔ Journey ↔ Story ↔ Gherkin 매핑 유지, AC 측정 가능. |
| **엣지** | Happy·잘못된 입력·경계(값·빈칸)·조합 재시도 커버. 네트워크·권한·특수문자는 범위 확장 시 보강. |
| **사용자 중심** | 서술적 감정·전환은 있음; **외부 이해관계자 리뷰**는 미실시. |
| **구현 가능성** | 도메인 중심 기술·데이터 전제 충족; 제품형 항목은 동등 검증으로 치환 표기. |

---

## 관련 Reporter 산출물

| 파일 | 역할 |
|------|------|
| `Reporter/09_magic-square-user-journey-epic-business-goal-report.md` | Level 1·2 작업본 |
| `Reporter/10_magic-square-user-journey-epic-level2-export-report.md` | Level 1·2 보내기 |
| `Reporter/11_magic-square-user-journey-epic-level3-user-stories-report.md` | Level 3 |
| `Reporter/12_magic-square-user-journey-epic-level3-export-report.md` | Level 3 보내기 |
| `Reporter/12_magic-square-user-journey-epic-level4-technical-scenarios-report.md` | Level 4 작업본 |
| `Reporter/13_magic-square-user-journey-epic-level4-export-report.md` | Level 4 보내기 |
| `Reporter/14_magic-square-user-journey-epic-level5-scenario-verification-report.md` | Level 5 작업본(본 문서) |
| `Reporter/15_magic-square-user-journey-epic-level5-export-report.md` | Level 5 보내기 |

---

## 문서 이력

| 일자 | 내용 |
|------|------|
| 2026-04-28 | Level 5 시나리오 검증·정리 체크리스트 초안 작성 |
| 2026-04-28 | 요약 형식(✅·Epic→Technical·엣지·사용자·구현) 섹션 추가 및 상세 표와 병기 |
| 2026-04-28 | 보내기 보고서 `15_magic-square-user-journey-epic-level5-export-report.md` 생성 (본문 동일) |
