# 1. Pythonの公式イメージ（Python 3.9）を使用
FROM python:3.9

# 2. 作業ディレクトリを設定
WORKDIR /app

# 3. 依存パッケージをインストール（pipを最新化しておく）
RUN pip install --upgrade pip
RUN pip install streamlit

# 4. コンテナ起動時にStreamlitを実行
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]