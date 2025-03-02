import streamlit as st
from pages import home, questions, results
from components import styles

# ページ設定
st.set_page_config(page_title="コーヒー診断ツール", page_icon="☕")

# カスタムCSS適用
styles.apply_css()

# セッション状態の初期化
def init_session():
    if "step" not in st.session_state:
        st.session_state["step"] = 1
    if "answers" not in st.session_state:  # ✅ answers を初期化
        st.session_state["answers"] = {}

init_session()  # ✅ セッションの初期化を実行

# ページ遷移の管理
def navigate():
    step = st.session_state["step"]
    if step == 1:
        home.show()
    elif step in [2, 3, 4, 5]:
        questions.show()
    elif step == 6:
        results.show()

navigate()
