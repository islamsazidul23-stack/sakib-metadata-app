import streamlit as st
import google.generativeai as genai
from PIL import Image

# =========================
# PUT YOUR API KEY HERE
# =========================
genai.configure(api_key="AIzaSyCAA3vc8ybXfuGMhu68zCMzsvDWZf436qc")

# Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="SAKIB TECHNOLOGY METADATA HOUSE", layout="wide")

st.title("SAKIB TECHNOLOGY METADATA HOUSE")
st.write("Professional Adobe Stock Metadata Generator")

uploaded_files = st.file_uploader(
    "Upload Images",
    accept_multiple_files=True,
    type=["jpg","jpeg","png"]
)

prompt = """
You are a professional Adobe Stock image SEO specialist.

STRICT RULES (MUST FOLLOW):

- Title max 100 characters
- Description max 100 characters
- Exactly 49 keywords
- First keyword must match title start
- First 5 keywords must appear in title
- No AI words
- No brand names
- English only

OUTPUT FORMAT:

Title:
Description:
Keywords:
"""

if uploaded_files:

    for file in uploaded_files:

        image = Image.open(file)

        st.image(image, width=350)

        with st.spinner("Generating SEO metadata..."):

            response = model.generate_content([prompt, image])

        st.success("Metadata Generated")

        st.write(response.text)
