import streamlit as st
import base64

st.set_page_config(layout="wide")

st.title("📄 Transcript Evaluation Dashboard")

uploaded_file = st.file_uploader("Upload Transcript", type=["pdf"])

# Two columns instead of three
center, right = st.columns([2, 1])

# CENTER PANEL
with center:
    st.subheader("🧾 Review")

    if uploaded_file:
        confidence = "72%"
        flags = "2"
        status = "Request Review"
    else:
        confidence = "--"
        flags = "--"
        status = "Waiting for upload"

    col1, col2, col3 = st.columns(3)
    col1.metric("Confidence", confidence)
    col2.metric("Flags", flags)
    col3.metric("Status", status)

    st.markdown("---")

    st.write("### 👤 Student Info")
    if uploaded_file:
        st.write({
            "Name": "John Doe",
            "School": "XYZ University",
            "Program": "MS Business Analytics"
        })
    else:
        st.info("Upload a transcript to see details")

    st.write("### 📊 Extracted Data")
    if uploaded_file:
        st.write({
            "GPA": "8.2 / 10",
            "Credits": "120"
        })

    st.write("### 🚩 Flags")
    if uploaded_file:
        st.warning("Detected GPA scale (10-point) not aligned with 4.0 standard")
        st.warning("Missing course mapping for equivalency check")

# RIGHT PANEL
with right:
    st.subheader("⚡ Actions")

    if uploaded_file:
        if st.button("✅ Accept"):
            st.success("Application accepted")

        if st.button("🟡 Request Review"):
            st.warning("Marked for review")

        if st.button("🔴 Escalate"):
            st.error("Escalated to registrar")

    st.markdown("---")

    st.subheader("📄 Preview")

    if uploaded_file:
        pdf_bytes = uploaded_file.read()
        base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

        pdf_display = f"""
        <iframe src="data:application/pdf;base64,{base64_pdf}" 
        width="100%" height="600px">
        </iframe>
        """
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.info("Upload a transcript to preview it here.")