import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
from concurrent.futures import ThreadPoolExecutor

# API
genai.configure(api_key=os.getenv("AIzaSyAh0ZwruNLMEenW6YoWgdtgxGcRzLqtXC0"))

model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Sakib Metadata Studio", layout="wide")

st.title("SAKIB TECHNOLOGY METADATA HOUSE")
st.caption("Fast AI Metadata Generator for Adobe Stock")

uploaded_files = st.file_uploader(
    "Upload Images",
    accept_multiple_files=True,
    type=["jpg","jpeg","png"]
)

prompt = """
Generate Adobe Stock metadata.

Title under 100 characters
Description under 120 characters
49 keywords

Format:

Title:
Description:
Keywords:
"""

def generate_metadata(file):

    image = Image.open(file)
    image = image.resize((400,400))

    response = model.generate_content([prompt, image])

    return image, response.text


if uploaded_files:

    st.success(f"{len(uploaded_files)} images uploaded")

    results = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        for result in executor.map(generate_metadata, uploaded_files):
            results.append(result)

    for img, meta in results:

        col1, col2 = st.columns([1,2])

        with col1:
            st.image(img, use_column_width=True)

        with col2:
            st.code(meta)
