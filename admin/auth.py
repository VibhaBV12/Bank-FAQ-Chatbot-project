
from utils.db_utils import add_admin, login_admin
import streamlit as st

# 🔐 Bank secret key (you decide this)
BANK_SECRET = "bank123"


def admin_auth_page():
    st.title("Admin Login/Register")

    tab1, tab2 = st.tabs(["Login", "Register"])

    # LOGIN
    with tab1:
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")

        if st.button("Login"):
            if login_admin(u, p):
                st.session_state.admin_logged_in = True
                st.success("Logged in")
                st.rerun()
            else:
                st.error("Invalid credentials")

    # REGISTER
    with tab2:
        u = st.text_input("New Username")
        p = st.text_input("New Password", type="password")
        secret = st.text_input("Bank Secret Key", type="password")

        if st.button("Register"):
            if secret == BANK_SECRET:
                add_admin(u, p)
                st.success("Registered successfully")
            else:
                st.error("Invalid Bank Secret Key ❌")