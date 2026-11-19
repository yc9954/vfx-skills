---
name: film-render-delivery
description: Execute authorized animation rendering/encoding/delivery or inspect render progress and resumes, with GPU timing, process safety and verified media. Consumes the saved scene and existing quality decisions; does not initiate reference analysis, animation construction or quality approval from a status question.
---

# 영상 렌더·납품 검증

상태 질문에는 실제 상태와 측정 기반 ETA만 답한다. 제작/재개 요청일 때만 작업을 시작한다.
먼저 기존 결과와 실행 중 프로세스를 확인해 중복 렌더를 피한다.

## 실행

렌더 실행·중단·재개 전 [gpu-and-process-safety.md](references/gpu-and-process-safety.md)를 읽는다.
기존 장면과 품질 근거를 먼저 확인한다. 새 장면에 핵심 결함/불확실성이 남으면 필요한 짧은
시험으로 위험을 줄이되, 이미 승인된 장면에 새 시험을 강제하거나 매번 사용자 승인을 요구하지 않는다.
사용자가 알려진 결함을 포함한 현재 상태의 전체 렌더를 요청하면 그 요청을 수행하고
기술적 완료와 품질 판정을 분리한다. “렌더해줘”를 자연스러움의 승인으로 해석하지 않는다.
새 버전의 장면, 렌더 설정, 출력, 로그를 하나의 run ID로 연결한다.
장면·외부 캐시의 불변 스냅샷을 정한 뒤 실행한다. 변경 중인 파일을 장시간 검사/렌더하고
끝에 최신 해시를 붙이지 않는다. 재개는 같은 입력의 유효한 프레임에 한정한다.
손 동작이 사용자에게 거절됐거나 관련 검수가 실패한 후보는 해상도/샘플 수를 높였다고
승인본이 되지 않는다. 검토용 렌더는 손이 읽히는 근접 뷰와 완결 행동을 제공하고,
미해결 상태는 시험본으로 명시한다. 손 문제 때문에 무관한 승인 장면까지 재제작하지 않는다.

다단계 제작/재개에서는 [공통 인계 규약](../miniature-film-director/references/handoff-contract.md)의
현재 장면·실행 기록을 확인한다. 실제 프로세스 상태와 파일 버전을 재확인한 뒤 이어간다.
렌더/인코딩 변경만으로 장면을 재제작하지 않는다. 결과 해시와 기술 검사를 같은 기록에 연결한다.
동반 스킬이 없으면 기존 프로젝트 노트에 기록한다. 상태 질문만으로 파일을 갱신하지 않는다.

## 납품 검증

- 실제 파일이 있고 요구한 해상도·길이·FPS·프레임 수인지 확인한다.
  exit 0, 마지막 로그, GPU 장치명만으로 완료를 선언하지 않는다.
- 영상 전체 디코딩과 음향 트랙 유무를 검사한다. 정상속도 연기 검토와 소음/싱크 청취는
  별도다. 도구로 직접 보거나 듣지 못했으면 미검증이라고 남긴다.
- `.blend` 또는 해당 엔진의 편집 원본을 함께 납품하고 외부 텍스처/캐시 의존성을 확인한다.
  메모리상의 장면과 저장된 파일이 다른데 같은 버전인 것처럼 설명하지 않는다.
- 각 결과에 기술 검증, 인과/접촉 검증, 연기/질감 검토, 오디오 검토를 분리 기록한다.
  실패가 있으면 수정하거나 시험본으로 전달한다. 이름에 FINAL을 붙여 승인 상태를 암시하지 않는다.

## 재사용 가능한 검사 도구

`scripts/media_receipt.py`는 Python 표준 라이브러리와 PATH의 `ffprobe`, `ffmpeg`를 사용한다.
입력 미디어를 수정하지 않고 첫 영상 트랙의 프레임 수·평균 FPS·길이·해상도,
음향 트랙, 전체 디코딩, 파일 해시를 확인한다. 로컬 파일에만 실행한다.

```sh
python3 /path/to/film-render-delivery/scripts/media_receipt.py /absolute/candidate.mp4 \
  --expect-frames 240 --expect-fps 24 --expect-seconds 10 \
  --expect-width 1440 --expect-height 1440 --audio absent \
  --scene /absolute/candidate.blend --receipt /absolute/new-run/media-receipt.json
```

위 수치는 사용 예다. **현재 요청값**을 넣고 기존 결과 수치를 기대값으로 복사해
자기 충족 검사를 만들지 않는다. `--expect-fps 30000/1001` 같은 유리수도 지원한다.
VFR의 평균 FPS는 일정 프레임 간격의 증명이 아니다. CFR가 필수면 타임스탬프 검사도 추가한다.
`--receipt`는 부모 폴더가 있어야 하며 기존 파일을 덮지 않는다. 생략하면 JSON을 stdout에 출력한다.
종료 코드는 0=명시된 기술 검사 통과, 1=불일치/디코딩 실패, 2=입력·도구 오류다.
기대값을 생략한 속성은 관찰값일 뿐 요청 충족 검사가 아니다.

## 전달

짧게 실제 길이/해상도/음향, 파일 링크 또는 인라인 영상, 편집 원본, 남은 결함을 말한다.
최종 영상 대신 분석 보고서만 주지 않는다. 렌더 진행 중이면 완료했다고 말하지 않고
현재 프레임, 최근 처리율과 남은 범위를 제시한다.
