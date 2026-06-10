import streamlit as st

st.set_page_config(
    page_title="Moon Jungho Portfolio",
    layout="wide"
)

if "page" not in st.session_state:
    st.session_state.page = "cover"

def go(page):
    st.session_state.page = page

# 전체 디자인 CSS
st.markdown("""
<style>
/* 전체 여백 */
.block-container {
    padding-top: 2rem;
}

/* 로고 버튼을 글자처럼 보이게 */
button[kind="primary"] {
    background: transparent !important;
    color: #31333F !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    text-align: left !important;
    font-size: 52px !important;
    font-weight: 800 !important;
    line-height: 1.1 !important;
}

button[kind="primary"]:hover {
    color: #777777 !important;
    background: transparent !important;
}

/* 일반 메뉴 버튼 */
button[kind="secondary"] {
    border-radius: 0px !important;
    border: 1px solid #dddddd !important;
    background: white !important;
    color: #222222 !important;
}

button[kind="secondary"]:hover {
    border: 1px solid #222222 !important;
    color: #000000 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# COVER PAGE
# ---------------------------

if st.session_state.page == "cover":

    st.image(
        "https://images.unsplash.com/photo-1511818966892-d7d671e672a2",
        use_container_width=True
    )

    st.markdown(
        """
        <div style="text-align:center; padding-top:20px;">
            <h1 style="font-size:54px;">MOON JUNGHO</h1>
            <h3>Architecture Portfolio</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    c1, c2, c3 = st.columns([3, 1, 3])

    with c2:
        if st.button("ENTER", use_container_width=True, type="secondary"):
            go("about")
            st.rerun()

# ---------------------------
# MAIN PAGE
# ---------------------------

else:

    menu, content = st.columns([1, 2])

    # LEFT MENU
    with menu:

        if st.button("MOON\nJUNGHO", type="primary"):
            go("cover")
            st.rerun()

        st.divider()

        if st.button("개인정보", use_container_width=True, type="secondary"):
            go("about")
            st.rerun()

        if st.button("프로젝트", use_container_width=True, type="secondary"):
            go("projects")
            st.rerun()

        if st.button("컨택", use_container_width=True, type="secondary"):
            go("contact")
            st.rerun()

    # RIGHT CONTENT
    with content:

        if st.session_state.page == "about":

            st.title("About Me")

            st.image(
                "images/증명사진.jpg",
                width=300
            )

            st.write("""
            ### 문정호

            명지대학교 건축학과

            관심 분야  
            - Architecture  
            - Urban Design  
            - Data Center  
            - Public Space  

            명지대에서 건축을 전공하고 있습니다. 
            다양한 분야에 관심이 많습니다.
            """)

        elif st.session_state.page == "projects":

            st.title("Projects")

            col1, col2 = st.columns(2)

            with col1:
                st.image(
                    "images/데이터센터.png",
                    use_container_width=True
                )
                st.markdown("""
                ### 데이터센터in용산
                Graduation Project · 2026  
                Data Center + Public Architecture
                """)
                if st.button("View Project 1", type="secondary"):
                    go("데이터센터in용산")
                    st.rerun()

            with col2:
                st.image(
                    "https://images.unsplash.com/photo-1494526585095-c41746248156",
                    use_container_width=True
                )
                st.markdown("""
                ### 24시간
                Architecture Studio · 2025  
                Hybrid Timber Structure
                """)
                if st.button("View Project 2", type="secondary"):
                    go("project_timber")
                    st.rerun()

        elif st.session_state.page == "contact":

            st.title("Contact")

            st.write("### Email")
            st.write("haqunamatatajh0905@gmail.com")

            st.write("### Instagram")
            st.write("@your_instagram")

            st.write("### LinkedIn")
            st.write("your_linkedin")

        elif st.session_state.page == "데이터센터in용산":

            st.title("데이터센터in용산")

            st.image(
                "images/데이터센터.png",
                use_container_width=True
            )

            st.write("""
            ## Project Overview

            여기에 프로젝트 설명 작성

            - Site 용산
            - Program 데이터센터
            - Concept 도심형 데이터센터
            - Strategy
            """)

            if st.button("← Back to Projects", type="secondary"):
                go("projects")
                st.rerun()

        elif st.session_state.page == "project_timber":

            st.title("Hybrid Timber System")

            st.image(
                "https://images.unsplash.com/photo-1494526585095-c41746248156",
                use_container_width=True
            )

            st.write("""
            ## Project Overview

            여기에 프로젝트 설명 작성
            """)

            if st.button("← Back to Projects", type="secondary"):
                go("projects")
                st.rerun()
