# [xss-1](https://dreamhack.io/wargame/challenges/28/)

## 소스코드 분석

- `def read_url()`
  - 코드
  ```python3
  def read_url(url, cookie={"name": "name", "value": "value"}):
    cookie.update({"domain": "127.0.0.1"})
    try:
        options = webdriver.ChromeOptions()
        for _ in [
            "headless",
            "window-size=1920x1080",
            "disable-gpu",
            "no-sandbox",
            "disable-dev-shm-usage",
        ]:
            options.add_argument(_)
        driver = webdriver.Chrome("/chromedriver", options=options)
        driver.implicitly_wait(3)
        driver.set_page_load_timeout(3)
        driver.get("http://127.0.0.1:8000/")
        driver.add_cookie(cookie)
        driver.get(url)
    except Exception as e:
        driver.quit()
        # return str(e)
        return False
    driver.quit()
    return True
  ```
- `def check_xss()`
  - 코드
  ```python3
  def check_xss(param, cookie={"name": "name", "value": "value"}):
    url = f"http://127.0.0.1:8000/vuln?param={urllib.parse.quote(param)}"
    return read_url(url, cookie)
  ```
- `@app.route("/")`
  - 코드
  ```python3
  @app.route("/")
  def index():
    return render_template("index.html")
  ```
- `@app.route("/vuln")`
  - 코드
  ```python3
  @app.route("/vuln")
  def vuln():
    param = request.args.get("param", "")
    return param
  ```
- `@app.route("/flag", methods=["GET", "POST"])`
  - 코드
  ```python3
  @app.route("/flag", methods=["GET", "POST"])
  def flag():
    if request.method == "GET":
        return render_template("flag.html")
    elif request.method == "POST":
        param = request.form.get("param")
        if not check_xss(param, {"name": "flag", "value": FLAG.strip()}):
            return '<script>alert("wrong??");history.go(-1);</script>'

        return '<script>alert("good");history.go(-1);</script>'
  ```
- `@app.route("/memo")`
  - 코드
  ```python3
  @app.route("/memo")
  def memo():
      global memo_text
      text = request.args.get("memo", "")
      memo_text += text + "\n"
      return render_template("memo.html", memo=memo_text)
  ```
