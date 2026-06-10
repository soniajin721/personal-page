import streamlit as st

st.set_page_config(
    page_title="Moon Jungho Portfolio",
    layout="wide"
)

if "page" not in st.session_state:
    st.session_state.page = "cover"

def go(page):
    st.session_state.page = page

if st.session_state.page == "cover":
    st.image(
        "https://images.unsplash.com/photo-1511818966892-d7d671e672a2",
        use_container_width=True
    )

    st.markdown(
        """
        <div style="text-align:center;">
            <h1>MOON JUNGHO</h1>
            <h3>Architecture Portfolio</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("ENTER"):
        go("about")
        st.rerun()

else:
    menu, content = st.columns([1, 2])

    with menu:
        st.markdown("# MOON<br>JUNGHO", unsafe_allow_html=True)
        st.write("")

        if st.button("개인정보"):
            go("about")
            st.rerun()

        if st.button("프로젝트"):
            go("projects")
            st.rerun()

        if st.button("컨택"):
            go("contact")
            st.rerun()

    with content:
        if st.session_state.page == "about":
            st.title("About Me")
            st.write("""
            여기에 개인정보/자기소개를 작성하면 돼.

            - 이름: 문정호
            - 전공: 건축학
            - 관심 분야: 건축 설계, 도시, 데이터센터, 공공건축
            """)

        elif st.session_state.page == "projects":
            st.title("Projects")

            col1, col2 = st.columns(2)

            with col1:
                st.image("https://images.unsplash.com/photo-1486406146926-c627a92ad1ab", use_container_width=True)
                st.markdown("### The Delta, Yongsan")
                st.write("Data Center + Public Architecture")
                if st.button("View Project 1"):
                    go("project_delta")
                    st.rerun()

            with col2:
                st.image("https://images.unsplash.com/photo-1494526585095-c41746248156", use_container_width=True)
                st.markdown("### Hybrid Timber System")
                st.write("Architecture Studio Project")
                if st.button("View Project 2"):
                    go("project_timber")
                    st.rerun()

        elif st.session_state.page == "contact":
            st.title("Contact")
            st.write("Email: haqunamatatajh0905@gmail.com")
            st.write("Instagram: @your_instagram")

        elif st.session_state.page == "project_delta":
            st.title("The Delta, Yongsan")
            st.image("https://images.unsplash.com/photo-1486406146926-c627a92ad1ab", use_container_width=True)
            st.write("""
            여기에 프로젝트 설명을 작성하면 돼.

            - Site
            - Concept
            - Program
            - Design Strategy
            """)

        elif st.session_state.page == "project_timber":
            st.title("Hybrid Timber System")
            st.image("https://images.unsplash.com/photo-1494526585095-c41746248156", use_container_width=True)
            st.write("""
            여기에 프로젝트 설명을 작성하면 돼.
            """)
