---
name: blender-seedance-handoff
description: Prepare and run requested Higgsfield video generation, extension or editing from images and action prompts, with optional Blender or motion guides, clip continuity and credit accounting. Use for direct image-to-video and hybrid generation stages; preserve the selected model. Not for Blender-only construction or a review-only question about an existing clip.
---

# 이미지·선택한 가이드 → Higgsfield 제작

이미지와 행동 프롬프트로 직접 제작하거나, 선택한 가이드를 지원 입력 역할로 함께 사용한다.
Blender 가이드를 쓰는 경우 동작·배치·접촉의 지시로 삼고 이미지로 외형·재질을 정한다.
생성 모델이 물리를 보장한다고 가정하지 않는다.
사용자가 Blender만 요청했다면 이 경로를 추가하지 않는다.
반대로 Higgsfield 최종 영상을 요청했다면 유효한 기존 가이드/레퍼런스를 재사용하고 실제
제출·회수 단계까지 진행한다. 직접 이미지→영상 경로에 새 Blender 제작을 의무화하지 않는다.
반복 파일별 제출 스크립트 대신 공통 실행기/기존 안전한 장부를 쓰고,
[산출물 우선 규약](../miniature-film-director/references/deliverable-routing.md)을 적용한다.

## 실행 전

- 최신 제작 방식과 입력을 [제작 루프](../miniature-film-director/references/collaborative-production-loop.md)에서
  복원한다. 현재 테이블 작업은 Nano Banana 접시/기존 엔티티 이미지→Kling 장면→접시별 배경 제거·
  경계 보정→네 좌석 배치→선택한 배경 합성이다. 분리 단계에서는
  [접시별 합성 지침](../miniature-film-director/references/per-plate-compositing.md)을 따른다.
  제공된 배경에 로컬 합성하며 생성형 배경 편집은 요청한 경우에 선택한다.
  새 Blender 프리비즈나 대조본 컨펌을 선행 조건으로 추가하지 않는다.
  사용자가 요청한 창작 컨펌과 이미 부여한 범위를 지키며, 창작 컨펌은 비용 승인과 구분한다.

- 현재 설치된 CLI/커넥터와 인증 상태를 확인한다. 로그인 완료 발언만으로 API 접근을
  가정하지 않는다. 도구 도움말·현재 서비스 문서로 모델, 길이, 해상도, 입력 영상 지원,
  extension 방식과 가격을 확인한다. 없는 명령이나 모델 기능을 지어내지 않는다.
- 사용자가 실제 선택한 서비스와 계정을 유지한다. 로그인 막힘은 정확한 오류와 로그인
  경로를 제시한다. 인증정보를 프롬프트·스크립트·공유 문서에 복사하지 않는다.
- 실행 전 [continuity-and-budget.md](references/continuity-and-budget.md)를 읽는다.
  과거의 크레딧 잔액과 예산을 현재 가용액으로 취급하지 않는다.
- 프롬프트 작성/수정 시 [prompt-execution-boundary.md](references/prompt-execution-boundary.md)를 읽는다.
  촬영·편집·CG 연출문, 실제 모델 설정, Blender/후반작업 지시를 분리한다.
  전문용어의 수가 아니라 화면에서 확인할 변화와 유지 조건을 기준으로 쓴다.
- Blender에서 확정한 배치·기하·접촉·카메라를 생성 모델에 넘길 때는
  [geometry-contact-contract.md](references/geometry-contact-contract.md)를 읽어 고정/허용 항목,
  실제 입력 버전과 후보 비교 기준을 명시한다. “reference”라는 단어만으로 보존을 가정하지 않는다.
- 사람의 들어 올리기·운반·붓기·도구 사용이 있으면 공통
  [human-motion contract](../human-motion-biomechanics/references/motion-language.md)의 버전과
  grip roles, 작업 범위, 지지 발, 하중 가정, 체중 이동, phase order를 함께 고정한다.
  Blender에서 확정된 이를 AI가 “더 자연스럽게” 다시 설계하도록 맡기지 않는다.
- character acting이 중요하면
  [performance beat packet](../character-performance-animation/assets/performance-beat-packet.md)의
  버전과 thought/emotional beats, key poses, gaze/face, moving hold, partner reaction,
  lead/follow/settle order를 함께 묶는다. 모델에는 전문용어 목록이 아니라 어떤 부위가
  언제 무엇을 보고, 무엇보다 늦게 따라오며, 어떤 contact/camera가 고정되는지 쓴다.

## 선택한 경로에 필요한 입력

1. **외형·구도 기준**: 사용자 목표에 맞는 이미지와 자산. 같은 캐릭터·의상·크기·소품을 유지한다.
   새 이미지가 요청 범위에 있으면 사용자가 선택한 이미지 모델과 기존 엔티티를 사용한다.
   현재 경로는 Nano Banana로 고정 접시 원본에 기존 `@` 엔티티를 배치하고, 그 기준 이미지를
   Kling의 시작 이미지로 넘긴다. UI의 `@` 호출은 실제 도구의 엔티티 바인딩 규약으로 연결한다.
2. **행동 프롬프트**: 시작 상태, thought/attention trigger, 인과 순서, key pose/hold,
   얼굴·시선·partner reaction, body/cloth settle, 끝 상태, 카메라/빛/재질 유지, 금지된
   순간 등장/형태 변화. “cinematic, cute, realistic, overlap”만 나열하지 않는다.
