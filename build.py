#!/usr/bin/env python3
"""LOCAL ISSUE QR 리다이렉트 사이트 생성기.

https://localissue2026.github.io/qr/{번호}  ->  https://www.life-mention.com/qr/{번호}
(라이프멘션 QR관리에서 연결 주소 수정·접속수 집계가 그대로 동작한다)

GitHub Pages 는 정적 호스팅이라 서버 리다이렉트가 없다. 그래서
- qr/{번호}.html : 번호별 페이지(HTTP 200). /qr/{번호} 주소로 그대로 열린다.
- 404.html       : 미리 만들어 두지 않은 번호를 위한 예비 경로(같은 스크립트).
번호 범위를 늘리려면 LAST 를 바꾸고 다시 실행한다:  python3 build.py
"""
import pathlib

TARGET = "https://www.life-mention.com/qr/"
FIRST, LAST = 1, 1500

ROOT = pathlib.Path(__file__).parent

PAGE = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>LOCAL ISSUE</title>
<meta http-equiv="refresh" content="0; url={target}{id}">
<script>location.replace("{target}{id}");</script>
</head>
<body></body>
</html>
"""

FALLBACK = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>LOCAL ISSUE</title>
<script>
(function () {{
  var m = location.pathname.match(/\\/qr\\/(\\d+)\\/?$/);
  if (m) location.replace("{target}" + m[1]);
}})();
</script>
</head>
<body></body>
</html>
"""

INDEX = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>LOCAL ISSUE</title>
</head>
<body></body>
</html>
"""

qr = ROOT / "qr"
qr.mkdir(exist_ok=True)
for old in qr.glob("*.html"):
    old.unlink()
for i in range(FIRST, LAST + 1):
    (qr / f"{i}.html").write_text(PAGE.format(target=TARGET, id=i), encoding="utf-8")

(ROOT / "404.html").write_text(FALLBACK.format(target=TARGET), encoding="utf-8")
(ROOT / "index.html").write_text(INDEX, encoding="utf-8")
(ROOT / ".nojekyll").write_text("", encoding="utf-8")
print(f"generated qr/{FIRST}.html ~ qr/{LAST}.html, 404.html, index.html")
