import streamlit as st
import google.generativeai as genai
from PIL import Image

# 🔑 PUT YOUR API KEY HERE
genai.configure(api_key="AIzaSyDfsKcX8-7fq-YYLIAGIlk4Cy6atiuBOTk")

model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Sakib Technology", layout="wide")

st.title("SAKIB TECHNOLOGY")
st.caption("Adobe Stock SEO Metadata Generator")

uploaded_files = st.file_uploader(
    "Upload Images",
    accept_multiple_files=True,
    type=["jpg","jpeg","png"]
)

prompt = """
You are a professional Adobe Stock image SEO specialist.

Your task is to generate SEO-optimized metadata for an Adobe Stock image.

STRICT RULES (MUST FOLLOW):

TITLE RULES:
- Maximum 120 characters.
- The FIRST PHRASE of the Title must be IDENTICAL to the FIRST keyword.
- The FIRST 5 keywords MUST appear in the Title in the same order.
- Title must clearly describe the main subject and visible context.
- Use natural commercial stock language.
- No brand names.
- Do NOT mention AI, artificial, generated, render, illustration, photo, image, software.

DESCRIPTION RULES:
- 1–2 natural sentences.
- Maximum 140 characters.
- Describe subject + environment + commercial use.
- No marketing claims.
- No emotional exaggeration.

KEYWORD RULES:
- EXACTLY 49 keywords.
- Comma-separated.
- Include a comma after the last keyword.
- No duplicate full keywords.
- First 10 keywords must represent strong commercial search intent.
- Use generic, evergreen, commercial language.
- No brand names.
- No forbidden terms.
- All keywords must be visually provable.

FINAL VALIDATION BEFORE OUTPUT:
- Confirm first phrase of Title matches first keyword exactly.
- Confirm first 5 keywords appear in Title in the same order.
- Confirm exactly 49 keywords.
- Confirm no duplicate full keywords.
- Confirm Title under 100 characters.

English language only.
Present tense only.
Suitable for Adobe Stock commercial licensing.

INPUT:
Describe the image clearly in ONE simple sentence.

OUTPUT FORMAT (ONLY THIS):

Title:
Description:
Keywords:
"""

if uploaded_files:

    for file in uploaded_files:

        image = Image.open(file)

        st.image(image, width=300)

        with st.spinner("Generating metadata..."):

            response = model.generate_content([prompt, image])

        st.text(response.text)
