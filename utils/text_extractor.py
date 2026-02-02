import PyPDF2

def extract_text(uploaded_file):
    """Handles the heavy lifting of reading files."""
    if uploaded_file.type == "application/pdf":
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text.strip()
    elif uploaded_file.type == "text/plain":
        return uploaded_file.read().decode("utf-8").strip()
    return None