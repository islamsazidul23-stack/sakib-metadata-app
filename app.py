import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# -------- API KEY --------
genai.configure(api_key=os.getenv("AIzaSyAh0ZwruNLMEenW6YoWgdtgxGcRzLqtXC0"))

# -------- FAST MODEL --------
model = genai.GenerativeModel("gemini-1.5-flash")

# -------- PAGE CONFIG --------
st.set_page_config(
    page_title="Sakibul Metadata Studio",
    page_icon="📸",
    layout="wide"
)

# -------- HEADER --------
st.title("SAKIBUL METADATA STUDIO")
st.caption("Fast AI Metadata Generator for Adobe Stock")

# -------- IMAGE UPLOAD --------
uploaded_files = st.file_uploader(
    "Upload Images",
    accept_multiple_files=True,
    type=["jpg","jpeg","png"]
)

# -------- PROMPT --------
prompt = """
You are a professional Adobe Stock image SEO specialist.

Generate:

Title under 120 characters.
Description under 140 characters.
Exactly 49 keywords.

Format:

Title:
Description:
Keywords:
"""

# -------- PROCESS --------
if uploaded_files:

    st.success(f"{len(uploaded_files)} images uploaded")

    for file in uploaded_files:

        image = Image.open(file)

        # resize for speed
        image = image.resize((600,600))

        st.image(image, width=300)

        with st.spinner("Generating metadata..."):

            response = model.generate_content([prompt, image])

        st.code(response.text)
