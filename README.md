EvidenceFirst — AI PDF Research Assistant

EvidenceFirst is a Python-based PDF research assistant that helps users find relevant evidence from PDF documents by asking questions in plain English.

Features

- Upload and read PDF documents.
- Extract readable text from PDF pages.
- Ask questions about the document.
- Retrieve relevant passages using keyword matching.
- Display page numbers alongside the evidence.
- Show a warning when matching evidence cannot be found.

Tech Stack

- Python
- Streamlit
- PyPDF
- Keyword-based text retrieval

How It Works

1. Upload a PDF file.
2. Enter a question about the document.
3. Click Find Evidence.
4. Review the matching text and its page number.

Limitations

This project uses keyword matching to find relevant passages. It does not use a large language model (LLM) to generate answers, and it may miss relevant evidence when different words are used in the question and document. Scanned PDFs without readable text may not work correctly.

Run Locally

Install the required packages:

pip install -r requirements.txt

Run the application:

streamlit run app.py

Project Status

Educational project demonstrating PDF text extraction, keyword search, and evidence-based information retrieval.
