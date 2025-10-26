import streamlit as st
from pypdf import PdfReader
from docx import Document
import io
import uuid

st.title("PDF to Word Convertor")
st.write("Upload your PDF here:")
pdf = None
uploaded_file = st.file_uploader(" ", type = ["pdf"])

if uploaded_file is None:
    st.write ("Please upload your PDF file")
else:
    pdf = PdfReader(uploaded_file)
    st.write("PDF is uploaded successfully")
    st.write(f"Number of pages: {len(pdf.pages)}")
    doc = Document()
    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]
        text = page.extract_text()
        doc.add_paragraph(text)

    word_io = io.BytesIO()
    doc.save(word_io)
    word_io.seek(0)

    st.download_button(
        label = "Download Converted File",
        data = word_io,
        file_name = f"{uuid.uuid4()}.docx",
        mime= "application/vnd.openxmlformats-officedocument.wordprocessingml.doc"
    )
