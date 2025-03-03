import streamlit as st

def apply_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Roboto:wght@400&display=swap');
        
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #FAF3E0 !important;
            font-family: 'Roboto', sans-serif !important;
            color: #3E2723 !important;
        }
        .title {
            font-size: 60px !important;
            font-weight: bold !important;
            font-family: 'Playfair Display', serif !important;
            color: #5D4037 !important;
            text-align: center;
            padding: 20px;
        }
        .question-box {
            background-color: rgba(255, 248, 220, 0.9) !important;
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