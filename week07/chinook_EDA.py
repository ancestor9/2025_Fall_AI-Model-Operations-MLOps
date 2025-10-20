from fastapi import FastAPI
import gradio as gr
import sqlite3
import pandas as pd
import base64
import os
import requests

import matplotlib
matplotlib.use("Agg")   # 반드시 pyplot import 전에 호출
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image



app = FastAPI()


# ==========================================================
# 1️⃣ DB 파일 자동 다운로드 (없을 시 GitHub에서 가져옴)
# ==========================================================
DB_URL = "https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite"
DB_PATH = "chinook.db"

def download_chinook_db():
    if not os.path.exists(DB_PATH):
        print("📥 Downloading Chinook database...")
        response = requests.get(DB_URL)
        with open(DB_PATH, "wb") as f:
            f.write(response.content)
        print("✅ Download complete.")
    else:
        print("✅ Chinook DB already exists.")

download_chinook_db()


DB_PATH = "chinook.db"

# ==========================================================
# SQLite 연결 및 테이블 조회 함수
# ==========================================================

# 1️⃣ 테이블 목록 조회
def get_tables():
    with sqlite3.connect(DB_PATH) as conn:
        tables = pd.read_sql_query(
            "SELECT name FROM sqlite_master WHERE type='table';", conn
        )
    return tables["name"].tolist()


# 2️⃣ 테이블 미리보기
def preview_table(table_name):
    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT 10;", conn)
    return df


# 3️⃣ SQL 직접 실행
def run_sql(query):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        return f"❌ Error: {str(e)}"


# 4️⃣ EDA 시각화: 장르별 트랙 수
def plot_genre_distribution():
    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query("""
            SELECT g.Name AS Genre, COUNT(*) AS TrackCount
            FROM Track t
            JOIN Genre g ON t.GenreId = g.GenreId
            GROUP BY g.Name
            ORDER BY TrackCount DESC;
        """, conn)
    plt.figure(figsize=(8, 5))
    plt.bar(df["Genre"], df["TrackCount"])
    plt.xticks(rotation=75)
    plt.title("Track Count by Genre")
    plt.xlabel("Genre")
    plt.ylabel("Count")
    plt.tight_layout()
    # 이미지 변환
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    return buf


def eda_dashboard():
    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query("""
            SELECT BillingCountry, SUM(Total) AS Revenue
            FROM Invoice
            GROUP BY BillingCountry
            ORDER BY Revenue DESC;
        """, conn)
    plt.figure(figsize=(8, 5))
    plt.bar(df["BillingCountry"], df["Revenue"])
    plt.xticks(rotation=75)
    plt.title("Revenue by Country")
    plt.xlabel("Country")
    plt.ylabel("Revenue")
    plt.tight_layout()
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    return buf


# 🎨 Gradio UI 정의
def launch_gradio():
    with gr.Blocks(title="Chinook EDA Dashboard") as demo:
        gr.Markdown("## 🎵 Chinook Database EDA")
        
        with gr.Tab("1️⃣ 테이블 목록"):
            btn = gr.Button("Show Tables")
            table_output = gr.Textbox(label="Tables", interactive=False)
            btn.click(fn=lambda: ", ".join(get_tables()), outputs=table_output)
        
        with gr.Tab("2️⃣ 테이블 미리보기"):
            table_dropdown = gr.Dropdown(choices=get_tables(), label="Select Table")
            preview_btn = gr.Button("Preview")
            preview_output = gr.Dataframe(label="Preview")
            preview_btn.click(fn=preview_table, inputs=table_dropdown, outputs=preview_output)
        
        with gr.Tab("3️⃣ SQL 실행"):
            sql_input = gr.Textbox(label="Enter SQL Query", lines=5)
            sql_btn = gr.Button("Run SQL")
            sql_output = gr.Dataframe(label="Query Result")
            sql_btn.click(fn=run_sql, inputs=sql_input, outputs=sql_output)
        
        with gr.Tab("4️⃣ 기본 EDA 시각화"):
            genre_btn = gr.Button("장르별 트랙 분포")
            genre_plot = gr.Image(label="Genre Plot")
            genre_btn.click(fn=plot_genre_distribution, outputs=genre_plot)

            rev_btn = gr.Button("국가별 매출")
            rev_plot = gr.Image(label="Revenue Plot")
            rev_btn.click(fn=eda_dashboard, outputs=rev_plot)
        
    return demo


# 🏁 FastAPI + Gradio 통합 실행
@app.get("/")
def read_root():
    return {"message": "Go to /gradio for the EDA dashboard."}


@app.on_event("startup")
async def startup_event():
    import threading
    demo = launch_gradio()
    threading.Thread(target=lambda: demo.launch(server_name="127.0.0.1", server_port=7860, share=True)).start()

'''
🖥 FastAPI (포트 8000)
        │
        ├──▶ API 엔드포인트 처리 (/gradio 등)
        │
        └──▶ startup_event()
                │
                └──▶ threading.Thread → Gradio(포트 7860)
                             │
                             └── Web UI (EDA Dashboard)
'''