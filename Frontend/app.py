import streamlit as st
import requests
from PIL import Image
import pandas as pd

API_URL = "https://gender-age-detection-1.onrender.com/Analyze_image"


st.set_page_config(page_title="CareCloud Gender & Age Detection", layout="centered")
st.title("🧠 CareCloud Gender & Age Detection")
st.markdown("Upload face images to detect gender and age using AI.")


if "results" not in st.session_state:
    st.session_state.results = []


uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="🖼️ Uploaded Image", use_container_width=True)

    if st.button("🔍 Analyze"):
        with st.spinner("Analyzing..."):
            try:
                image_bytes = uploaded_file.getvalue()
                files = {"file": (uploaded_file.name, image_bytes, uploaded_file.type)}

                response = requests.post(API_URL, files=files)

                if response.status_code == 200:
                    result = response.json().get("response", {})

                    st.session_state.results.append({
                        "Image": uploaded_file.name,
                        "Gender": result.get("Gender", "N/A"),
                        "Age": result.get("Age", "N/A"),
                        "Confidence": result.get("Confidence", "N/A")
                    })

                    st.success("✅ Prediction Successful!")
                    st.markdown(f"**👤 Gender:** `{result.get('Gender', 'N/A')}`")
                    st.markdown(f"**📅 Age:** `{result.get('Age', 'N/A')}`")
                    st.markdown(f"**🎯 Confidence:** `{result.get('Confidence', 'N/A')}`")

                else:
                    st.error("❌ Prediction failed.")
                    st.json(response.json())

            except Exception as e:
                st.error(f"⚠️ Error: {e}")


if st.session_state.results:
    st.markdown("### 📊 Session Log")
    df = pd.DataFrame(st.session_state.results)
    st.dataframe(df, use_container_width=True)

    
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Session Log as CSV",
        data=csv,
        file_name="gender_age_results.csv",
        mime="text/csv"
    )
else:
    st.markdown("ℹ️ No predictions yet. Upload an image and click **Analyze** to begin.")
