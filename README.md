# 🧠 Gender & Age Detection AI App

This project is a full-stack AI web application that detects the **gender** and **age** of a person from an uploaded image using Google Gemini (Generative AI). Built using **FastAPI** for the backend and **Streamlit** for the frontend.

---

## 🚀 Live Demos

- 🔹 **Frontend (Streamlit)**: [Click Here](https://your-streamlit-app-url)  
- 🔹 **Backend (FastAPI)**: [Click Here](https://your-render-backend-url)

---

## 📦 Tech Stack

| Layer    | Tech |
|----------|------|
| 🧠 AI     | Google Gemini API (via `google.generativeai`) |
| 🖼️ Image  | `PIL` for image processing and conversion |
| 🧪 Backend | FastAPI |
| 🌐 Frontend | Streamlit |
| ☁️ Deployment | Render (Backend), Streamlit Cloud (Frontend) |

---

## 📂 Project Structure

```

Gender\_Age\_Detection/
│
├── Backend/
│   ├── main.py
│   ├── Age\_Detection.py
│   ├── requirements.txt
│   └── .env (with GEMINI\_API\_KEY)
│
├── Frontend/
│   ├── app.py
│   └── requirements.txt

````

---

## 🛠️ Setup Instructions

### ✅ Backend (FastAPI + Gemini)

1. Clone this repo:
   ```bash
   git clone https://github.com/Warishayat/Gender_Age_Detection.git
   cd Gender_Age_Detection/Backend
````

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file:

   ```
   GEMINI_API_KEY=your_google_gemini_api_key
   ```

5. Run the backend:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 10000
   ```

---

### ✅ Frontend (Streamlit)

1. Go to frontend folder:

   ```bash
   cd ../Frontend
   ```

2. Install frontend dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the frontend:

   ```bash
   streamlit run app.py
   ```

---

## ⚙️ Environment Variables

Only required in **backend**:

* `GEMINI_API_KEY`: Your Google Gemini API key

---

## 📸 How It Works

1. User uploads a face image via Streamlit.
2. Image is sent to FastAPI backend.
3. Backend:

   * Converts image to base64
   * Sends it to Google Gemini for analysis
   * Parses the result into structured JSON
4. Frontend displays predicted gender, age, and confidence score.

---

## ✅ Example Response

```json
{
  "Gender": "Male",
  "Age": 25,
  "Confidence": "87%"
}
```

---

## 📌 Future Improvements

* 🎨 UI Enhancements with Streamlit Components
* 🧠 Add face detection preprocessing
* 📤 Support multiple faces in one image
* 📈 Show detection confidence histogram

---

## 📜 License

This project is under the [MIT License](LICENSE).

---

## 🙌 Credits

Developed with ❤️ by [Waris Hayat](https://github.com/Warishayat)

```


