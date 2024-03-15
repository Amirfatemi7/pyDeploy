import requests
import os
import dotenv

dotenv = dotenv.load_dotenv()
token = os.getenv("the_oneAPI_token")


headers = {
    "Authorization" : token
}
resp = requests.get("https://the-one-api.dev/v2/book", headers= headers)

print(resp.status_code)
print(resp.json())






# resp = requests.get("https://the-one-api.dev/v2/movie")
# print(resp.status_code)
# print(resp.json())