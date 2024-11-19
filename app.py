import streamlit as st
import openai
from fpdf import FPDF
from docx import Document
from io import BytesIO

# Set up OpenAI API
openai.api_key = "your_api_key"


# Define OpenAI response generator
def generate_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use "gpt-3.5-turbo" if gpt-4 is unavailable
        messages=messages
    )
    return response.choices[0].message['content'].strip()


# Define functions for each task
def rewrite_text(text):
    messages = [{"role": "system", "content": "Rewrite the following text."}, {"role": "user", "content": text}]
    return generate_response(messages)


def extend_text(text):
    messages = [{"role": "system", "content": "Extend the following text."}, {"role": "user", "content": text}]
    return generate_response(messages)


def summarize_text(text):
    messages = [{"role": "system", "content": "Summarize the following text."}, {"role": "user", "content": text}]
    return generate_response(messages)


def fix_grammar(text):
    messages = [{"role": "system", "content": "Fix the grammar in the following text."},
                {"role": "user", "content": text}]
    return generate_response(messages)


def fix_code_bug(text):
    messages = [{"role": "system", "content": "Fix any code bugs in the following code."},
                {"role": "user", "content": text}]
    return generate_response(messages)


def optimize_code(text):
    messages = [{"role": "system", "content": "Optimize the following code."}, {"role": "user", "content": text}]
    return generate_response(messages)


# Function to sanitize text for FPDF
def sanitize_text_for_pdf(text):
    replacements = {
        "“": '"', "”": '"', "‘": "'", "’": "'",
        "—": "-", "–": "-", "…": "...",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


# Display output with download options
def display_output(text):
    sanitized_text = sanitize_text_for_pdf(text)
    st.markdown(f"<div class='output-container'><pre>{sanitized_text}</pre></div>", unsafe_allow_html=True)

    # Copy text
    if st.button("📋 Copy Text"):
        st.session_state['copied_text'] = text
        st.success("Text copied to clipboard! (Simulated)")

    # Download as TXT
    st.download_button("💾 Download as TXT", sanitized_text, "output.txt", "text/plain")

    # Download as PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, sanitized_text)
    pdf_output = pdf.output(dest="S").encode("latin1", "ignore")
    st.download_button("📄 Download as PDF", pdf_output, "output.pdf", "application/pdf")

    # Download as DOCX
    doc = Document()
    doc.add_paragraph(sanitized_text)
    doc_io = BytesIO()
    doc.save(doc_io)
    st.download_button("📄 Download as DOCX", doc_io.getvalue(), "output.docx",
                       "application/vnd.openxmlformats-officedocument.wordprocessingml.document")


# Custom CSS for styling
st.markdown("""
    <style>
        .output-container {
            background-color: #f0f4ff;
            border-radius: 8px;
            padding: 20px;
            font-size: 16px;
            color: #333;
            font-family: Arial, sans-serif;
            line-height: 1.6;
            overflow-wrap: break-word;
            white-space: pre-wrap;
        }
        .stButton > button {
            background-color: #007bff;
            border: none;
            color: white;
            padding: 8px 15px;
            font-size: 14px;
            margin: 5px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #0056b3;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit Interface
st.title("AI-Powered Web Application")
st.write("Choose a task from the options below:")

option = st.selectbox("Select an option", [
    "Rewrite", "Extend", "Summarize", "Fix Grammar", "Fix Code Bug", "Optimize Code"
])

# Processing based on user option
if option in ["Rewrite", "Extend", "Summarize", "Fix Grammar", "Fix Code Bug", "Optimize Code"]:
    text = st.text_area("Enter text here:")
    if st.button("Submit"):
        if option == "Rewrite":
            result = rewrite_text(text)
        elif option == "Extend":
            result = extend_text(text)
        elif option == "Summarize":
            result = summarize_text(text)
        elif option == "Fix Grammar":
            result = fix_grammar(text)
        elif option == "Fix Code Bug":
            result = fix_code_bug(text)
        elif option == "Optimize Code":
            result = optimize_code(text)
        display_output(result)
