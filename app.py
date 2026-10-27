import streamlit as st
from pdf_reader import extract_text_from_pdf
from search_engine import search_relevant_passages

st.set_page_config(page_title="EvidenceFirst", page_icon="📄")

st.title("EvidenceFirst")
st.write("Ask questions about a PDF and find supporting evidence.")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    try:
        pages = extract_text_from_pdf(uploaded_file)

        if not pages:
            st.warning(
                "No readable text found. The PDF may be scanned or image-based."
            )
        else:
            st.success(f"PDF loaded: {len(pages)} pages with readable text.")

            question = st.text_input("Ask a question about this PDF")

            if st.button("Find Evidence"):
                if not question.strip():
                    st.warning("Please enter a question first.")
                else:
                    results = search_relevant_passages(question, pages)

                    if not results:
                        st.warning("I couldn't find matching evidence in this PDF.")
                    else:
                        st.subheader("Relevant evidence")

                        for result in results:
                            st.markdown(f"**Page {result['page']}**")
                            st.write(result["text"])
                            st.divider()

    except Exception as error:
        st.error(f"Could not read this PDF: {error}")