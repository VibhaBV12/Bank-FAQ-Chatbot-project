
## user_chat_page.py
import streamlit as st
from utils.faiss_utils import load_index, query
from utils.db_utils import save_question

def user_chat_page():
    

    # Initialize chat messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Load FAQ database (list of lines)
    db = load_index()
    if not db:
        st.warning("⚠️ FAQ file is empty or not found. Admin may need to upload FAQ.")
        return

    # Display chat history
    for role, msg in st.session_state.messages:
        if role == "user":
            st.markdown(f"**You:** {msg}")
        else:
            st.markdown(f"**Bot:** {msg}")

    # ----------------- User input via form -----------------
    with st.form(key="question_form", clear_on_submit=True):
        user_input = st.text_input("Type your question...")
        submit_button = st.form_submit_button("Ask")

    if submit_button and user_input:
        # Add user message to chat
        st.session_state.messages.append(("user", user_input))

        # Get answer using local keyword search
        try:
            answer = query(db, user_input)
        except Exception as e:
            answer = "⚠️ Error generating answer."
            st.error(str(e))

        # Add bot response to chat
        st.session_state.messages.append(("bot", answer))

        # Save user question (optional)
        try:
            save_question(user_input)
        except:
            pass