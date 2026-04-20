import streamlit as st

def render_actions():

    st.markdown("### ⚡ Decision Actions")

    if st.button("✅ Accept transcript"):
        st.success("Approved")

    if st.button("🟡 Request review"):
        st.warning("Needs review")

    if st.button("🔴 Escalate"):
        st.error("Escalated")