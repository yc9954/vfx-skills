# 세션 기반 스킬 보강 · 2026-11-19

등록된 VFX 스킬 12개를 유지하고, 제작 중 반복된 문제의 수리·검증 기준을 담당 스킬에
추가했다. 기존 이미지 중심 제작·합성 변경도 함께 보존했다. 원본 영상·모델·Blender 장면,
계정·인증정보·모션 데이터는 이 소스 업데이트에 포함하지 않는다.

## 스킬별 반영 범위

| 스킬 | 반영한 내용 / 유지한 책임 |
|---|---|
| [miniature-film-director](../skills/miniature-film-director/SKILL.md) | 최신 이야기·투사 치수와 등장 시점의 버전 연결, 제한된 완결 행동 시험, 선택한 제작 경로와 접시별 분리·합성 |
| [film-reference-breakdown](../skills/film-reference-breakdown/SKILL.md) | 스토리 개정과 외형 참고 역할 구분, 물 경계·불꽃의 관찰 항목 |
| [visual-image](../skills/visual-image/SKILL.md) | 이미지/Tripo 출처·실제 부피·분리 부품 맞물림, 배경 크롭, 물/소품 재질 통합, 현재 프로젝트 시점 유지 |
| [visual-video](../skills/visual-video/SKILL.md) | 이미지 중심 또는 Blender 경로 선택, 선택적 프리비즈, 전경 분리 후 배경 합성 |
| [animation-causal-staging](../skills/animation-causal-staging/SKILL.md) | 필수 프리비즈 강제 제거, 이미지·행동 기반 경로와 범위별 적용 사례 |
| [character-performance-animation](../skills/character-performance-animation/SKILL.md) | 기존 의도·시선·키포즈·타이밍·겹침 연기 계약 유지; 이번 변경에서 본문 수정 없음 |
| [human-motion-biomechanics](../skills/human-motion-biomechanics/SKILL.md) | 기존 인체·하중·지지 계약 유지; 구현 스킬에 지식을 중복하지 않음; 본문 수정 없음 |
| [food-vfx-director](../skills/food-vfx-director/SKILL.md) | 조개·관자·전복 구조 구분, 나중 등장하는 재료, 들어 올리는 중 조리 변환과 최종 음식 정체성 |
| [blender-contact-animation](../skills/blender-contact-animation/SKILL.md) | 공개 모캡의 실제 사용 구간, 리타깃 전이, 순환 없는 소품 제어, 신발 전체·소매 수리, 악화된 보정의 복귀 |
| [blender-seedance-handoff](../skills/blender-seedance-handoff/SKILL.md) | 이미지·행동 지시와 선택적 가이드의 역할, 선택한 모델 유지, 현재 합성 흐름과 예산 경계 |
| [animation-causality-review](../skills/animation-causality-review/SKILL.md) | 저장 장면의 실제 표면·제외 영역·검사 구간, 제어 관계 시험, 잘못된 전체 승인 반례 |
| [film-render-delivery](../skills/film-render-delivery/SKILL.md) | 불변 장면·외부 의존성, 구간별 재개, 실제 프로세스 상태와 모션/beauty 출력 구분 |

상세 새 참조:

- [모캡과 접촉 수리](../skills/blender-contact-animation/references/mocap-and-contact-repair.md)
- [평가된 접촉 근거](../skills/animation-causality-review/references/evaluated-contact-evidence.md)
- [생성 배경과 재질 통합](../skills/visual-image/references/generated-set-integration.md)
- [식재료 정체성과 변환](../skills/food-vfx-director/references/ingredient-identity-and-transformations.md)

생물학과 모캡 채널 설명의 출처는 각 참조에 연결했다. 제작상의 수리 규칙은 세션 경험을
일반화한 지침이며, 특정 수치·카메라 각도·실패한 보정법을 전역 규칙으로 만들지 않았다.
상속한 Visual Skills의 LICENSE·NOTICE·SOURCE와 원저자 표기는 유지했다.

## 실행한 검증

| 검사 | 결과와 범위 |
|---|---|
| `vfx.py skills validate` | 등록 12개, frontmatter·라우팅·로컬 Markdown 링크 통과 |
| skill-creator `quick_validate.py` | 12개 통과; UI short description 길이와 default prompt의 스킬 참조도 확인 |
| 공통 unittest | Python 3.12.13, 24개 통과; 유료 제공자는 모킹 |
| phrase timing | Python 3.12.13, 11개 통과 |
| media receipt | Python 3.12.13 및 로컬 FFmpeg/FFprobe, 10개 통과 |
| joint DOF audit | Blender 4.5.13 LTS의 Python에서 합성 관절 13개 통과 |
| whole-tile composition | Python 3.12.13, NumPy/Pillow 및 FFmpeg/FFprobe, 4개 통과: 프레임·180° 회전·원본 보존, 기존 출력 보존, 중첩 거부, 페더 영역의 전경 감지 |
| 게시 검사 | Git index 172개 소스 파일의 `check_publish.py`, whitespace 및 변경된 Markdown의 로컬 링크 검사 통과 |

별도 에이전트 2개에는 수정 의도나 기대 정답을 주지 않고, 스킬과 합성 입력만 전달했다.

| 적용 사례 | 실제 응답에서 확인한 판단 |
|---|---|
| 구버전 해시, 4개 샘플, 소매 제외, Foot-only 메시, 독립 소품 곡선과 모캡 크레딧이 있는 보고서 | 전체 무관통/자연스러움 승인 거부; 버전·범위·실제 표면·제어·연기를 구분하고 미관찰 상태를 유지 |
| 현재 60° 투사 브리프, 다른 시리즈 75° 지침, 선택한 배경 크롭, 단일 이미지 전복, 후반 등장과 새우 조리 변환 | 현재 치수·60°와 이미지 크롭을 유지; 턴테이블과 다중 입력을 구분; 최신 이야기 미접근을 명시하고 지지·등장·변환 검사로 인계 |

이는 제한된 텍스트 적용 시험이다. 실제 전체 영화의 정상속도 연기·관통·재질을 검수한
결과가 아니다. 관절 검사는 합성 리그에 한정하고, 타일 합성 검사는 전경 제거·물리 투사
캘리브레이션을 검증하지 않는다. 신규 유료 생성, 원격 GPU 작업과 본편 렌더는 실행하지 않았다.

위 결과는 로컬 검증이다. CI 설치나 원격 자동 테스트의 성공을 대신 주장하지 않는다.
