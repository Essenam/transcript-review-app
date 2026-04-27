import streamlit as st
import pandas as pd
import base64

st.set_page_config(layout="wide")

# -------------------------
# SESSION STATE
# -------------------------
if "page" not in st.session_state:
    st.session_state.page = "dashboard"

if "selected" not in st.session_state:
    st.session_state.selected = None

# -------------------------
# MOCK DATA
# -------------------------
def get_mock_applications():
    return [
        {"id": 1, "name": "John Doe", "status": "Pending", "confidence": 72, "decision": "Review"},
        {"id": 2, "name": "Jane Smith", "status": "Approved", "confidence": 96, "decision": "Accept"},
        {"id": 3, "name": "Mike Lee", "status": "In Review", "confidence": 65, "decision": "Review"},
    ]

# -------------------------
# DASHBOARD PAGE
# -------------------------
if st.session_state.page == "dashboard":

    st.title("📄 Transcript Evaluation Dashboard")

    col1, col2 = st.columns([3, 1])

    # Search
    with col1:
        search = st.text_input("🔍 Search")

    # Upload
    with col2:
        uploaded_file = st.file_uploader(
            "Upload",
            type=["pdf"],
            label_visibility="collapsed"
        )

    # Upload → open viewer
    if uploaded_file:
        st.session_state.selected = {
            "name": uploaded_file.name,
            "status": "Review",
            "confidence": 70,
            "decision": "Review",
            "file": uploaded_file
        }
        st.session_state.page = "viewer"
        st.rerun()

    st.markdown("---")

    # HEADER ROW
    header_cols = st.columns([2, 1, 1, 1, 1])
    header_cols[0].markdown("**Student Name**")
    header_cols[1].markdown("**Status**")
    header_cols[2].markdown("**Confidence**")
    header_cols[3].markdown("**AI Recommendation**")
    header_cols[4].markdown("**Action**")

    st.markdown("---")

    # DATA ROWS
    data = get_mock_applications()

    for i, row in enumerate(data):
        cols = st.columns([2, 1, 1, 1, 1])

        cols[0].write(f"{i+1}. {row['name']}")
        cols[1].write(row["status"])
        cols[2].write(f"{row['confidence']}%")
        cols[3].write(row["decision"])

        if cols[4].button("Open", key=f"open_{i}"):
            st.session_state.selected = row
            st.session_state.page = "viewer"
            st.rerun()

# -------------------------
# VIEWER PAGE
# -------------------------
elif st.session_state.page == "viewer":

    # Back button
    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()

    st.title("📄 Transcript Viewer")

    left, right = st.columns([2, 1])

    selected = st.session_state.selected

    # -------------------------
    # LEFT: PDF VIEWER
    # -------------------------
    with left:
        st.subheader("📄 Transcript Viewer")

        if selected and "file" in selected:
            pdf_bytes = selected["file"].read()
            base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

            pdf_display = f"""
            <iframe src="data:application/pdf;base64,{base64_pdf}" 
            width="100%" height="600px">
            </iframe>
            """
            st.markdown(pdf_display, unsafe_allow_html=True)
        else:
            st.info("No file preview available (backend will provide this later)")

    # -------------------------
    # RIGHT: DATA PANEL
    # -------------------------
    with right:
        st.subheader("📊 Extracted Data")

        if selected:

            # 👤 Student Info
            st.markdown("### 👤 Student Info")
            name = st.text_input("Name", selected["name"])
            dob = st.text_input("DOB", "01/01/2000")

            # 🎓 GPA
            st.markdown("### 🎓 GPA")
            raw_gpa = st.text_input("Raw GPA", "8.5 / 10")
            normalized_gpa = st.text_input("Normalized GPA", "3.4")

            # 📚 Courses
            st.markdown("### 📚 Courses")
            df = pd.DataFrame({
                "Course": ["Math 101", "Eng 201"],
                "Credits": [3, 4],
                "Grade": ["B", "A"],
                "Norm": [3.0, 4.0]
            })
            st.dataframe(df, use_container_width=True)

            # 🚩 Flags
            st.markdown("### 🚩 Flags")
            st.error("Missing GPA scale")
            st.error("Unclear grading format")

            # 🤖 AI Summary
            st.markdown("### 🤖 AI Summary")
            st.write("Decision:", selected.get("decision", "--"))
            st.write("Confidence:", f"{selected.get('confidence', '--')}%")

            # 📝 Notes
            st.markdown("### 📝 Notes")
            notes = st.text_area("Add notes")

            # ⚡ Actions
            st.markdown("### ⚡ Actions")
            col1, col2, col3 = st.columns(3)

            with col1:
                if st.button("✅ Accept"):
                    st.success("Accepted")

            with col2:
                if st.button("🟡 Review"):
                    st.warning("Marked for review")

            with col3:
                if st.button("🔴 Reject"):
                    st.error("Rejected")