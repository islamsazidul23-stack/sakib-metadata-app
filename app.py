import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key="AIzaSyBNMlBlyqs0ec7MyTkfEssh5yyvnVCI3V8")

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("SAKIB TECHNOLOGY METADATA HOUSE")

uploaded_files = st.file_uploader("Upload Images", accept_multiple_files=True, type=["jpg","jpeg","png"])

prompt = """
You are a professional Adobe Stock image SEO specialist.

STRICT RULES:
- Title max 100 characters
- Description max 100 characters
- Exactly 49 keywords
- First keyword must match title start
- First 5 keywords must appear in title
- No AI words
- No brand names

OUTPUT FORMAT:
Title:
Description:
Keywords:
"""

if uploaded_files:
    for file in uploaded_files:
        image = Image.open(file)
        st.image(image, width=300)

        response = model.generate_content([prompt, image])

        st.write(response.text)
