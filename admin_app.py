import streamlit as st
from utils.db_utils import init_db
from admin.auth import admin_auth_page
from admin.dashboard import admin_dashboard

st.set_page_config(page_title="Admin Panel", layout="wide")

# Initialize database
init_db()

st.title("🔐 Admin Panel")

# Session state for login
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

# ---------------- Logic ----------------
if not st.session_state.admin_logged_in:
    admin_auth_page()
else:
    admin_dashboard()

    # Logout button
    if st.button("Logout"):
        st.session_state.admin_logged_in = False
        st.rerun()