3. **선택적 동작 가이드**: 가이드가 필요한 구체적 목적과 모델의 영상 입력 지원을 확인한
   경우에만 사용한다. 일반 Kling 이미지→영상에 모션 영상을 자동 첨부하지 않는다.
   Blender 가이드라면 고정 카메라, 읽히는 캐릭터 비율, 실제 높이의 접시/지지물,
   열린 뜰채 입구와 손잡이, 명확한 손/발 접촉. 상세 장식 대신 필요한 기하에 집중한다.
   너무 단순해서 망의 입구나 물/접시 경계가 사라지면 행동이 모호해진다.
   하중 동작은 손만 추적하지 말고 grip-before-load, 발/골반/몸통의 준비, working-range
   margin, continuous contact, 새 지지와 settle이 읽히는 guide 구간을 제공한다.

음식·유체의 점도, 분열, 파동, 쌀알/입자 스케일, wetness/SSS/증기는 설치된
`food-vfx-director`가 물성 계약과 후보 QA를 맡는다. 이 스킬은 그 계약을 실제
실제 입력 역할에 묶고, Blender 가이드를 쓰는 경우 source/receiver geometry가 살아 있는지 확인한다.

입력 지원/길이 제한에 맞춰 제출한다. 지원하지 않는 모션 가이드를 사용했다고 주장하지 않는다.

레퍼런스마다 `파일/버전 | 대상 | 역할 | 적용 구간 | 이어받을 것 | 제외할 것`을 적는다.
가이드의 배치·동작과 이미지의 외형·재질을 분리하고, 캐릭터/도구를 개별적으로 연결한다.
설치된 `visual-video`는 비트와 프롬프트를 다듬는 데, `visual-image`는 외형 기준 설계에
사용할 수 있다. 해당 스킬의 모델표는 고정된 참고 문서이지 현재 CLI 기능 목록이 아니다.
Jimeng 웹 기능을 Higgsfield에서도 된다고 가정하지 않는다. 프롬프트 예시의 CLI 옵션이나
JSON을 실제 API 스키마로 복사하지 않는다. 새 연결은 실행 전 도움말/스키마로 검증한다.

고정 카메라 작업의 시간 구간은 그 자체로 컷 지시가 아니다. 단, 사용자가 요청한
전체 화면 부채 wipe 같은 명시적 편집은 유지하며 국소 효과로 바꾸지 않는다. 프롬프트를
줄일 때도 접촉·정체성·카메라·배경 연결 제약을 남기고 중복 설명/장식적 수식부터 덜어낸다.

## 생성·수정·확장

- 사용자가 정한 장면과 길이로 제작한다. 짧은 시험은 요청되었거나 구체적 미해결 문제가
  있을 때만 선택한다. 10초 연구나 별도 A/B 비교를 모든 제작의 선행 단계로 강제하지 않는다.
- 초기 캐릭터/질감과 행동이 어긋나면 긴 이야기를 먼저 생성하지 않는다.
- 손이 뒤틀린 Blender 가이드를 그대로 넘기고 영상 모델이 고쳐줄 것이라 가정하지 않는다.
  소품을 다루는 핵심 장면이면 제작 스킬의 손 축/그립 검증을 먼저 하고, 생성 결과에서도
  엄지 맞섬·패드 방향·손목/전완·지지 전환을 다시 본다. 가이드 통과는 생성본의 통과가 아니다.
- 생성본이 Blender의 고정 grip/pose/support를 더 보기 좋게 바꾸었더라도 contract drift다.
  얼굴·옷·미세 연기는 bounded일 수 있지만, 손 위치·하중 이전·지지 발·phase order는
  명시적으로 풀지 않는 한 fixed로 유지한다.
- 생성본이 contact를 보존해도 thought beat, key pose 대비, gaze target, partner offset,
  moving hold 또는 staggered settle을 지우면 performance drift다. 물리 통과와 별도로 기록한다.
- 받아 온 영상 자체를 검사한다. 이미지 생성 성공, 업로드 성공, 작업 제출 성공은 영상 생성 완료가 아니다.
- extension도 접촉/정체성을 망칠 수 있다. 이전 승인 클립의 끝 상태와 이어지는 결과를 비교한다.
  전체 이야기 요청을 단편만으로 완료 처리하지 않는다.
- 실제 생성 파일, 작업 ID/비용, 경계 검토, 입력 이미지·프롬프트와 사용한 경우 가이드를 보존한다.
  납품 전에 `animation-causality-review`가 설치되어 있으면 검수하고, 기술 파일 검증은 별도로 한다.
- 후보가 의도와 다르면 실패 구간을 사용자에게 보여주고 기획/가이드/모델/후반 원인을 나눈다.
  중요한 변경은 영향받는 이미지·행동 지시·선택한 가이드를 수정하고 필요한 협의로 돌아간다.
  전체 메시 프리비즈를 자동 추가하거나 자동 유료 재시도하지 않는다.

다단계 제작/재개에는 [공통 인계 규약](../miniature-film-director/references/handoff-contract.md)을 사용한다.
가이드·이미지·프롬프트 버전, job ID/미확정 제출, 비용 장부와 실제 출력 ID를 연결한다.
생성 서비스의 완료 상태와 시각적 품질 판정을 분리한다. 동반 스킬이 없으면 기존 장부/노트에
동일한 연결을 남긴다. 이미 유효한 분석·가이드가 있으면 다시 제작하지 않는다.
