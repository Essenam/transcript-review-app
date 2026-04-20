import streamlit as st
import base64

def render_pdf(file):

    st.markdown("### 📄 Transcript Preview")

    base64_pdf = base64.b64encode(file.read()).decode("utf-8")

    pdf_display = f"""
    <iframe src="data:application/pdf;base64,{base64_pdf}" 
    width="100%" height="500px"></iframe>
    """

    st.markdown(pdf_display, unsafe_allow_html=True)