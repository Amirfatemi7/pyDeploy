import requests
import os
import dotenv

dotenv = dotenv.load_dotenv()
url = "https://api.d-id.com/clips/clp_AhbmyjaDsvcCt8dcHIXmw"

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": os.getenv("D_ID_token")
}

resp = requests.get(url, headers=headers)
print(resp.status_code)
print(resp.json())

