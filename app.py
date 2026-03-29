import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

# API KEY
genai.configure(api_key=os.getenv("AIzaSyA9wBvtzlAn8jiRHS6Fr0g7NgEKzMyXs0Y"))

# FAST MODEL
model = genai.GenerativeModel("gemini-2.5-flash")

# UI
st.set_page_config(page_title="Sakib Technology", layout="wide")

st.title("SAKIB TECHNOLOGY")
st.caption("Auto SEO Metadata Generator (Bulk Images)")

# Upload multiple images
uploaded_files = st.file_uploader(
    "Upload Images",
    accept_multiple_files=True,
    type=["jpg", "jpeg", "png"]
)

# 🔥 CLEAN PROMPT (NO ,,,, ISSUE)
prompt = """
Generate Adobe Stock SEO metadata.

RULES:
- Title max 100 characters (clean, no commas, no symbols)
- Description 1 short sentence
- Generate exactly 25 keywords (comma separated)
- First keyword must match title start
- No brand names
- Use simple commercial language

FORMAT:
Title:
Description:
Keywords:
"""

# Generate for all images
if uploaded_files:

    if st.button("Generate All Metadata"):

        for file in uploaded_files:
            image = Image.open(file)

            st.image(image, width=250)

            with st.spinner(f"Processing {file.name}..."):
                response = model.generate_content([prompt, image])

            st.success(f"Done: {file.name}")
            st.text(response.text)
