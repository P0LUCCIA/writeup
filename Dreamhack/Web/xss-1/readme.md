# [xss-1](https://dreamhack.io/wargame/challenges/28/)

## 소스코드 분석

- `def read_url()`
- `def check_xss()`
- `@app.route("/")`
- `@app.route("/vuln")`
- `@app.route("/flag", methods=["GET", "POST"])`
- `@app.route("/memo")`