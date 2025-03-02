import streamlit as st
from logic.diagnosis import get_coffee_recommendation

def show():
    st.markdown('<p class="subheader">🎉 診断結果！</p>', unsafe_allow_html=True)
    q1 = st.session_state["answers"].get("q1", "")
    q2 = st.session_state["answers"].get("q2", "")
    q3 = st.session_state["answers"].get("q3", "")
    q4 = st.session_state["answers"].get("q4", "")
    
    coffee, desc = get_coffee_recommendation(q1, q2, q3, q4)
    
    st.markdown(f'<div class="question-box"><b>あなたにおすすめのコーヒーは {coffee} です！</b><br>{desc}</div>', unsafe_allow_html=True)
    st.button("もう一度診断する", on_click=lambda: set_step(1))

def set_step(step):
    st.session_state["step"] = step
