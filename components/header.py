import streamlit as st

def render_header():
    st.markdown("""
    <div class="header">
        <h2>📄 Transcript Evaluation Dashboard</h2>
        <p>Human-in-the-loop admissions review prototype</p>
    </div>
    """, unsafe_allow_html=True)