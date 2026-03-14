import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

genai.configure(api_key=os.getenv("AIzaSyAh0ZwruNLMEenW6YoWgdtgxGcRzLqtXC0"))

model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(
    page_title="Sakibul Metadata Studio",
    layout="wide"
)

st.title("SAKIBUL METADATA STUDIO")
st.caption("Ultra Fast Adobe Stock Metadata Generator")

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

if uploaded_files:

    st.success(f"{len(uploaded_files)} images uploaded")

    for file in uploaded_files:

        image = Image.open(file)

        # FAST resize
        image = image.resize((300,300))

        st.image(image, width=250)

        with st.spinner("Generating metadata..."):

            response = model.generate_content([prompt, image])

        st.code(response.text)
