import streamlit as st

# ページ設定
st.set_page_config(page_title="コーヒー診断ツール", page_icon="☕")

# セッション状態の初期化
if "step" not in st.session_state:
    st.session_state["step"] = 1

# ユーザーの回答を保存
if "answers" not in st.session_state:
    st.session_state["answers"] = {}

# ステップ管理（1:トップ, 2:質問1, 3:質問2, 4:結果）
def next_step():
    st.session_state["step"] += 1

def reset_quiz():
    st.session_state["step"] = 1
    st.session_state["answers"] = {}

# **1️⃣ トップページ**
if st.session_state["step"] == 1:
    st.title("☕ あなたにぴったりのコーヒー診断")
    st.write("数秒でできる！あなたに最適なコーヒーを診断します。")
    st.button("診断をスタート！", on_click=next_step)

# **2️⃣ 質問1：ライフスタイル診断（産地診断）**
elif st.session_state["step"] == 2:
    st.subheader("Q1. 朝の過ごし方は？")
    q1 = st.radio("", ["すぐ行動する", "ゆっくりコーヒーを飲む", "読書から始める"])
    
    st.session_state["answers"]["q1"] = q1
    st.button("次へ", on_click=next_step)

# **3️⃣ 質問2：味の好み診断（焙煎度診断）**
elif st.session_state["step"] == 3:
    st.subheader("Q2. コーヒーの味の好みは？")
    q2 = st.radio("", ["フルーティー", "バランスが良い", "しっかり苦味"])
    
    st.session_state["answers"]["q2"] = q2
    st.button("診断結果を見る", on_click=next_step)

# **4️⃣ 診断結果ページ**
elif st.session_state["step"] == 4:
    st.subheader("🎉 診断結果！")

    # ユーザーの回答を取得
    q1 = st.session_state["answers"].get("q1", "")
    q2 = st.session_state["answers"].get("q2", "")

    # 診断ロジック
    if q1 == "すぐ行動する" and q2 == "フルーティー":
        coffee = "エチオピア 浅煎り ☕"
        desc = "フルーティーな香りが特徴で、すっきりとした味わい。"
    elif q1 == "ゆっくりコーヒーを飲む" and q2 == "バランスが良い":
        coffee = "コロンビア 中煎り ☕"
        desc = "バランスの取れたコクと甘み。飲みやすく万人向け。"
    else:
        coffee = "マンデリン 深煎り ☕"
        desc = "濃厚でスモーキーな苦味が特徴。しっかりした味わい。"

    st.write(f"あなたにおすすめのコーヒーは **{coffee}** です！")
    st.write(desc)

    # Twitterシェアボタン
    tweet_text = f"私は【{coffee}】タイプでした！☕✨ あなたも診断してみよう！"
    tweet_url = f"https://twitter.com/intent/tweet?text={tweet_text}&url=https://your-diagnosis-url.com"
    st.markdown(f"[📢 結果をTwitterでシェア]({tweet_url})", unsafe_allow_html=True)

    st.button("もう一度診断する", on_click=reset_quiz)
