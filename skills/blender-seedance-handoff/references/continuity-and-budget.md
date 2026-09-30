# 클립 연결과 크레딧

## 연속성 계약

클립별로 다음을 고정한다: 인물 ID/비율/의상, 접시 위치/크기, 도구/재료 목록과 소유 상태,
시작/끝 자세, 지지 발, 손 그립, 루트 속도, 화면 방향, 카메라, 노출/색관리, 효과음 기준.
이전 승인 클립의 실제 마지막 프레임/허용된 영상 입력을 사용한다. 단순 텍스트로
“same chef”라고 쓰는 것만으로 정체성 고정이 검증되지 않는다.

- 마지막 한 장을 고정해도 속도가 끊길 수 있다. 이전 수 프레임의 행동과 다음 동작의
  준비를 고려하고 경계 전후를 정상속도로 검토한다.
- 조명/화이트밸런스/노출 변화를 진단한 다음 고정 기준으로 색을 맞춘다.
  프레임별 자동 정규화는 펌핑을 만들 수 있다.
- 크로스 디졸브는 정적인 배경이나 합리적인 시간 전환에 쓸 수 있다. 움직이는 두 셰프,
  겹친 뜰채, 두 번 놓이는 발을 만들면 연결 개선이 아니다.
- 더 긴 모델은 컷 수를 줄일 수 있지만 정체성/물리/비용 문제를 자동 해결하지 않는다.
  실제 지원 길이와 관찰된 품질·비용으로 extension, 긴 생성, Blender 직접 렌더를 비교한다.
- 요청 스토리를 바꿔 실패를 피하지 않는다. 음식의 종, 출발 위치, 재료 개수, 조리 결과가
  바뀌면 연속성 결함으로 기록한다.

## 비용 장부

`shot | input versions | job id | estimated/quoted credits | status | actual charged | refund confirmed | output`

- 현재 승인 상한, 이미 사용한 비용, 처리 중 예약/예상 비용, 잔여액을 먼저 확인한다.
  읽기 전용 잔액/가격 확인은 생성 요청과 구분한다.
- 확인 가능한 상한 내에서만 제출한다. 정확한 비용이 불명확해 상한 준수를 보장할 수 없으면
  유료 제출을 보류하고 확인한다. 무료 사전 준비는 계속할 수 있다.
- 제출 응답이 끊겼다면 ID/상태/히스토리를 확인한 뒤 재시도한다. 불명확한 상태에서
  중복 생성으로 잔액을 태우지 않는다. 동일 요청의 idempotency 기능이 있으면 활용한다.
- 재시도 비용도 포함한다. 실패/정책 차단이 자동 환불됐다고 가정하지 않는다.
  확인된 환불만 반영한다. 결제·추가 충전·새 구독·서비스 변경은 별도 권한이다.
- 권리/서비스 정책 차단은 이를 숨기는 프롬프트나 반복 제출로 우회하지 않는다.
  안전하고 허용된 대안을 설명한다.

## 프롬프트 골격 예시

“Use the attached guide for camera, timing and physical blocking, and the approved
reference image for character and materials. Start with the chef's feet planted
beside the net stand. Reach with both hands, close fingers around the handle,
shift body weight toward the supported tool, transfer the load only after the grip
is secure, then lift the net clear of its stand with hands continuously attached.
End holding it steadily with the feet and torso visibly supporting the load.
Keep the plate, chef scale, prop inventory, exposure and camera unchanged. No new
objects, morphing, teleportation, contact penetration or unexplained cuts.”

가이드 입력을 해당 모델이 실제 지원할 때만 이 표현을 쓴다. 프롬프트의 금지 문구는
검증을 대신하지 않는다. 실행 후 실제 프레임에서 행동 순서를 확인한다.
