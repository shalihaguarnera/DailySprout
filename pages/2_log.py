from datetime import datetime
import calendar
import time
import streamlit as st
import data

# Defining helper functions
def hide_buttons():
    st.markdown(
        """
        <style>
        button[data-testid="stBaseButton-secondary"] {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def chat_stream(response):
    response = f"{response}"
    for char in response:
        yield char
        time.sleep(.02)

def append_history(role, content) -> None:
    st.session_state.history.append({"role": role, "content": content})

def disable_chat():
    st.session_state.chat_hidden = True

# Defining variables
if "response_options" not in st.session_state:
    st.session_state["response_options"] = {
        "day_rating": ["Terrible", "Bad", "Ok", "Good", "Great"],
        "activities": ["Work", "School", "Exercise", "Study", "Relax"],
        "people": ["Friends", "Colleagues", "Family"]
    }

current_date = datetime.now().date()
current_month = current_date.strftime('%B')
current_weekday = calendar.day_name[current_date.weekday()]

# Adding page title, header, and divider
st.set_page_config(page_title = "Sprout Log", page_icon = "✏️")
st.title(f"{current_weekday}, {current_month} {current_date.day}, {current_date.year}")
st.divider()

# Initialize session state for chat messages
if "history" not in st.session_state:
    st.session_state.history = []

for i, message in enumerate(st.session_state.history):
    with st.chat_message(message["role"]):
        st.write(message["content"])

if "chat_hidden" not in st.session_state:
    st.session_state.chat_hidden = False

if "asked_name" not in st.session_state:
    st.session_state.asked_name = False

if "asked_rating" not in st.session_state:
    st.session_state.asked_rating = False

if "user_info" not in st.session_state:
    st.session_state.user_info = "Shaliha"

if not st.session_state.user_info:
    if not st.session_state.asked_name:
        with st.chat_message("assistant"):
            response = st.write_stream(chat_stream("Welcome! It looks like you're new here. What is your name?"))
        st.session_state.asked_name = True
        append_history("assistant", response)
    user_input = st.chat_input("Say something", disabled = st.session_state.chat_hidden, on_submit = disable_chat)
    
    if user_input:
        st.session_state.user_info = user_input
        data.user_info["name"] = user_input
        with st.chat_message("user"):
            st.write(user_input)
        append_history("user", user_input)
        with st.chat_message("assistant"):
            response = st.write_stream(chat_stream(f"It's great to meet you {user_input}. Let's begin logging your day."))
        append_history("assistant", response)
        st.session_state.chat_hidden = False
        st.rerun()

if not st.session_state.asked_rating:
    with st.chat_message("assistant"):
        response = st.write_stream(chat_stream("How are you feeling today?"))
    append_history("assistant", response)

    rating_container = st.container()
    with rating_container:
        col1, col2, col3, col4, col5 = st.columns(5, vertical_alignment = "bottom")
        columns = [col1, col2, col3, col4, col5]
        for index, rating in enumerate(st.session_state.response_options["day_rating"]):
            with columns[index]:
                if st.button(rating, key=f"rating_option_{index}", use_container_width = True):
                    hide_buttons()
                    with st.chat_message("user"):
                        st.write(st.session_state.response_options.day_rating[index])
                    st.session_state.chat_messages.append({"role": "user", "content": rating})

    st.session_state.asked_rating = True

    