EvidenceFirst

PDF Research Assistant

A Python-based application that helps users find relevant evidence in PDF documents by asking questions in plain English.

---

# About the Project

EvidenceFirst allows users to upload a PDF document, ask a question, and find a relevant passage with its page number.

# Key Features

- PDF Upload: Upload PDF documents.
- Text Extraction: Extract readable text from PDF pages.
- Question-Based Search: Ask questions about the document.
- Evidence Retrieval: Find passages matching question keywords.
- Page References: Display the page number of matching evidence.
- Error Handling: Show helpful messages when evidence cannot be found.

# Technologies Used

- Python
- Streamlit
- PyPDF
- Regular Expressions

# How It Works

1. Upload a PDF document.
2. Enter a question about the document.
3. The application searches the extracted text for matching keywords.
4. The best-matching passage and its page number are displayed.

# Installation and Setup

Step 1: Install Dependencies

pip install -r requirements.txt

Step 2: Run the Application

streamlit run app.py

# Project Structure

- "app.py" — Main application and user interface.
- "pdf_reader.py" — Extracts text from PDF pages.
- "search_engine.py" — Searches for relevant passages.
- "requirements.txt" — Lists the required Python packages.

# Limitations

EvidenceFirst uses keyword matching rather than a large language model or semantic search. It may return irrelevant passages or miss useful evidence when the question uses different wording from the document.

Scanned PDFs may require OCR to extract text.

# Future Improvements

- Add semantic search.
- Support scanned PDFs using OCR.
- Improve search accuracy.
- Test with more document types.

---

Developed using Python and Streamlit.
