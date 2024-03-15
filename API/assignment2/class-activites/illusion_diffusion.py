import requests
import os
import dotenv

dotenv = dotenv.load_dotenv()
url = "https://fal.run/fal-ai/illusion-diffusion"

headers = {
    "Content-Type": "application/json",
    "Authorization": os.getenv("illusion_diffusion_token")
}

payload = {
    "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/pattern.png",
    "prompt": "(masterpiece:1.4), (best quality), (detailed), a yellow ferrary car",
    "negative_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t",

}


resp = requests.post(url, headers=headers, json= payload)
print(resp.status_code)
print(resp.json())