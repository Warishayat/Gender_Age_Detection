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
You are an expert in facial analysis.

Your task is to detect **gender** and **age** from the uploaded image. Only proceed if you are at least **90% confident** in your prediction.

- If no human is detected, respond with:
  {
    "error": "No human detected."
  }

- If a human is detected, and you are at least 90% confident in the prediction, respond strictly in this JSON format:
  {
    "Gender": "Male" or "Female" or "Transgender",
    "Age": integer (estimated),
    "Confidence": "XX%" (a string percentage, must be 90% or higher)
  }

- If your confidence is below 90%, respond with:
  {
    "error": "Low confidence. Unable to predict reliably."
  }

Do not include markdown, explanations, or formatting — return only raw JSON.
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
