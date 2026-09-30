# Kimodo 기능과 제작 역할 분담

2026-09-21 공식 문서 + 당시 로컬 Kimodo 체크아웃 소스 대조. 실행 가능한 기능, 제약으로 구성하는
워크플로, 구현되지 않은 기능을 구분한다. 연구/진단 요청만으로 생성 코드 변경·가중치 다운로드·
클라우드 실행·영상 재제작까지 진행하지 않는다. 로컬 파일 해시는 프로젝트 조사 기록을 따른다.

## 선택 원칙

Kimodo는 전신 동작의 기반을 만들고, Blender는 실제 자산·표면·접촉·연기를 마무리한다.
인물 하나를 어느 한쪽에 영구 배정할 필요는 없다. 몸통/보행은 생성하고 손/소품/시선만 직접
다듬는 하이브리드가 가능하다. 한 번 생성했다고 자연스러움을 승인하지 않는다.

| 필요한 결과 | 우선 방법 | 추가로 해결할 것 |
|---|---|---|
| 병사 행진, 주민 이동, 인사, 자유로운 몸짓 | Kimodo 단일 프롬프트/다중 후보 | 인물별 보폭·행동 차이, 보행 접촉, 군중 간 거리 |
| 같은 행동이 계속되는 이동 | 가능한 길이 안에서 단일 동작 + 경로 | 경유점은 통과하고 진짜 목적지에서만 정지 |
| 걷기→회전→인사처럼 행동 변화 | `multi_prompt` + 목적별 구간 길이 | 전이 시간, 지지 발/속도, 다음 행동의 실행 여유 |
| 기존 클립 뒤 이어가기 | 끝의 짧은 포즈 이력을 조건으로 새 구간 생성 | canonical 좌표 이동, 이력 중복 제거, 경계 검사 |
| 정해진 시작·끝 사이 메우기 | 양 끝 full-body 키포즈/짧은 이력 + 중간 생성 | 도달 가능한 시간·속도·접촉, 손발 방향 제약 |
| 손을 특정 위치로 내밀기, 특정 지점에 디디기 | sparse end-effector 조건 | 실제 물체/발바닥 메시 접촉과 팔꿈치/무릎 방향 |
| 그릇 받치기·뜰채·부채·악기·손가락 | Kimodo 전신 기반 + Blender IK/FK/그립 | 손가락 축, 양손 협응, 소품 지지/분리, 관통 |
| 일반 춤/다양한 스타일 초안 | Kimodo 후보 + 프레이즈별 편집 | 피벗/슬라이드 허용, 회전 이력, 음악 타이밍 |
| 정확한 정재/특정 안무/음악 비트 재현 | 허가된 실연·모캡 기반 우선 | Kimodo는 보조 전이 후보; 고증·음악 조건 능력 과장 금지 |
| 물·옷·재료 낙하·충돌 반응 | Blender 시뮬레이션/명시적 접촉 제어 | 캐릭터가 반응하려면 별도 구동/제어 필요 |

## 공개 제작 기능 맵

### 생성과 변주

`KimodoModel.__call__`에서 텍스트, 프레임 길이, seed(호출 전 RNG 설정), 샘플 수,
denoising steps, CFG, 제약, 최초 heading, 후처리를 조합한다. 문자열 하나 안의 순차 행동과
동시 행동도 가능하지만 조밀한 이야기 전체를 한 프롬프트에 넣는 방식은 피한다.
동작의 목적과 지속 상태를 각 구간에 포함하고, 정말 정지할 때만 정지를 요구한다.

- `multi_prompt=False` + 리스트: 독립적인 배치. 연속 모션이 아니다.
- `multi_prompt=True` + 리스트: 순차 생성. 여러 후보는 `num_samples`로 분리.
- `cfg_type`: `nocfg`, `regular`(가중치 하나), `separated`(텍스트/제약 각각).
  높은 제약 가중치가 신체 자세나 자연스러움을 보장하지 않는다.
- 스텝 증가/seed 변경은 후보 탐색 수단이지 잘못된 경로·축·지지 상태의 수리가 아니다.
- 프롬프트당 약 10초는 공식 안내의 학습/운용 범위다. 전이 이력까지 붙인 실제 입력 길이와
  체크포인트를 확인한다. 긴 배열을 만들 수 있다는 사실을 장기 품질 검증으로 쓰지 않는다.

