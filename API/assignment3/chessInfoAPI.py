from fastapi import FastAPI, HTTPException, status
from fastapi.responses import StreamingResponse, FileResponse, RedirectResponse
# from typing import Union
from pathlib import Path

app = FastAPI()

data = {
    "bishop": ".فیل ُ با حرکت به صورت ضربدر می تواند حرکت کند",
    "king": ".شاه ُ می تواند در همه جهت ها و فقط یک خانه حرکت کند",
    "knight": "اسب ُ حرکت بصورت L می باشد.",
    "pawn": "سرباز ُ در مرحله اول یک یا دو خانه رو به جلو حرکت می کند و در ادامه فقط یک خانه رو به جلو حرکت می کند.",
    "queen": "ملکه یا وزیر ُ در همه جهت ها و به هر میزان می تواند حرکت کند.",
    "rook": "رخ یا قلعه ُ حرکت به صورت جلو و عقب و چپ و راست حرکت می کند"
    }

@app.get("/")
def root():
    return "سلام به صفحه ما خوش آمدید. شما می توانید اطلاعاتی در مورد شاه ُ ملکه ُ فیل ُ رخ ُ سرباز و اسب بدست آورید"

@app.get("/pieces")
def pieces():
    return data

@app.get("/pieces/{piece_name}")
def pieces_name(piece_name: str):
    try:
        match piece_name:
            case "bishop":
                return data["bishop"]
            case "king":
                return data["king"]
            case "knight":
                return data["knight"]
            case "pawn":
                return data["pawn"]
            case "queen":
                return data["queen"]
            case "rook":
                return data["rook"]
            case _:
                return "dont have in database"
    except Exception as e:
        print("error : ",e)
        raise  HTTPException(status_code= status.HTTP_502_BAD_GATEWAY, detail= " ")

@app.get("/pieces/image/{piece_name}")
def pieces_img(piece_name: str):
    
    try:
        match piece_name:
            case "bishop":
                image_path = Path("/img/bishop.png")
                if not image_path.is_file():
                    return {"error": "Image not found on the server"}
                return FileResponse(image_path)
            case "king":
                image_path = Path("/img/king.png")
                if not image_path.is_file():
                    return {"error": "Image not found on the server"}
                return FileResponse(image_path)
            case "knight":
                image_path = Path("/img/knight.png")
                if not image_path.is_file():
                    return {"error": "Image not found on the server"}
                return FileResponse(image_path)
            case "pawn":
                image_path = Path("/img/pawn.png")
                if not image_path.is_file():
                    return {"error": "Image not found on the server"}
                return FileResponse(image_path)

            case "queen":
                image_path = Path("/img/queen.png")
                if not image_path.is_file():
                    return {"error": "Image not found on the server"}
                return FileResponse(image_path)

            case "rook":
                image_path = Path("/img/rook.png")
                if not image_path.is_file():
                    return {"error": "Image not found on the server"}
                return FileResponse(image_path)
            
   
    except Exception as e:
        print("error : ",e)
        raise  HTTPException(status_code= status.HTTP_502_BAD_GATEWAY, detail= "error in gateway")
    
    

   


