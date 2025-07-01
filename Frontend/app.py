import streamlit as st
import requests
from PIL import Image

API_URL = "https://gender-age-detection-1.onrender.com/Analyze_image"

st.set_page_config(page_title="Gender & Age Detection", layout="centered")
st.title("Gender & Age Detection")
st.markdown("Upload an image of a face to detect gender and age using AI.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Analyze"):
        with st.spinner("Analyzing..."):
            try:
                image_bytes = uploaded_file.getvalue()
                files = {
                    "file": (uploaded_file.name, image_bytes, uploaded_file.type)
                }

                response = requests.post(API_URL, files=files)

                if response.status_code == 200:
                    result = response.json().get("response", {})

                    st.success("Prediction Successful!")
                    st.markdown(f"Gender: `{result.get('Gender', 'N/A')}`")
                    st.markdown(f"Age: `{result.get('Age', 'N/A')}`")
                    st.markdown(f"Confidence: `{result.get('Confidence', 'N/A')}`")

                else:
                    st.error("Prediction failed. Backend returned an error.")
                    st.json(response.json())

            except Exception as e:
                st.error(f" Unexpected error: {e}")
