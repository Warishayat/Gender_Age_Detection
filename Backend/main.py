from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import google.generativeai as genai
import os
import io
import base64
from PIL import Image
from Age_Detection import Analyze_image_and_Age
import json

import warnings
warnings.filterwarnings('ignore')



load_dotenv()
gemini_api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)



app = FastAPI()

def convert_uploadfile_to_base64(file: UploadFile) -> str:
    image = Image.open(file.file)
    if image.mode != "RGB":
        image = image.convert("RGB")
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return encoded

@app.post("/Analyze_image")
async def analyze(file:UploadFile = File(...)):
    try:
        base64_image = convert_uploadfile_to_base64(file)
        result = Analyze_image_and_Age(base64_image)

        # Convert JSON string to dict if needed
        if isinstance(result, str):
            try:
                result = json.loads(result)
            except json.JSONDecodeError:
                result = {"raw": result}
        return {"response": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


