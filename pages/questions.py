import streamlit as st

def show():
    step = st.session_state.get("step", 1)
    questions = [
        ("Q1. 朝の過ごし方は？", ["すぐ行動する", "ゆっくりコーヒーを飲む", "読書から始める"], "q1", 3),
        ("Q2. コーヒーの味の好みは？", ["フルーティー", "バランスが良い", "しっかり苦味"], "q2", 4),
        ("Q3. コーヒーを飲むシチュエーションは？", ["朝食と一緒に", "仕事中", "リラックスタイム"], "q3", 5),
        ("Q4. 甘いものと一緒に飲む？", ["はい", "いいえ"], "q4", 6)
    ]

    for q_text, options, key, next_step in questions:
        if step == next_step - 1:
            ask_question(q_text, options, key, next_step)
            break

def ask_question(question_text, options, key, next_step):
    st.markdown(f'<p class="subheader">{question_text}</p>', unsafe_allow_html=True)

    # ✅ ここで "answers" の存在をチェックしてから代入
    if "answers" not in st.session_state:
        st.session_state["answers"] = {}

    st.session_state["answers"][key] = st.radio("", options, key=key)
    st.button("次へ", on_click=lambda: set_step(next_step))

def set_step(step):
    st.session_state["step"] = step
