import requests
import os
import dotenv

dotenv = dotenv.load_dotenv()
url = "https://api.d-id.com/clips"

payload = {
    "script": {
        "type": "text",
        
        "provider": {
            "type": "microsoft",
            "voice_id": "en-US-JennyNeural"
        },
        "ssml": "false",
        "input": "Hi there, I am your smart assistant. ask me your questions"
    },
    "config": { "result_format": "mp4" },
    "presenter_config": { "crop": { "type": "wide" } },
    "background": {"color": "false"},
    "presenter_id": "amy-sEIU0O2gBy"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": os.getenv("D_ID_token")
}

response = requests.post(url, json=payload, headers=headers)
print(response.status_code)
print(response.json())

