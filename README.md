# VFX Skills

레퍼런스 → 연기/접촉 설계 → Blender 또는 Higgsfield → 검수 → 납품을 위한 개인 제작 도구 모음.
**스킬 11개와 작은 공통 실행기만 Git으로 관리**하고, 영상·모델·가중치·계정 정보는 로컬에 둡니다.

## 바로 시작

Python 3.10 이상이 필요합니다. Python 표준 라이브러리만 사용합니다.
아래 `python3`는 3.10 이상 실행 파일로 바꿔 사용할 수 있습니다.

```sh
python3 vfx.py doctor
python3 vfx.py skills validate
python3 vfx.py route higgsfield generate
python3 vfx.py route hybrid prompt --specialist acting --specialist food
python3 -m unittest discover -s tests -v
```

`doctor`는 설치 경로만 조회하며 로그인·업로드·렌더·유료 생성을 하지 않습니다.
다른 디렉터리에서 실행해도 됩니다. 스크립트 경로에 공백이 있으면 따옴표로 감싸세요.
선택적 설치는 `python3 -m pip install -e .`; wheel 단독 배포가 아닌 **소스 체크아웃** 방식입니다.
다른 위치에 설치한 실행기에는 `VFX_SKILLS_ROOT`로 체크아웃을 지정합니다.

## 구조

```text
config/workflow.json       단계별 스킬 라우팅 — 실행 경로를 임의로 바꾸지 않음
skills/                   제작/연기/인체/음식/AI/검수/납품 스킬 11개
src/vfx_skills/            경로 탐색, 라우팅, 1회 제출 관리
examples/                 개인정보 없는 설정 예시
tests/                    서비스 호출을 모킹한 오프라인 회귀 테스트
tools/                    설치·게시 전 검사·로컬 이관 도구
docs/                     아키텍처·실행·마이그레이션 안내
.local/                   Git 제외: 기존 제작물, 실행 영수증, 백업
```

## 스킬 등록

```sh
python3 tools/install_skills.py           # 변경 계획만 확인
python3 tools/install_skills.py --apply   # 기존 11개만 백업한 뒤 이 저장소로 연결
```

등록된 스킬의 실제 파일은 이 저장소가 원본입니다. 저장소를 다시 이동하면 설치 명령을 다시 실행합니다.
다른 스킬은 건드리지 않습니다. 백업 위치는 `.local/skill-backups/`입니다.
Codex의 이미 진행 중인 턴이 새 설명을 즉시 다시 로드한다고 가정하지 말고 다음 턴/세션에서 확인합니다.

## 제작 방식

- **Higgsfield 요청:** 이미 유효한 이미지/가이드가 있으면 제출 단계로 진행. 불필요한 Blender 재제작 금지.
- **Blender 요청:** 편집 가능한 장면과 실제 검수 영상을 제작. AI 영상 생성 자동 추가 금지.
- **Hybrid 요청:** Blender는 필요한 배치·동작·접촉 가이드, AI는 허용된 표현 확장.
- 연기·인체·음식 스킬은 필요한 단계에만 추가. 모든 스킬을 매번 읽지 않습니다.
- `film_state.json`이 이미 있으면 그대로 사용. 실행 영수증만 `.local/runs/<run>/`에 연결합니다.
- 기술적 완료와 자연스러움 검수는 별개입니다. 성공 응답만으로 영상 완성을 선언하지 않습니다.

상세: [아키텍처](docs/architecture.md) · [생성 실행](docs/generation.md) ·
[폴더/경로 이관](docs/migration.md) · [출처와 라이선스](NOTICE.md).

## 저장소에 넣지 않는 것

계정/토큰, Notion 원문, 사용자 레퍼런스, 유료 생성 결과, `.blend`/FBX/영상, 모델 가중치,
거대 로그, 렌더 프레임, `node_modules`는 게시하지 않습니다. Private 저장소도 예외가 아닙니다.
Git 인덱스 기준 검사: `python3 tools/check_publish.py`.
이 검사는 알려진 패턴/경로/크기 가드이며 완전한 비밀 탐지기를 대신하지 않습니다.

현재 GitHub 로그인에 `workflow` 권한이 없어 자동 CI는 등록하지 않았습니다.
`tools/ci.template.yml`에 오프라인 테스트용 설정을 보관했습니다. 별도로 권한을 승인받은 뒤
`.github/workflows/ci.yml`로 설치할 수 있으며, 지금은 위 로컬 테스트 명령으로 검증합니다.

기존 Kimodo/Unreal 실험과 과거 결과물은 `.local/legacy/`에 보존됩니다.
GitHub에서 새로 클론하면 이 로컬 데이터는 포함되지 않습니다.
