import streamlit as st

st.set_page_config(layout="wide")

menu, content = st.columns([1, 2])

with menu:
    st.markdown("# MOON<br>JUNGHO", unsafe_allow_html=True)
    st.write("")

    if st.button("개인정보"):
        st.switch_page("pages/about.py")
    if st.button("프로젝트"):
        st.switch_page("pages/projects.py")
    if st.button("컨택"):
        st.switch_page("pages/contact.py")

with content:
    st.title("Projects")

    col1, col2 = st.columns(2)

    with col1:
        st.image("https://images.unsplash.com/photo-1486406146926-c627a92ad1ab", use_container_width=True)
        st.markdown("### The Delta, Yongsan")
        st.write("Data Center + Public Architecture")
        if st.button("View Project 1"):
            st.switch_page("pages/project_delta.py")

    with col2:
        st.image("https://images.unsplash.com/photo-1494526585095-c41746248156", use_container_width=True)
        st.markdown("### Hybrid Timber System")
        st.write("Architecture Studio Project")
        if st.button("View Project 2"):
            st.switch_page("pages/project_timber.py")
