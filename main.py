import streamlit as st
import pdfplumber

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    with pdfplumber.open(uploaded_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def main():
    st.title("PDF Chatbot")

    # File uploader widget
    uploaded_file = st.file_uploader("Upload a PDF", type=['pdf'])

    if uploaded_file is not None:
        # Display uploaded file
        st.write("Uploaded PDF:", uploaded_file.name)

        # Extract text from PDF
        text = extract_text_from_pdf(uploaded_file)
       # Query input field
        query = st.text_input("Enter your query:")

        if st.button("Search"):
            # Perform search in the extracted text
            if query.strip() != "":
                results = [line.strip() for line in text.split("\n") if query.lower() in line.lower()]
                if results:
                    st.write("Search Results:")
                    for result in results:
                        st.write(result)
                else:
                    st.write("No results found for the query.")
            else:
                st.write("Please enter a query.")
  if __name__ == "__main__":
      main()
