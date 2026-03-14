import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
from concurrent.futures import ThreadPoolExecutor

# API
genai.configure(api_key=os.getenv("AIzaSyAh0ZwruNLMEenW6YoWgdtgxGcRzLqtXC0"))

model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(
    page_title="Sakibul Metadata Studio",
    layout="wide"
)

# ---------- UI ----------
st.markdown(
"""
<style>

.title{
font-size:45px;
font-weight:700;
text-align:center;
color:#f1c40f;
}

.subtitle{
text-align:center;
color:gray;
margin-bottom:30px;
}

.box{
background:#f7f7f7;
padding:20px;
border-radius:10px;
margin-top:10px;
}

</style>
""",
unsafe_allow_html=True
)

st.markdown('<div class="title">SAKIBUL METADATA STUDIO</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Fast AI Metadata Generator for Adobe Stock</div>', unsafe_allow_html=True)

# ---------- UPLOAD ----------
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

# ---------- FUNCTION ----------
def generate_metadata(file):

    image = Image.open(file)

    # resize for speed
    image = image.resize((3240,1080))

    response = model.generate_content([prompt, image])

    return image, response.text


# ---------- PROCESS ----------
if uploaded_files:

    st.success(f"{len(uploaded_files)} images uploaded")

    with ThreadPoolExecutor() as executor:

        results = list(executor.map(generate_metadata, uploaded_files))

    for img, meta in results:

        col1, col2 = st.columns([1,2])

        with col1:
            st.image(img, use_column_width=True)

        with col2:
            st.markdown('<div class="box">', unsafe_allow_html=True)
            st.code(meta)
            st.markdown('</div>', unsafe_allow_html=True)
