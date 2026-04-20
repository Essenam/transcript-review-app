import streamlit as st
import base64

st.set_page_config(layout="wide")

st.title("📄 Transcript Evaluation Dashboard")

uploaded_file = st.file_uploader("Upload Transcript", type=["pdf"])

# Always show layout
left, center, right = st.columns([1, 2, 1])

# LEFT PANEL
with left:
    st.subheader("📂 Queue")

    st.markdown("""
    **John Doe**  
    🔴 HIGH RISK  
    72% confidence  
    2 flags
    """)

# CENTER PANEL
with center:
    st.subheader("🧾 Review")

    col1, col2, col3 = st.columns(3)
    col1.metric("Confidence", "72%")
    col2.metric("Flags", "2")
    col3.metric("Status", "Request Review")

    st.markdown("---")

    st.write("### 👤 Student Info")
    st.write({
        "Name": "John Doe",
        "School": "XYZ University",
        "Program": "MS Business Analytics"
    })

    st.write("### 📊 Extracted Data")
    st.write({
        "GPA": "8.2 / 10",
        "Credits": "120"
    })

    st.write("### 🚩 Flags")
    st.warning("GPA scale not standard")
    st.warning("Missing course mapping")

# RIGHT PANEL
with right:
    st.subheader("⚡ Actions")

    st.button("✅ Accept")
    st.button("🟡 Request Review")
    st.button("🔴 Escalate")

    st.markdown("---")

    st.subheader("📄 Preview")

    if uploaded_file:
        pdf_bytes = uploaded_file.read()
        base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

        pdf_display = f"""
        <iframe src="data:application/pdf;base64,{base64_pdf}" 
        width="100%" height="500px">
        </iframe>
        """
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.info("Upload a transcript to preview it here.")