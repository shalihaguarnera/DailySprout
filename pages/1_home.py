import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run_home():

    st.set_page_config(page_title = "DailySprout", page_icon = "🌱")

    st.title("🌱 Welcome to DailySprout!")
    st.write("Let's get started. Go to Sprout Log to begin logging your day.")

    col1, col2, col3 = st.columns(3, vertical_alignment = "bottom")
    with col1:
        if st.button("Sprout Log", use_container_width = True):
            st.switch_page("pages/2_log.py")
    with col2:
        if st.button("Report", use_container_width = True):
            st.switch_page("pages/3_report.py")
    with col3:
        if st.button("Calendar", use_container_width = True):
            st.switch_page("pages/4_calendar.py")

run_home()
