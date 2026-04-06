import streamlit as st
from utils.db_utils import init_db
from user.chat_ui import user_chat_page

st.set_page_config(page_title="Bank Chatbot", layout="wide")

# Initialize database
init_db()

# ---------------- Main Page ----------------
st.title("🏦 Bank Chatbot")
st.write("Ask your banking questions below:")

# Only user chat
user_chat_page()