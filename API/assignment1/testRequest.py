import json
import requests

resp = requests.get("https://goweather.herokuapp.com/weather/" + "Tehran")

res = resp.json()
print(res["temperature"])
print(res["forecast"][0]["temperature"])
