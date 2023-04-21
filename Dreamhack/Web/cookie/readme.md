# [cookie](https://dreamhack.io/wargame/challenges/6/)

## 소스코드 분석

- `/` 접근
  - `/` 접근시 사용되는 코드

    ```python3
    @app.route('/')
    def index():
        username = request.cookies.get('username', None)
        if username:
            return render_template('index.html', text=f'Hello {username}, {"flag is " + FLAG if username == "admin" else "you are not admin"}')
        return render_template('index.html')
    ```

  - 코드 순서도

    ![index](/Dreamhack/Web/cookie/image/index.png)

- `/login' 접근
  - `/login` 접근시 실행되는 코드

  ```python3
  @app.route('/login', methods=['GET', 'POST'])
  def login():
      if request.method == 'GET':
          return render_template('login.html')
      elif request.method == 'POST':
          username = request.form.get('username')
          password = request.form.get('password')
          try:
              pw = users[username]
          except:
              return '<script>alert("not found user");history.go(-1);</script>'
          if pw == password:
              resp = make_response(redirect(url_for('index')) )
              resp.set_cookie('username', username)
              return resp 
          return '<script>alert("wrong password");history.go(-1);</script>'
  ```

  - 코드 순서도
