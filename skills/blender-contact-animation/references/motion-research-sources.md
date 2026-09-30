# 모션 제작 방법의 근거와 적용 상태

2026-09-21 조사. 아래의 '가능'은 원저자/공식 문서의 범위이지 현재 프로젝트에서 검증된
품질이 아니다. 새로운 의존성 선택 시 버전·가중치·권한·입출력·실행 환경을 다시 확인한다.
이 자료는 방법 선택용이며 모든 동작 작업에서 전체를 다시 읽을 필요는 없다.

| 근거 | 확인한 내용 | 이 프로젝트에서의 판단 |
|---|---|---|
| [Pixar 협력 전시 — Animation](https://sciencebehindpixar.org/pipeline/animation) | 주요 포즈와 그 사이 움직임으로 감정/성격을 연기하는 과정 | 키프레임 연출의 근거. 물리 정확성이나 자동 생성 품질의 근거로 확대하지 않음 |
| [Kimodo 제약 공식 문서](https://research.nvidia.com/labs/sil/projects/kimodo/docs/key_concepts/constraints.html) | 경로·키포즈·말단 제약, canonical Y-up 미터 좌표; 발 접촉 조건은 문서상 학습했지만 UI/API 미구현 | 기존 설치를 우선 활용하되 지원하지 않는 foot-contact 입력 플래그를 지어내지 않음 |
| [Kimodo 기술 보고서](https://research.nvidia.com/labs/sil/projects/kimodo/assets/kimodo_tech_report.pdf) | multi-prompt의 겹침 조건과 후처리 접근 | 독립 클립의 단순 연결보다 경계 조건 생성 우선. 접촉·연기 결과는 별도 확인 |
| [Ubisoft La Forge — Learned Motion Matching](https://www.ubisoft.com/en-us/studio/laforge/news/6xXL85Q3bF2vEj76xmnmIu/introducing-learned-motion-matching) | 현재 포즈/속도와 미래 경로를 기준으로 모션을 검색; 작은 불연속에 블렌딩/관성화, 이후 발 보정 | 상태를 맞춰 연결하는 근거. 데이터에 없는 안무를 모션 매칭이 만들어낸다고 가정하지 않음 |
| [EDGE, CVPR 2023](https://edge-dance.github.io/) | 음악 조건 춤, 구간 연결/중간 동작 생성, 의도적인 발 슬라이드와 불필요한 미끄러짐 구별 | 춤의 제약 설계에 참고. 일반 발 고정 후처리를 춤에 그대로 적용하지 않음 |
| [EDGE 공식 구현](https://github.com/Stanford-TML/EDGE) | 코드/모델 다운로드 및 SMPL→FBX 경로, Linux/NVIDIA 기반 요구사항과 연구 코드 유지보수 한계 | 설치하지 않음. Mac Metal 즉시 호환이라고 단정하지 않으며 실제 샘플/비용 비교 후 선택 |
| [AIST++ 설명](https://google.github.io/aistplusplus_dataset/factsfigures.html), [다운로드 안내](https://google.github.io/aistplusplus_dataset/download.html) | 다중 뷰로 추정한 3D 춤/음악 자료, 주석은 CC BY 4.0; 원본 영상/음악은 별도 약관 확인 요구 | 움직임 분석/실험 후보. 광학 모캡 원본이라고 부르지 않고 모든 데이터의 상업 권한으로 일반화하지 않음 |
| [Adobe Mixamo FAQ](https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html) | 이족 휴머노이드용 리깅/모션; FAQ는 영상 등 상업 프로젝트 사용을 허용한다고 안내 | 재사용 모션 후보. 실제 클립·계정·현행 조건 확인, 소스 자산 재배포 권한은 별도. 접촉/손 품질 보증 아님 |
| [DeepMimic, SIGGRAPH 2018](https://xbpeng.github.io/projects/DeepMimic/index.html) | 예제 모션을 모방하는 제어 정책으로 물리 환경의 행동/회복을 학습 | 물리 반응에는 구동/제어가 필요하다는 근거. Unreal 설치 또는 래그돌 추가와 동등하지 않음 |
| [DanceEditor 논문 페이지](https://lzvsdy.github.io/DanceEditor/), [연결된 저장소](https://github.com/LZVSDY/DanceEditor) | 음악 기반 생성 후 텍스트로 편집하는 연구. 확인한 저장소에는 figure와 index.html만 표시 | 아이디어 참고만. 논문의 Code 링크를 실행 가능한 추론 코드/가중치 확보로 오인하지 않음 |
| [국립국악원 춘앵전 자료](https://archive.gugak.go.kr/portal/detail/searchVideoDetail?clipid=32956&recording_type_code=V&system_id=AV) | 정재 공연 기록과 작품 정보; 이 자료는 공공누리 4유형 표시 | 양식 조사 후보. 이번에는 메타데이터만 확인, 영상 동작은 미분석. 상업 이용/변환 허가로 취급하지 않음 |

자료별 연구 성능 수치나 홍보 문구를 서로 다른 데이터/환경에서 직접 비교하지 않는다.
코드의 MIT 같은 라이선스가 음악·가중치·SMPL 계열 자산까지 자동 포괄하지 않는다.
Blender NLA 공식 페이지는 이번 조회에서 본문 취득 오류가 있었으므로 새 버전 API를
검증했다고 기록하지 않는다. 실제 구현 시 설치된 bpy API와 짧은 평가 장면으로 확인한다.

## 로컬 Kimodo 코드에서 실제 확인한 것

중복된 구현 설명은 [Kimodo 기능·호출 계약](kimodo-capabilities.md)에 모았다.
멈칫거림/시간 불일치/root-only 축소와 실제 배열 검사는
[연속성 진단](kimodo-continuity.md)에 있다. 소스·NPZ·메타데이터의 SHA-256 및
재실행 가능한 진단은 프로젝트의 `skill-maintenance/kimodo-capabilities-20260921.kojqdB/`에 보존한다.
배열 검사/합성 반례는 실행했지만 새 모델 추론, 최종 리그 접촉 검증, 영상 품질 비교를
수행한 것은 아니다. 경로나 코드가 달라지면 이 로컬 스냅샷의 결론을 재확인한다.

## 현재의 실용적 순서

기존 Blender 리그의 기본 행동 검증 → 권한이 확인된 모션/실연과 Kimodo로 짧은 기반 생성 →
행동/음악 프레이즈별 연결 → 손/발/소품 보정 → 정상속도 비교가 첫 경로다.
음악 조건 모델, 모션 매칭 런타임, 물리 모방 학습은 해당 기능이 실제 병목일 때 별도 시험한다.
리서치 문서와 계획용 타이밍 도구가 생겼다는 사실을 새 춤 영상이 완성됐다는 말로 바꾸지 않는다.
