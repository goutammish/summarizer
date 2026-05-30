import streamlit as st
from summarizer import summarize_text

st.set_page_config(
    page_title="Text Summarizer",
    page_icon="📝"
)

st.title("📝 Gemini Text Summarizer")

user_text = st.text_area(
    "Enter Paragraph",
    height=250
)

if st.button("Generate Summary"):

    if user_text.strip():

        with st.spinner("Generating Summary..."):

            summary = summarize_text(user_text)

            st.subheader("Summary")

            st.write(summary)

    else:
        st.warning("Please enter some text.")


