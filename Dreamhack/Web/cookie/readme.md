# [cookie](https://dreamhack.io/wargame/challenges/6/)

## 소스코드 분석

- `@app.route('/')`
  - `/` 접근시 사용되는 코드

    ```python3
    @app.route('/')
    def index():
        username = request.cookies.get('username', None)
        if username:
            return render_template('index.html', text=f'Hello {username}, {"flag is " + FLAG if username == "admin" else "you are not admin"}')
        return render_template('index.html')
    ```
  - 코드 분석
  
    username 쿠키가 `admin`인 경우 `FLAG`를 출력
    
    username 쿠키가 `admin`이 아닐경우 `you are not admin` 출력

- `@app.route('/login', methods=['GET', 'POST'])`
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

  - 코드 분석
    
    POST 메서드를 통하여 `username`과 `password`를 받음
    
    `username` 값이 `users` dict에 있을 경우 value 값을 불러옴
      
      + value 값이 POST 메서드를 통해 받은 `password` 값과 비교한다
      
      + 참일 경우 
        
        + `username` cookie에 username을 넣음
        
        + 이후 `/` 리다이렉트
        
      + 거짓일 경우 
        
        + `wrong password`를 alert로 return
        
    `username` 값이 `users` dict에 없을 경우 `not found user`를 alert로 return


## 웹 분석

- `guest`로 로그인시 얻는 쿠키

  ![guest](https://raw.githubusercontent.com/M00nHeeSung/writeup/main/Dreamhack/Web/cookie/image/guest.png)

  다음과 같이 `username`이 쿠키가 guest로 되어있다.
  
  이를 통하여 `username`이 admin일 경우 공격이 가능하다고 다시 한번 확인 할 수 있었음.
  
## 공격

- `username` 쿠키 값을 `admin`으로 변경

  ![admin](https://raw.githubusercontent.com/M00nHeeSung/writeup/main/Dreamhack/Web/cookie/image/admin.png)

  `username` 쿠키 값이 `admin`일 경우 FLAG를 위와 같이 출력하는 것을 알 수 있다.
