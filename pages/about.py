import streamlit as st

st.set_page_config(layout="wide")

st.title("About Me")

st.write("여기에 자기소개를 작성하면 됩니다.")

if st.button("프로젝트"):
    st.switch_page("pages/projects.py")
