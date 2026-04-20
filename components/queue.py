import streamlit as st

def render_queue():
    st.markdown("### 📂 Transcript Queue")

    st.markdown("""
    <div class="card">
        <b>T-1023 - John Doe</b><br>
        Intl - GPA Missing<br><br>
        <span class="high">HIGH RISK</span><br>
        72% confidence<br>
        2 flags
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <b>T-1045 - Maria Chen</b><br>
        US - Scale unclear<br><br>
        <span class="medium">MEDIUM RISK</span><br>
        68% confidence
    </div>
    """, unsafe_allow_html=True)