import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

# API KEY (from secrets)
genai.configure(api_key=os.getenv("AIzaSyC_b9FPKVkeIbpdhanpomgPdUD_SHRY3M8"))

model = genai.GenerativeModel("gemini-2.5-flash-latest")

# UI CONFIG
st.set_page_config(page_title="Sakib Technology PRO", layout="wide")

st.title("🚀 SAKIB TECHNOLOGY PRO")
st.caption("AI SEO Metadata Generator (Image + Video)")

# MODE SELECT
mode = st.selectbox("Select Mode", ["Image SEO", "Video SEO"])

# FILE UPLOAD
if mode == "Image SEO":
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
else:
    uploaded_file = st.file_uploader("Upload Video", type=["mp4", "mov", "avi"])

# PROMPT
prompt = """
You are a professional stock SEO expert.

Generate:
Title (max 100 chars)
Description (1-2 sentences, max 140 chars)
49 keywords (comma separated)

No brand names.
Commercial stock language only.
"""

# PROCESS
if uploaded_file:
    st.success("File uploaded successfully!")

    if st.button("Generate Metadata"):

        with st.spinner("Generating..."):

            if mode == "Image SEO":
                image = Image.open(uploaded_file)
                response = model.generate_content([prompt, image])
            else:
                # video case (basic text-based)
                response = model.generate_content(prompt + " This is a video file.")

            st.subheader("📌 Result")
            st.text(response.text)
