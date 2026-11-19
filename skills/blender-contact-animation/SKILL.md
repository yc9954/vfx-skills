---
name: blender-contact-animation
description: Build or repair Blender character rigs, locomotion, dance, expressive motion and prop interactions with anatomical calibration and contact-aware transitions. Includes public mocap retargeting, native prop ownership, evaluated shoe/cloth contact repair, conditional Kimodo and engine transfer; review-only faults belong to animation-causality-review and render-only work to film-render-delivery.
---

# Blender 접촉·동작 제작

동작의 원인과 지지 관계를 먼저 설계하고 그 위에 연기를 만든다. 분석만 요청되면
장면을 수정하지 않는다. 제작에서는 기존 리깅·재질·자산을 점검해 재사용하고 원본을 보존한다.

사람의 도달·하중·균형·그립을 설계할 때는 설치된 공통 지식층
[`human-motion-biomechanics`](../human-motion-biomechanics/SKILL.md)의 해당 reference로
동작 계약을 먼저 만든다. 공통층은 ROM/하중/지지의 의미를 소유하고, 이 스킬은 그 계약을
실제 Blender 포즈·IK·접촉·제약과 evaluated mesh로 구현한다.

연기 의도·키포즈·타이밍·시선·표정·secondary motion을 새로 설계하거나 전달받았다면
[`character-performance-animation`](../character-performance-animation/SKILL.md)의 performance
contract/version을 입력으로 사용한다. 그 스킬은 “살아 있는가”를 설계하고, 이 스킬은
biomechanics floor와 접촉을 지키며 블로킹/리그/곡선으로 구현한다.

## 작업 모드

- 사람의 이동/도구 상호작용: [contact-and-acting.md](references/contact-and-acting.md).
- 자연스러운 연기, 다채로운 동작, 춤/음악 동기화, 군무, 동작 사이 전이:
  [natural-motion-and-dance.md](references/natural-motion-and-dance.md).
  사용 목적에 따라 실연/모캡·조건 생성·키프레임을 선택하고 리듬과 지지 상태를 함께 설계한다.
  성격·thought beat·key pose·gaze/face 자체의 설계는 공통 performance skill에서 가져온다.
- 새 인체 리그, 자동 리깅 검증, 발·무릎·골반·척추·어깨 문제, 여러 행동에 쓸 리그:
  [full-body-biomechanics.md](references/full-body-biomechanics.md)를 읽는다.
  관절별 축/변형과 전신 협응을 분리해 확인하고, 필요한 행동별 사용 가능 범위를 남긴다.
- 손가락 리깅, 손목 비틀림, 소품 집기/운반: 추가로
  [hand-biomechanics.md](references/hand-biomechanics.md)를 읽는다. 뼈 개수나
  손목 IK 도달만으로 손을 승인하지 않고, 해부학적 축과 물체별 지지 방식을 먼저 보정한다.
- 들어 올리기·운반·붓기·밀기·당기기처럼 하중이 중요한 행동:
  공통 [동작 계약](../human-motion-biomechanics/references/motion-language.md)과
  [하중·균형](../human-motion-biomechanics/references/load-balance-and-handling.md)을 함께 읽는다.
- Kimodo 기능 조사·생성 방식 선택: [kimodo-capabilities.md](references/kimodo-capabilities.md).
  멈칫거림·클립 경계 문제는 [kimodo-continuity.md](references/kimodo-continuity.md)를 함께 읽는다.
- BVH/FBX 리타깃과 단위: [motion-and-units.md](references/motion-and-units.md).
- 공개 모캡으로 교체, 소품 그룹/지지 전환, 신발·의상 관통 또는 접촉 보정 회귀:
  [mocap-and-contact-repair.md](references/mocap-and-contact-repair.md)를 함께 읽는다.
  소스 사용 사실, 리타깃 성공, 실제 그립·접지와 정상속도 연기를 별도로 확인한다.
- Unreal 이전이 실제 요청됐거나 Blender로 필요한 기능을 구현할 수 없을 때:
  [engine-transfer.md](references/engine-transfer.md).

선택한 작업의 참조만 읽는다. 한 번의 걷기 수정 때문에 새 엔진을 설치하거나 모션 모델을 다시 받지 않는다.

## 장면 계약

- 길이 단위, 업/전방 축, FPS, 캐릭터 신장과 접시 크기, 접촉 허용오차를 먼저 기록한다.
  필요한 손가락·발 구름·몸통/목 움직임을 실제로 제어할 수 있는지 확인한다.
  본 이름/개수와 자동 리깅 완료만으로 관절 중심·축·스킨의 타당성을 판단하지 않는다.
