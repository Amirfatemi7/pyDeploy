import argparse
import requests
import os
import dotenv
from PIL import Image 

dotenv = dotenv.load_dotenv()
url = "https://fal.run/fal-ai/illusion-diffusion"
url_plant= "https://my-api.plantnet.org/v2/identify/all"

headers = {
    "Content-Type": "application/json",
    "Authorization": os.getenv("illusion_diffusion_token")
}

parser = argparse.ArgumentParser()
parser.add_argument('plant_name', help='enter plant or flower name to display image')
parser.add_argument('-display', '--show', help='display image', action='store_true')
args = parser.parse_args()

if args.show:


    payload = {
        "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/funky.jpeg",
        "prompt": "(masterpiece:1.4), (best quality), (detailed), a "+ args.plant_name +" plant ",
        "negative_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t",
    }

    try:
        resp = requests.post(url, headers=headers, json= payload)
        json_resp = resp.json()
        print(json_resp['image']['url'])
        
    except requests.exceptions.Timeout:
        print("show image api timeout")
    except requests.exceptions.ConnectionError:
        print("show image api ConnectionError")
    except resp.status_code !=200 as s:
        print("status code : ",s )
    except Exception as e:
        print("error : ",e)
    
    data = requests.get(json_resp['image']['url']).content
    # print(data)
    f = open('img.jpg','wb')
    f.write(data) 
    f.close() 
    
    img = Image.open('img.jpg') 
    img.show()

    payload_plant = {
    "api-key": os.getenv("plant_token")
    }
    files = {
        "images": open("img.jpg", "rb")
        
    }
    headers_plant = {

    }
    try:
        resp_plant = requests.post(url_plant, headers=headers_plant, params=payload_plant, files=files)
        json_resp_plant  = resp_plant.json()
        # print(json_resp_plant)
        # print(json_resp_plant['results'][0]['species'])
        print("image name:",json_resp_plant['results'][0]['species']['scientificNameWithoutAuthor'])
    except requests.exceptions.Timeout:
        print("plant api timeout")
    except requests.exceptions.ConnectionError:
        print("plant api ConnectionError")
    # except resp_plant.status_code !=200 as s:
    #     print("status code : ",s )
    except Exception as e:
        print("error : ",e)

else:
    print('write action and try again')