from fastapi import FastAPI

app = FastAPI()

@app.get("/test1")
def root():
    return {"test1": "hi every body"}