- 고정된 월드, 배우의 루트, 사지 포즈, 소품 지지 상태를 분리한다.
  손잡이와 발의 목표를 단순 루트 좌표와 혼동하지 않는다.
- 실제 지지 표면을 사용한다. 접시 안/테두리/밖의 높이를 한 Z 평면으로 대체하지 않는다.
  지면 레이캐스트가 캐릭터 자신의 몸이나 다른 배우를 맞히지 않도록 대상 집합을 지정한다.
- 모델링된 구멍/입구를 막는 볼록 충돌체, 시각 메시보다 작은 루트 충돌체를 먼저 확인한다.
- 동작마다 지지 주체를 명시한다: 선반→손, 물/바닥→망, 망→낙하→그릇.
  visibility, parenting, constraint influence, dynamic/kinematic 전환을 시간표로 남긴다.
- 사람-소품 동작에는 `prop/load assumption | start support | grip roles | working range |
  kinetic chain | weight transfer | end support/velocity`를 기록한다. 하중을 모르면 kg를
  지어내지 말고 `unknown`으로 두되, 화면에 필요한 지지와 노력의 단서는 명시한다.
- 전달받은 연출 비트의 목적·시선·결과를 실제 지지 전환과 연결한다. 블록아웃은
  상세 장식보다 실루엣·출입 경로·그립·열린 용기 기하를 우선한다. 원기둥의 경로가
  매끈하다는 사실을 사람의 보행이나 손 접촉이 완성됐다는 증거로 쓰지 않는다.
- performance contract의 story pose와 dominant accent를 stepped blocking에서 먼저 확인한다.
  지지/접촉 포즈가 성립한 뒤 breakdown, spacing, overlap, facial/hand detail 순으로 발전시키며,
  spline smoothing이 포즈 대비·pause·successive joint order를 지우면 다시 블로킹으로 돌아간다.
- 음식·유체 장면에서는 실제 용기 입구, emitter/receiver, 가림/충돌 경로와 조작 타이밍을
  이 스킬이 구현한다. 점도·분열·파동·입자 스케일·wetness/SSS의 연출/QA는 설치된
  `food-vfx-director`의 계약을 입력으로 받되, 그 프롬프트가 기하 검증을 대신하지 않는다.

## 제작과 검사

1. complete interaction의 저비용 버전을 만든다. 준비와 놓기를 뺀 예쁜 가운데 부분만 검사하지 않는다.
2. key pose/실루엣과 지지 발·그립·진행 방향·체중 이동을 함께 조율한 후 breakdown과
   secondary/tertiary motion을 더한다. 디테일은 primary action의 읽힘을 경쟁하지 않는다.
3. 저장된 장면을 다시 열어 evaluated mesh/bone 기준으로 측정한다. 제작 함수의 목표값을
   동일 함수와 비교하는 자체 확인만으로 성공 판정하지 않는다.
4. 실제 이동 방향, 지지 발 드리프트, 발바닥 틈/침투, 손잡이 도달, 사지 길이,
   소품의 조기 이동·순간 등장, 경계 프레임 속도, 관련 충돌 쌍을 검사한다.
   단위·구간·표면·시간 샘플링과 빠진 범위를 함께 기록한다.
5. 실제 후보가 생기면 수치 확인 후 정상속도 연기와 확대 접촉을 별도로 검토한다. 설치된
   `animation-causality-review`가 있으면 납품 전에 사용한다. 없으면 같은 범위를 직접 검토한다.

## 물리라는 표현

이 작업이 키네마틱 접촉 애니메이션인지, 강체/천/유체 시뮬레이션인지, 하이브리드인지 명시한다.
애니메이션된 메시를 물리엔진에 넣거나 충돌체를 생성했다는 사실만으로 반응이 생기지 않는다.
점프·물·운반의 힘까지 검증하지 않았다면 “물리적으로 완벽”이라고 부르지 않는다.
의도적인 점프를 매 프레임 바닥에 붙여 없애거나 관통을 카메라로 숨기는 수정은 하지 않는다.

## 다음 단계로 넘길 것

다단계 제작/재개에서는 [공통 인계 규약](../miniature-film-director/references/handoff-contract.md)을 따른다.
저장 장면 버전, 변경한 리그/지오메트리/동작, 자체 측정 범위와 후보 파일, 남은 문제를 넘긴다.
관련된 이전 검사만 stale로 처리한다. 아직 만들지 않은 영상의 품질을 통과로 기록하지 않는다.
동반 스킬이 없으면 기존 프로젝트 기록에 이 항목을 남긴다. 단순 검토만으로 기록을 갱신하지 않는다.
