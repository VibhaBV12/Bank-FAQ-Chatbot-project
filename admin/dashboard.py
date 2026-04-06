
import streamlit as st
import pandas as pd
import sqlite3
import os
from utils.faiss_utils import create_index
from constants import FAQ_PATH, INDEX_PATH

def admin_dashboard():
    st.title("Admin Dashboard")

    # --- Upload FAQ file ---
    file = st.file_uploader("Upload FAQ file")
    if file:
        # Ensure data folder exists
        os.makedirs(os.path.dirname(FAQ_PATH), exist_ok=True)

        # Save uploaded file
        with open(FAQ_PATH, "wb") as f:
            f.write(file.read())
        st.success("Uploaded FAQ file")

        # Automatically rebuild FAISS index after upload
        create_index()
        st.success("FAISS Index rebuilt")

    # --- Optional: Manual rebuild button ---
    if st.button("Rebuild FAISS Index"):
        create_index()
        st.success("FAISS Index rebuilt")

    # --- Show user questions from database ---
    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect("database/bank.db")

    try:
        df = pd.read_sql("SELECT * FROM questions", conn)
    except:
        df = pd.DataFrame()
    finally:
        conn.close()

    st.subheader("User Questions")
    st.dataframe(df)
