from pathlib import Path
import streamlit as st

dir_path = Path(__file__).parent

# Note that this needs to be in a method so we can have an e2e playwright test.
def run() -> None:
    page = st.navigation(
        {
            "🌱 DailySprout": [
                st.Page(
                    dir_path / "pages/1_home.py",
                    title = "Home",
                    icon = "🏡"
                ),
                st.Page(
                    dir_path / "pages/2_log.py",
                    title = "Sprout Log",
                    icon = "📝",
                ),
                st.Page(
                    dir_path / "pages/3_report.py",
                    title = "Report",
                    icon = "📊",
                ),
                st.Page(
                    dir_path / "pages/4_calendar.py",
                    title = "Calendar",
                    icon = "📅",
                ),
            ]
        }
    )
    page.run()

if __name__ == "__main__":
    run()
