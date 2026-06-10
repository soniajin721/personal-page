import streamlit as st

st.set_page_config(
    page_title="Moon Jungho Portfolio",
    layout="wide"
)

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
    st.switch_page("pages/about.py")
