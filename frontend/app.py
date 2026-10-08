import streamlit as st

st.set_page_config(
    page_title="PCB Defect Inspector",
    page_icon="🔍",
    layout="wide"
)

st.title("PCB Defect Inspector")
st.write("AI-powered PCB defect detection and diagnosis")

uploaded_file = st.file_uploader(
    "Upload PCB image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded PCB image")
    st.info("Defect detection pipeline is not implemented yet.")