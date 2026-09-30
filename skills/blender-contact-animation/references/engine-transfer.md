# 엔진 이전은 새로운 좌표·제어 계약

물리 반응이 필요한 경우에도 전신 ragdoll, 캐릭터 이동, 발 IK, 손의 물체 조작,
강체 접촉, 유체는 다른 시스템이다. 필요한 상호작용을 정하고 이전 비용과 현재 자산의 호환성을 본다.

## 최소 검증 장면

- 배우 하나, 바닥 하나, 잡을 소품 하나를 먼저 옮긴다. 전체 마을을 가져오기 전에
  신장/루트/본의 단위, 원점, 정면, 애니메이션의 1초 이동을 각각 측정한다.
- Blender m/Z-up/right-handed와 Unreal cm/Z-up/left-handed 사이 변환을
  한 곳에서 정의한다. 축 negation을 exporter, importer, actor에 중복 적용하지 않는다.
- mesh 크기, bone translation, actor scale, animation scale 채널을 분리 검사한다.
  `apply transform` 뒤 Action의 scale 키가 다시 적용되는지 확인한다.
- 스켈레톤 공유와 data single-user 여부를 확인한 뒤 복제본에서 작업한다.
  임시 100배 보정에 추가 보정을 쌓지 말고 알려진 길이로 import/export를 왕복 확인한다.

## 실제 충돌 제어

- NavMesh는 길찾기용이다. 손잡이 그립, 발 접지, 신체 간 충돌을 자동 해결하지 않는다.
- Sequencer의 kinematic transform은 동적 충돌 반응을 우회할 수 있다.
  어느 component가 이동을 소유하는지, sweep/collision profile/physics mode가 무엇인지 확인한다.
- 캐릭터를 소인 크기로 축소하면 물리 tolerance와 step height가 맞지 않을 수 있다.
  인간 크기 시뮬레이션 후 표현 변환을 택하면 모든 support/prop/camera 단위도 일관되게 처리한다.
- 실제 떨어뜨리기, 막힌 경로, 없는 손, 닫힌 입구의 짧은 반례로 제어를 시험한다.

## 실행과 파일 확인

설치/라이선스/관리자 권한이 필요하면 권한 경계에서 멈춘다. 계정 코드·토큰을 문서에 남기지 않는다.
Unreal Python API와 Movie Render Queue 동작은 설치 버전의 코드/문서에서 확인한다.
에디터 commandlet에서 UI subsystem이 존재한다고 가정하지 않는다.
level/sequence를 실제 package 경로에 저장했는지, 카메라 binding과 tick/display rate가 맞는지,
render exit 0 뒤 실제 프레임이 생겼는지 확인한다. 실행 옵션 하나를 보편적인 해법으로 고정하지 않는다.
