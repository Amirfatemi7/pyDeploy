import requests

url = "https://api.edenai.run/v2/text/question_answer"

payload = {
    "response_as_dict": True,
    "attributes_as_list": False,
    "show_original_response": True,
    "temperature": 0,
    "texts": ["The bar-shouldered dove (Geopelia humeralis) is a species of dove, in the family Columbidae, native to Australia and southern New Guinea. Its typical habitat consists of areas of thick vegetation where water is present, damp gullies, forests and gorges, mangroves, plantations, swamps, eucalyptus woodland, tropical and sub-tropical shrubland, and river margins. It can be found in both inland and coastal regions."],
    "providers": "tenstorrent,openai",
    "question": "What is the scientific name of bar-shouldered dove?",
    "examples_context": "In 2017, U.S. life expectancy was 78.6 years.",
    "examples": [["What is human life expectancy in the United States?", "What is human life expectancy in the United States?"]]
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNWMxZmQyYmYtY2EwNC00YjU5LTllY2UtZmI3NjkzZjIyZTYzIiwidHlwZSI6ImFwaV90b2tlbiJ9.zoI4D14-AOmGn4YlCEuhepfXCC1nfVFWcU7U8PunMYQ"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())