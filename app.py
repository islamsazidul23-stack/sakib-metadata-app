import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# -------- API KEY --------
genai.configure(api_key=os.getenv("AIzaSyAh0ZwruNLMEenW6YoWgdtgxGcRzLqtXC0"))

# -------- FAST MODEL --------
model = genai.GenerativeModel("gemini-2.5-flash")

# -------- PAGE CONFIG --------
st.set_page_config(
    page_title="Sakibul Metadata Studio",
    page_icon="📸",
    layout="wide"
)

# -------- LUXURY UI --------
st.markdown("""
<style>

body{
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
}

.title{
font-size:52px;
font-weight:800;
text-align:center;
color:#FFD700;
margin-bottom:5px;
}

.subtitle{
text-align:center;
font-size:18px;
color:#cccccc;
margin-bottom:35px;
}

.resultbox{
background:#1b1f27;
padding:20px;
border-radius:14px;
box-shadow:0 0 15px rgba(0,0,0,0.5);
margin-top:10px;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">SAKIBUL METADATA STUDIO</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Fast AI Metadata Generator for Adobe Stock</div>', unsafe_allow_html=True)

# -------- IMAGE UPLOAD --------
uploaded_files = st.file_uploader(
"Upload Images",
accept_multiple_files=True,
type=["jpg","jpeg","png"]
)

# -------- PROMPT --------
prompt = """
You are a professional Adobe Stock image SEO specialist.

TITLE RULES
Maximum 120 characters
First keyword must start the title
First 5 keywords must appear in title
No commas in title

DESCRIPTION RULES
1–2 natural sentences
Maximum 140 characters

KEYWORDS
Exactly 49 keywords
Comma separated
No duplicates

OUTPUT FORMAT

Title:
Description:
Keywords:
"""

# -------- PROCESS --------
if uploaded_files:

    st.success(f"{len(uploaded_files)} images uploaded")

    for file in uploaded_files:

        image = Image.open(file)

        col1, col2 = st.columns([1,2])

        with col1:
            st.image(image, use_column_width=True)

        with col2:

            with st.spinner("Generating metadata..."):

                response = model.generate_content([prompt, image])
                metadata = response.text

                st.markdown('<div class="resultbox">', unsafe_allow_html=True)
                st.code(metadata)

                st.download_button(
                    label="Copy Metadata",
                    data=metadata,
                    file_name="metadata.txt"
                )

                st.markdown('</div>', unsafe_allow_html=True)
