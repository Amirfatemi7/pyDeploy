import requests
import os
import dotenv


dotenv = dotenv.load_dotenv()

url = "https://api.github.com/user"
token = os.getenv("gitHub_token")
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": token,
    "X-GitHub-Api-Version": "2022-11-28" 
}
payload = {
   
}
response = requests.get(url, headers=headers, params= payload)
print(response.status_code)
resp_json = response.json()
print("number of followers", resp_json["followers"])
print("number of following", resp_json["following"])