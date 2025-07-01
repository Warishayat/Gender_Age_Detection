from dotenv import load_dotenv
import google.generativeai as genai
import os
from PIL import Image
import io
import warnings
warnings.filterwarnings("ignore")


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=gemini_api_key)
prompt = """
Detect gender and age from the image. If no human is present, return:
{ "error": "No human detected." }

Otherwise, return:
{
  "Gender": "Male/Female/Transgender",
  "Age": integer,
  "Confidence": "percent"
}
"""

def Analyze_image_and_Age(image_path):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([
        prompt,
        {"mime_type": "image/jpeg", "data": image_path}
    ])
    
    return response.text


if __name__ == "__main__":
    image_path = r"C:\Users\HP\Desktop\Gneder-Dtection\Backend\dp.jpeg"
    Analyze_image_and_Age(image_path)
