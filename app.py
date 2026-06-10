        elif st.session_state.page == "projects":
            st.title("Projects")

            st.markdown("""
            <style>
            .project-card {
                background-color: #f4f4f4;
                padding: 18px;
                margin-bottom: 25px;
                border-radius: 2px;
            }
            .project-title {
                font-size: 22px;
                font-weight: 700;
                margin-top: 10px;
            }
            .project-info {
                font-size: 14px;
                color: #666;
            }
            </style>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            with col1:
                st.image("https://images.unsplash.com/photo-1486406146926-c627a92ad1ab", use_container_width=True)
                st.markdown("""
                <div class="project-card">
                    <div class="project-title">The Delta, Yongsan</div>
                    <div class="project-info">Graduation Project · 2026</div>
                    <p>Data Center + Public Architecture</p>
                </div>
                """, unsafe_allow_html=True)

                if st.button("View The Delta"):
                    go("project_delta")
                    st.rerun()

            with col2:
                st.image("https://images.unsplash.com/photo-1494526585095-c41746248156", use_container_width=True)
                st.markdown("""
                <div class="project-card">
                    <div class="project-title">Hybrid Timber System</div>
                    <div class="project-info">Architecture Studio · 2025</div>
                    <p>Hybrid timber structure and architectural system.</p>
                </div>
                """, unsafe_allow_html=True)

                if st.button("View Timber Project"):
                    go("project_timber")
                    st.rerun()
