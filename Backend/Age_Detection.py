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
You are an AI model that detects gender and age from an image.

If no human is present, respond with:
{ "error": "No human detected." }

Otherwise, respond only with a valid raw JSON object like:
{ 
  "Gender": "Male", 
  "Age": 25, 
  "Confidence": "87%" 
}
Do not include any text, explanation, or markdown formatting. Just return the JSON object only.
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
