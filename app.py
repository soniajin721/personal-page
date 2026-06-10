import streamlit as st

st.set_page_config(
    page_title="Moon Jungho Portfolio",
    layout="wide"
)

# ---------------------------
# 페이지 상태 관리
# ---------------------------

if "page" not in st.session_state:
    st.session_state.page = "cover"

def go(page):
    st.session_state.page = page

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
            <h1>MOON JUNGHO</h1>
            <h3>Architecture Portfolio</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    c1, c2, c3 = st.columns([3,1,3])

    with c2:
        if st.button("ENTER", use_container_width=True):
            go("about")
            st.rerun()

# ---------------------------
# MAIN PAGE
# ---------------------------

else:

    menu, content = st.columns([1, 2])

    # -----------------------
    # LEFT MENU
    # -----------------------

    with menu:

        st.markdown(
            """
            # MOON  
            # JUNGHO
            """
        )

        st.divider()

        if st.button("개인정보", use_container_width=True):
            go("about")
            st.rerun()

        if st.button("프로젝트", use_container_width=True):
            go("projects")
            st.rerun()

        if st.button("컨택", use_container_width=True):
            go("contact")
            st.rerun()

    # -----------------------
    # RIGHT CONTENT
    # -----------------------

    with content:

        # ABOUT

        if st.session_state.page == "about":

            st.title("About Me")

            st.image(
                "https://images.unsplash.com/photo-1500648767791-00dcc994a43e",
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

            이곳에 자기소개를 자유롭게 작성하면 됩니다.
            """)

        # PROJECTS

        elif st.session_state.page == "projects":

            st.title("Projects")

            st.markdown("""
            <style>
            .project-title{
                font-size:22px;
                font-weight:700;
                margin-top:10px;
            }

            .project-info{
                color:#777777;
                font-size:14px;
            }
            </style>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            # 프로젝트 1

            with col1:

                st.image(
                    "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab",
                    use_container_width=True
                )

                st.markdown(
                    """
                    <div class="project-title">
                    The Delta, Yongsan
                    </div>

                    <div class="project-info">
                    Graduation Project · 2026
                    </div>

                    Data Center + Public Architecture
                    """,
                    unsafe_allow_html=True
                )

                if st.button("View Project 1"):
                    go("project_delta")
                    st.rerun()

            # 프로젝트 2

            with col2:

                st.image(
                    "https://images.unsplash.com/photo-1494526585095-c41746248156",
                    use_container_width=True
                )

                st.markdown(
                    """
                    <div class="project-title">
                    Hybrid Timber System
                    </div>

                    <div class="project-info">
                    Architecture Studio · 2025
                    </div>

                    Hybrid Timber Structure
                    """,
                    unsafe_allow_html=True
                )

                if st.button("View Project 2"):
                    go("project_timber")
                    st.rerun()

        # CONTACT

        elif st.session_state.page == "contact":

            st.title("Contact")

            st.write("### Email")
            st.write("haqunamatatajh0905@gmail.com")

            st.write("### Instagram")
            st.write("@your_instagram")

            st.write("### LinkedIn")
            st.write("your_linkedin")

        # PROJECT DETAIL 1

        elif st.session_state.page == "project_delta":

            st.title("The Delta, Yongsan")

            st.image(
                "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab",
                use_container_width=True
            )

            st.write("""
            ## Project Overview

            여기에 프로젝트 설명 작성

            - Site
            - Program
            - Concept
            - Strategy
            """)

            if st.button("← Back to Projects"):
                go("projects")
                st.rerun()

        # PROJECT DETAIL 2

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

            if st.button("← Back to Projects"):
                go("projects")
                st.rerun()
