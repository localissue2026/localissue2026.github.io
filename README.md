# LOCAL ISSUE QR

`https://localissue2026.github.io/qr/{번호}` 로 들어온 접속을 QR 관리 시스템의 같은 번호로 넘겨 주는 정적 리다이렉트 사이트입니다.

- `qr/{번호}.html` : 번호별 리다이렉트 페이지 (`build.py` 로 생성)
- `404.html` : 미리 만들어 두지 않은 번호를 위한 예비 경로
- 번호 범위를 늘리려면 `build.py` 의 `LAST` 를 바꾸고 `python3 build.py` 실행 후 커밋

행사 인쇄물의 QR 이 이 주소를 가리키므로, QR 이 쓰이는 동안에는 저장소를 삭제하거나 비공개로 바꾸면 안 됩니다.
