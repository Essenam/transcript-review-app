import streamlit as st

def render_review(data):

    st.markdown("### 🧾 Transcript Review")

    c1, c2, c3 = st.columns(3)
    c1.metric("Confidence", f"{data['confidence']}%")
    c2.metric("Flags", len(data["flags"]))
    c3.metric("Status", data["status"])

    st.markdown("---")

    st.markdown("### 👤 Student Info")
    st.write(data["student"])

    st.markdown("### 📊 Extracted Data")
    st.write(data["data"])

    st.markdown("### 🚩 AI Flags")
    for f in data["flags"]:
        st.warning(f)