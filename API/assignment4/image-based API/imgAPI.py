from deepface import DeepFace
from fastapi import FastAPI, File, Form, UploadFile, HTTPException, status

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/analyze")
async def analyze_img(file: UploadFile | None = None):
     if not file:
        raise HTTPException(status_code= status.HTTP_304_NOT_MODIFIED,detail="try to upload file") 
     else:
        img = await file.read()
        f = open('img.jpg','wb')
        f.write(img) 
        f.close()

        objs = DeepFace.analyze(img_path = "img.jpg", 
                actions = ['age', 'gender', 'race', 'emotion']
        )

        # print(objs)
        return {"Facial Attribute Analysis": objs}


