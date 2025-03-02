import streamlit as st

def show():
    st.markdown('<h2 class="title">☕ あなたにぴったりのコーヒー診断</h2>', unsafe_allow_html=True)
    st.write("コーヒーの好みに合わせたパーソナライズ診断を体験しましょう！")
    st.button("診断をスタート！", on_click=lambda: set_step(2))

def set_step(step):
    st.session_state["step"] = step