근거: [설정](https://research.nvidia.com/labs/sil/projects/kimodo/docs/user_guide/configuration.html),
[권장 사용법](https://research.nvidia.com/labs/sil/projects/kimodo/docs/key_concepts/limitations.html),
로컬 `kimodo/model/kimodo_model.py`, `kimodo/scripts/generate.py`.

### 제약 — 정확히 무엇을 지정하는가

| 기능 | 실제 조건 대상 | 오해하지 말 것 |
|---|---|---|
| sparse `Root2DConstraintSet` | 지정 프레임의 smoothed root XZ | 장애물 인식/경로 탐색/충돌 물리가 내장된 것이 아님 |
| dense Root2D | 시간에 따른 연속 XZ 경로 | 모든 경유점에서 속도 0으로 만들지 않음; 높이 경로 아님 |
| `global_root_heading` | `[cos θ, sin θ]` heading 조건 | 전방과 이동 방향은 다를 수 있음; raw radians 아님 |
| `first_heading_angle` | 첫 프레임 heading, radians | 클립 전체의 진행 방향 고정 아님 |
| `FullBodyConstraintSet` | 전신 관절 위치, root/heading | 회전을 입력받아도 conditioning은 전 관절 회전 고정이 아님 |
| 손/발 end-effector | 손목/발뒤꿈치 위치·회전과 손끝/발끝 위치 등 | 임의 손가락 그립 생성이나 자유로운 단일 점 타깃 API로 간주하지 않음 |
| 혼합 제약 | 같은 타임라인에서 여러 제약 조합 | 서로 모순된 목표는 물리적으로 실현 불가 |
| 발 접촉 패턴 입력 | 학습 능력으로 설명됨 | 공개 UI/Python API에는 미구현. 존재하지 않는 플래그를 만들지 않음 |

end-effector는 입력 full pose에서 지정 말단을 추출하며, 이 로컬 구현은 smoothed root,
root 높이, heading도 함께 조건화한다. "손만 지정했으니 몸통은 완전히 자유"라고 가정하지 않는다.
사용할 skeleton의 `expand_joint_names()`로 이름과 확장 관절을 확인한다.

좌표는 Y-up, +Z 전방, 미터, ground XZ. 첫 root 위치를 canonical 원점 기준으로 옮긴다.
JSON frame index는 0-based이며 `local_joints_rot`는 axis-angle radians, Python 클래스의
`global_joints_rots`는 global rotation matrices다. 두 인터페이스를 섞지 않는다.
제약은 원칙적으로 sparse, dense는 주로 root 경로에 사용한다. 점프 높이/계단 발판은
Root2D만으로 지정되지 않으므로 키포즈/말단과 실제 표면 검증을 조합한다.

근거: [제약 개념](https://research.nvidia.com/labs/sil/projects/kimodo/docs/key_concepts/constraints.html),
[JSON 계약](https://research.nvidia.com/labs/sil/projects/kimodo/docs/user_guide/constraints.html),
로컬 `kimodo/constraints.py`.

### 연속·연장·중간 생성

공개 고수준 호출에서 확인한 것은 multi-prompt와 constraint 기반 생성이다. 별도의
`extend()`·`inbetween()`·영상 입력 재현·음악 입력 함수를 있다고 가정하지 않는다.
기존 모션의 앞/뒤 포즈를 제약으로 옮겨 continuation/in-between을 **구성할 수 있다**.
이는 두 독립 모션을 영상 cross-dissolve로 감추는 것과 다르다.
구체적인 설계와 함정은 [kimodo-continuity.md](kimodo-continuity.md)를 읽는다.
기술 보고서의 in-between 사례와 물리 기반 로봇 구동은 구분한다. 후자는 생성 후 별도 정책이다.
[기술 보고서](https://research.nvidia.com/labs/sil/projects/kimodo/assets/kimodo_tech_report.pdf)

### 후처리

공식 CLI는 SOMA 등에 후처리를 기본 활성화하고 `--no-postprocess`로 끈다.
Python `__call__`의 기본은 `post_processing=False`; 프로젝트의 dance/journey도 명시적으로 꺼져 있다.
G1은 CLI에서 비활성화한다. `motion_correction` 기반 foot-skate/제약 보정은 키네마틱
최적화이지 장애물·마찰·중력 시뮬레이터가 아니다. `root_margin`은 그 보정의 허용 범위이며
우리 접시 경계 여유나 충돌 캡슐 반경과 다르다.

현재 `postprocess.py` mask 생성은 `left-hand/right-hand/left-foot/right-foot` 이름을
처리하지만 일반 `end-effector` 이름을 분기하지 않는다. 일반 EE 조건이 생성에는 전달되어도
후처리까지 원하는 말단을 고정한다고 단정하지 말고 named wrapper와 같은 목표로 짧게 비교한다.
후처리를 켤 수 있다는 것과 이 환경에서 오류 없이 품질 개선이 검증됐다는 것은 별개다.

원본→공식 보정→우리 보정→retarget를 별도 보존한다. 춤의 pivot/slide/air는
무조건 planted로 잠그지 않는다. 모든 translation/rotation 수정 후 FK·smooth root·heading·
contact/velocity 파생 채널의 일관성을 확인한다.
근거: 로컬 `kimodo/postprocess.py`, `kimodo/scripts/generate.py`, `pipeline/footlock.py`.

### 모델·리그 선택

현재 문서에는 SOMA RP/SEED v1·v1.1, G1 RP/SEED v1, SMPLX RP v1이 있다.
이 작업은 기존 SOMA-RP-v1.1을 먼저 활용한다. RP는 일반 생성 권장, SEED는 공개 데이터 기반
비교 연구 용도도 있다. G1은 로봇 관절/CSV용이지 사람 리그 품질 업그레이드가 아니다.
SMPL-X는 호환성 목적이며 공식 문서도 심한 retarget artifact 가능성을 경고한다.
모델/가중치·신체 모델·원본 모캡·자산 라이선스는 각각 확인한다.
[모델 목록](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/quick_start.html)

**SOMA 77본 출력은 77본 전부를 모델이 세밀하게 생성한다는 뜻이 아니다.** 내부 예측은
30본으로 손가락 디테일이 대부분 제외되며, export에서 77본으로 확장한다. 변환 코드의
relaxed-hand rest pose 확장을 관찰해 그립 생성으로 오인하지 않는다. SMPL-X export의
`pose_hand` 필드도 학습된 손 연기라는 증거가 아니다. Tripo 리그와 체형이 달라지면
목표 신체에서 발 접촉·관절 축·무릎/팔꿈치·어깨·옷 변형을 다시 검사한다.
[Skeletons](https://research.nvidia.com/labs/sil/projects/kimodo/docs/key_concepts/skeleton.html)

### UI·CLI·캐시·내보내기

- Demo: 프롬프트 타임라인, FK pose 편집, frame/interval 제약, waypoint→dense path,
  여러 후보 중 하나 선택, NPZ/constraints/example 저장·재로드, skeleton/skinned preview.
  Snap to Constraint는 pose authoring 도구이지 이미 저장된 영상의 자연스러움 보증이 아니다.
  [UI 제약](https://research.nvidia.com/labs/sil/projects/kimodo/docs/interactive_demo/constraints.html)
- CLI: period로 나눈 문장을 별도 prompt로 해석한다. 계속 이어지는 한 행동을 문장부호 때문에
  쪼개지 않도록 Python의 명시적 리스트나 입력 meta를 사용한다. `--input_folder`,
  `--save_example_dir`로 재현 가능한 설정/제약을 보존한다.
  [CLI](https://research.nvidia.com/labs/sil/projects/kimodo/docs/user_guide/cli.html)
- 반복 실행은 `kimodo_textencoder` 서비스/캐시 재사용을 검토한다. 텍스트 인코더를 CPU에 두는
  옵션도 있다. 모델 로딩 시간은 영상 내 정지의 원인이 아니다. MPS 장기 구간 실패는 이력이며
  모든 버전의 고정 길이 한계가 아니다. NullTextEncoder는 의미 있는 텍스트 조건의 대체품이 아니다.
- NPZ는 원본/접촉/좌표 검증의 기준. SOMA BVH는 cm 및 rest-pose 옵션
  `--bvh_standard_tpose`를 확인. G1 CSV는 MuJoCo qpos, SMPL-X AMASS는 별도 형식.
- `kimodo_convert`의 Kimodo NPZ 출력은 30Hz로 resample한다. 임의 BVH retarget 도구는 아니다.
  SOMA 계층/원본 fps를 확인하고 fps 재해석으로 속도를 바꾸지 않는다. FBX/Tripo 자동 리타깃은
  Kimodo 기본 export와 별도의 Blender 작업이다.
  [형식 변환](https://research.nvidia.com/labs/sil/projects/kimodo/docs/user_guide/motion_convert.html),
  [출력](https://research.nvidia.com/labs/sil/projects/kimodo/docs/user_guide/output_formats.html)

### 평가의 역할

기본 제공 foot-skate/contact consistency/constraint-error/TMR 평가는 후보 비교에 유용하지만
자연스러운 연기·충돌 없음·비트 동기화·손가락 그립의 증거는 아니다. TMR은 평가용 별도 모델이다.
우리 `path_error`는 pelvis와 목표를 비교하므로 smoothed-root 추종 오차와 구분해 보고한다.
채널 수는 문서의 4개를 하드코딩하지 않는다. 확인한 SOMA77 NPZ는 6개이고 skeleton 매핑이 필요하다.
높이 기반 발 미끄러짐 지표도 의도적 슬라이드/계단/점프에서는 접촉 모드에 맞게 해석한다.
[Metrics](https://research.nvidia.com/labs/sil/projects/kimodo/docs/benchmark/metrics.html)

## 로컬 버전의 호출 주의점

`kimodo/model/kimodo_model.py`에서 확인한 사항으로 버전 변경 시 다시 검사한다.

1. 파라미터명은 `prompts`; 일부 문서 예시의 `prompt=`를 그대로 복사하지 않는다.
2. multi-prompt는 `num_samples=1`과 prompt별 frame 리스트를 명시한다. 기본값 보정 전
   `bs`를 사용하고, 정수 frame을 sample 수만큼 확장하는 구현 때문에 편의 입력을 신뢰할 수 없다.
3. prompt/frame 개수가 같고 모든 길이가 유효한지 호출 전에 검사한다. 내부 `zip`의 잘림을 막는다.
4. 3성분 `smooth_root_2d`의 로컬 슬라이스는 `[0,1]`이다. XZ 2성분을 명시적으로 전달한다.
5. 제약 device/dtype을 맞추되 frame index는 정수로 유지한다. 모델 크기와 pose 배치 차원을 확인한다.
6. API가 받는다는 것, 추론이 끝났다는 것, 원본 모션 품질, 최종 캐릭터 접촉 품질을 각각 기록한다.
