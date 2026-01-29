import streamlit as st
from rewriter import rewrite_text

st.set_page_config(page_title="Tone & Style Rewriter")

st.title("Tone & Style Rewriter")

input_text = st.text_area(
    "Enter text to rewrite:",
    height=200
)

tone = st.selectbox(
    "Select tone:",
    ["formal", "friendly", "confident","funny"]
)

if st.button("Rewrite"):
    if not input_text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Rewriting..."):
            rewritten = rewrite_text(input_text, tone)
            st.subheader("Rewritten Text")
            st.write(rewritten)
