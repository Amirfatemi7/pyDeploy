import requests
import os
import dotenv


dotenv = dotenv.load_dotenv()

url = "https://api.iconfinder.com/v4/icons/search"

headers = {
    "accept": "application/json",
    "Authorization": os.getenv("icon_finder_token")
}
payload = {
    "query": "arrow",
    "count": "10"
}
response = requests.get(url, headers=headers, params= payload)
print(response.status_code)
print(response.json())