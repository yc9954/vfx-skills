---
name: miniature-film-director
description: Coordinate end-to-end miniature tabletop film production or resume a multi-stage Le Petit Chef-style project. Routes reference analysis, Blender construction, optional generation, candidate review and delivery at their actual stages; isolated analysis, review or render-status requests can use the corresponding specialist directly.
---

# 미니어처 영상 제작 감독

사용자는 이야기와 원하는 느낌을 말하면 된다. 에이전트가 리소스 조사, 제작,
검수, 렌더를 맡고, 사용자에게 bpy 코드나 도구 설정을 불필요하게 떠넘기지 않는다.
분석 요청에는 분석만, 제작 요청에는 실제 결과물을 만든다.

## 먼저 정할 것

- 현재 요청의 범위: 원본 재현 / 같은 이야기의 새 연출 / 질감 연구 / 동작 수정.
  최근 피드백을 우선하며 과거에 거절된 안을 정답으로 재사용하지 않는다.
- 실제 입력 영상·이미지·기존 장면을 확인한다. 파일명, 길이, 수정 시각만으로
  “방금 생성한 영상”이라고 단정하지 않는다. 없으면 그 사실부터 밝힌다.
- 길이, FPS, 화면비, 투사/일반 영상, 카메라, 음향, 비용 상한을 현재 지시에서
  복원한다. 10초 연구는 2분 이야기의 완성본이 아니다.
- 기본 제작 경로는 사용자가 선택한 도구를 따른다. 단순한 Blender 접촉 애니메이션으로
  가능한 작업을 물리라는 이름만 얻기 위해 Unreal로 이전하지 않는다.
- 현재 산출물과 실행 경로는 [deliverable-routing.md](references/deliverable-routing.md)로 고정한다.
  Higgsfield 최종 생성 요청을 받았다면 기존 유효한 가이드를 재사용해 생성 단계로 간다.
  가이드 완성이나 플러그인 시험을 본편 완성으로 보고하지 않는다.

## 단계별로 필요한 스킬만 사용

아래 스킬이 현재 설치되어 있는지 확인하고 해당 단계에서만 읽는다. 없으면
누락을 밝히고 그 단계의 산출물과 검사 기준을 직접 수행한다. 전부 무조건 로드하지 않는다.
한 요청의 담당 단계를 먼저 정한다. 분석만이면 분석에서 끝내고, 제작을 요청받았다면
후보가 만들어진 시점에 검수를 적용한다. 검수 스킬을 미리 불러 없는 완성본을 요구하지 않는다.
사용자가 이름으로 지정한 스킬은 읽되, 그 자체로 요청 범위를 넓히지 않는다.

| 단계 | 스킬 | 필요한 결과 |
|---|---|---|
| 레퍼런스의 동작·소품·질감 관찰 | `film-reference-breakdown` | 시간표, 엔티티 목록, 관찰/추론 구분 |
| 뜬금없는 등장·행동·효과·전환의 사전 설계 | [animation-causal-staging](../animation-causal-staging/SKILL.md) | 등장 근거, 트리거→경로→결과, 지속 상태와 전환 전/가림/공개/후 이미지; 실제 행동과 편집 구분 |
| 장면 목적·감정·성격을 살아 있는 연기로 설계 | `character-performance-animation` | thought/emotional beat, key pose, timing, gaze/face, secondary motion이 담긴 performance contract |
| 사람 동작의 ROM·그립·하중·균형 명세 | `human-motion-biomechanics` | 제작·프롬프트·검수가 공유할 compact motion contract |
| 새 이야기의 화면·프롬프트 연출 | `visual-video` | performance/motion contract를 카메라·빛·편집과 관찰 가능한 생성문으로 변환 |
| 외형·재질 기준 이미지 설계 | `visual-image` | 목표 질감과 불합격 기준; 실제 이미지는 생성 도구로 제작 |
| Blender 동작·접촉 제작 | `blender-contact-animation` | 연속된 지지·그립·이동이 있는 편집 가능 장면 |
| 음식·유체 물성 설계/검수 | `food-vfx-director` | 재료 상태, 소스→싱크, 스케일, 생성 제약과 후보 QA |
| 요청된 AI 영상 경로 | `blender-seedance-handoff` | 짧은 시험, 연속성·비용 기록, 실제 생성 영상 |
| 어색함 검토 및 납품 전 검수 | `animation-causality-review` | 통과 범위 / 실패 / 미검증을 구분한 기록 |
| GPU 렌더와 파일 납품 | `film-render-delivery` | 재생 검증된 영상, 원본, 해당 버전의 검사 결과 |

원본 파악이 끝난 작업에서는 유효한 분석을 재사용한다. 재질 수정 때문에 보행을 다시
생성하거나, 인코딩 수정 때문에 장면을 재제작하지 않는다. 바뀐 대상과 영향을 받는
인과관계만 다시 검사하되, 최종 납품 때는 실제 출력 전체의 누락·새 결함을 확인한다.

## 중단 후 재개와 단계 인계

여러 단계의 제작이나 재개 요청에는 [handoff-contract.md](references/handoff-contract.md)를 읽고
기존 작업 기록을 먼저 재사용한다. 기록이 없을 때만 [film-state.template.json](assets/film-state.template.json)을
프로젝트의 `film_state.json`으로 복사해 확인한 사실을 채운다. 단순 질문/검토만으로 만들지 않는다.
현재 지시, 산출물 버전, 유효한 검사, 남은 문제, 실행 중 작업과 다음 행동을 함께 기록한다.
기록은 기억 보조이며 실행 허가나 실제 프로세스 상태를 대신하지 않는다.

