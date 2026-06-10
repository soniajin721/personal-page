import streamlit as st

st.set_page_config(layout="wide")

# 왼쪽 목차 / 오른쪽 콘텐츠
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
    st.title("About Me")

    st.write("""
    여기에 개인정보/자기소개를 작성하면 돼.

    - 이름: 문정호
    - 전공: 건축학
    - 관심 분야: 건축 설계, 도시, 데이터센터, 공공건축
    """)

    st.image(
        "https://images.unsplash.com/photo-1497366754035-f200968a6e72",
        use_container_width=True
    )
