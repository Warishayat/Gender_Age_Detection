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
You are a facial analysis expert.

Your task is to predict the gender and age of the person in the uploaded image.

⚠️ Only respond if you are at least 90% confident in your prediction.

Instructions:

- If there is **no human face**, respond only with:
  {
    "error": "No human detected."
  }

- If your **confidence is below 90%**, respond only with:
  {
    "error": "Confidence below 90%. Cannot provide a reliable prediction."
  }

- If a face is detected and you are confident (≥ 90%), respond **only** in this exact JSON format:
  {
    "Gender": "Male" or "Female" or "Transgender",
    "Age": estimated integer age,
    "Confidence": "percent string like '91%'"
  }

Return ONLY valid JSON.
No markdown.
No explanations.
No extra formatting.
.
"""

def Analyze_image_and_Age(image_path):
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content([
        prompt,
        {"mime_type": "image/jpeg", "data": image_path}
    ])
    
    return response.text


if __name__ == "__main__":
    image_path = r"C:\Users\HP\Desktop\Gneder-Dtection\Backend\dp.jpeg"
    Analyze_image_and_Age(image_path)