## 이 프로젝트의 연출 기준

접시 프로젝션 작업이면 [projection-art-direction.md](references/projection-art-direction.md)를 읽는다.
이것은 이 사용자와 만든 시리즈의 기준이며 다른 프로젝트의 보편 법칙은 아니다.
새 지시로 카메라·세계관·스타일이 바뀌면 이전 기준을 강요하지 않는다.

새 이야기/행동 설계에는 [story-to-contact.md](references/story-to-contact.md)를 읽어
짧은 연출 비트를 실제 지지·그립 전환으로 바꾼다. 기존 장면의 렌더나 상태 확인만이라면
이 단계를 다시 수행하지 않는다. `visual-video`/`visual-image`는 선택적 연출 자료이며
설치되지 않아도 제작을 막지 않는다. 목표 행동과 사용자 제약이 프롬프트 관례보다 우선이다.

## 제작 순서와 중단 기준

이 테이블 시리즈의 기본 제작 루프는 [collaborative-production-loop.md](references/collaborative-production-loop.md)를 따른다.
러프안→질문/기획 보완→이미지 콘티→전체 단순 메시 프리비즈→나란히 대조/최종 컨펌→
Higgsfield 제작→실제 후보 검수이며, 의도 불일치는 자동 재결제 없이 기획 대화로 돌아온다.
상태/조사만 요청된 경우 제작 루프를 시작하지 않는다.

1. 기존 자산을 검토해 재사용한다. 라이선스·리깅·텍스처가 확인된 것부터 쓴다.
   무료 다운로드 가능과 상업적 투사·배포 권한은 구분한다.
2. 새 제작에서는 이야기의 핵심 상호작용을 먼저 완성한다. 걷기→멈춤→집기라면 준비·그립·들기까지
   포함한 짧은 시험을 만든다. 사용자의 기본 테스트 요청은 대략 100프레임/짧은 클립으로
   해석하되, 원인과 결과가 잘리지 않도록 범위를 설명한다.
   먼저 scene objective, character want, emotional change, partner relation과 성격 의도를 정하고,
   설치된 `character-performance-animation`으로 thought beat→key pose→timing/gaze/face→secondary
   motion의 performance contract를 만든다. 그 다음 biomechanics가 같은 포즈·행동을 ROM·하중·
   지지·그립으로 제한한다. 물리 제약 때문에 포즈가 바뀌면 연기 의도를 유지한 대체 포즈를 다시 잡는다.
   사람이 하중을 다루면 공통 motion contract의 시작/끝 지지, 양손 역할, 작업 범위,
   kinetic chain, 체중 이동과 settle을 먼저 기록해 Blender·생성 프롬프트·검수에 같은 버전을 넘긴다.
3. 비싼 전체 제작 전에 동작 시험과 별도로, 고정된 실제 투사 시점의 look frame을 만든다.
   `visual-image`의 projection look gate로 시선 우선순위·명암·재질·실제 표시 크기를 확인한다.
   내부 단편 제작 판단과 사용자 승인은 구분한다. 회색 접촉 진단 이미지를 최종 미술 기준으로
   승격시키지 않는다. 동작과 접촉을 확인한 뒤 재질·조명·물·소리의 밀도를 높인다. 질감만 수정하는 요청에는
   기존 동작을 유지하고 그 변경의 영향을 검토한다. 각 재료의 정체와 역할은
   처음부터 기록하되, 보이지 않는 미세 모델링에 시간을 먼저 쓰지 않는다.
   음식·유체가 핵심이면 `food-vfx-director`의 물성/스케일/소스-싱크 계약을 적용하되,
   카메라 연출·Blender 접촉·장면 전체 승인과 기술 납품의 책임은 합치지 않는다.
   새 인체 리그는 관절/스킨→전신 협응과 지지→시간에 따른 연기를 구분해 확인한다.
   설치된 제작/검수 스킬의 전신 참조에 따라 해당 역할의 걷기·회전·낮은/높은 도달·운반 등
   필요한 완결 행동으로 사용 가능 범위를 남긴다. 손 취급은 손 전용 참조도 적용한다.
   첫 리그의 잘못된 관절 축·IK·웨이트를 전체 배우에 복제하지 않는다. 검증된 제어를
   재사용해도 체형·의상·신발·소품이 바뀌면 영향을 받는 행동은 다시 확인한다.
4. 핵심 결함이 남으면 전체 고비용 렌더를 보류하고 해당 상호작용을 고친다.
   짧은 시험이 이미 승인됐거나 전체 제작이 명확히 요청됐으면 불필요한 재확인을 반복하지 않는다.
   사용자가 결함을 알고 현 상태 전체 렌더를 요청하면 그 범위를 수행하고 품질 판정은 별도로 남긴다.
5. 납품 범위를 지키며 실제 영상과 편집 원본을 전달한다. 미검증 자연스러움을 승인으로
   바꾸지 않는다. 가능한 결과가 시험본뿐이면 시험본으로 표시한다.

진행 보고는 실제 완료된 산출물, 다음 한 단계, 측정된 시간/구체적 장애만 말한다.
스킬 호출은 유료 생성·새 구독·자료 업로드·파일 삭제·새 작업 생성의 추가 허가가 아니다.

## 사용 예

“이 레퍼런스와 폴더 자산으로 같은 이야기를 새로 만들어줘. 접시 위 소인들의
행동이 자연스러운지 짧은 영상부터 확인하고, 괜찮으면 전체를 렌더해줘.”
