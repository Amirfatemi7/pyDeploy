import requests
import os
import dotenv


dotenv = dotenv.load_dotenv()

url= "https://my-api.plantnet.org/v2/identify/all"

headers = {

}

payload = {
    "api-key": os.getenv("plant_token")
}

files = {
    "images": open("/home/amir/Pictures/img1.jpeg", "rb")
}
resp = requests.post(url, headers=headers, params=payload, files=files)
print(resp.status_code)
print(resp.json())