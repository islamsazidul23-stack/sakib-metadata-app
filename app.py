import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# ---------- API KEY ----------
genai.configure(api_key=os.getenv("AIzaSyAh0ZwruNLMEenW6YoWgdtgxGcRzLqtXC0"))

model = genai.GenerativeModel("gemini-1.5-flash")

# ---------- PAGE ----------
st.set_page_config(
    page_title="Sakibul Metadata Studio",
    page_icon="📸",
    layout="wide"
)

# ---------- LUXURY STYLE ----------
st.markdown("""
<style>

body {
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
}

.main-title {
font-size:50px;
font-weight:800;
text-align:center;
color:#FFD700;
margin-bottom:10px;
}

.sub-title{
text-align:center;
font-size:18px;
color:#dddddd;
margin-bottom:40px;
}

.result-box{
background:#1c1f26;
padding:20px;
border-radius:12px;
box-shadow:0 0 15px rgba(0,0,0,0.6);
margin-top:15px;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">SAKIBUL METADATA STUDIO</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Professional AI Metadata Generator For Adobe Stock</div>', unsafe_allow_html=True)

# ---------- UPLOAD ----------
uploaded_files = st.file_uploader(
"Upload Images",
accept_multiple_files=True,
type=["jpg","jpeg","png"]
)

prompt = """
You are a professional Adobe Stock image SEO specialist.

Generate metadata following Adobe Stock rules.

Title under 120 characters.
Description under 140 characters.
Exactly 49 keywords.
No commas in title.
"""

if uploaded_files:

    for file in uploaded_files:

        image = Image.open(file)

        col1, col2 = st.columns([1,2])

        with col1:
            st.image(image, use_column_width=True)

        with col2:

            with st.spinner("Generating metadata..."):

                response = model.generate_content([prompt, image])

                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.write(response.text)
                st.markdown('</div>', unsafe_allow_html=True)
