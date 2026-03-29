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
st.caption("Fast SEO Metadata Generator")

# Upload
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

# FAST PROMPT
prompt = """
Generate SEO metadata for stock image:
Title
Description (1 short sentence)
20 keywords
"""

# Process
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, width=300)

    if st.button("Generate Metadata"):

        with st.spinner("Generating..."):
            response = model.generate_content([prompt, image])

        st.subheader("Result")
        st.text(response.text)
