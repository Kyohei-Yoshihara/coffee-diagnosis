import streamlit as st

def apply_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Roboto:wght@400&display=swap');
        .stApp {
            background-color: #FAF3E0;
            font-family: 'Roboto', sans-serif;
            color: #3E2723;
            padding: 20px;
        }
        .title {
            font-size: 60px !important;
            font-weight: bold !important;
            font-family: 'Playfair Display', serif;
            color: #5D4037;
            text-align: center;
            padding: 20px;
        }
        .question-box {
            background-color: rgba(255, 248, 220, 0.9);
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
            text-align: center;
            font-size: 18px;
        }
        .button {
            background-color: #795548 !important;
            color: white !important;
            font-size: 18px !important;
            border-radius: 8px !important;
            padding: 10px 20px !important;
            margin-top: 10px;
        }
        </style>
    """, unsafe_allow_html=True)
