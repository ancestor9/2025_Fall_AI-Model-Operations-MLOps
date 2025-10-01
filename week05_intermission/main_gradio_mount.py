# main_mounted.py

import pickle
import numpy as np
import requests
import json
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.datasets import load_iris
import gradio as gr
from gradio.routes import mount_gradio_app # 💡 Gradio Mount 함수 임포트

# --- 1. 모델 로드 및 설정 ---
MODEL_FILENAME = "iris_model.pkl"
try:
    with open(MODEL_FILENAME, "rb") as f:
        model = pickle.load(f)
    print(f"✅ 모델 '{MODEL_FILENAME}' 로드 완료.")
except FileNotFoundError:
    print(f"❌ 치명적 오류: '{MODEL_FILENAME}' 파일을 찾을 수 없습니다. train_model.py를 먼저 실행하세요.")
    model = None

iris_names = load_iris().target_names # 품종 이름

# --- 2. FastAPI 설정 ---
app = FastAPI(title="FastAPI + Gradio Mounted Service")

class IrisFeatures(BaseModel):
    sl: float
    sw: float
    pl: float
    pw: float

# --- 3. FastAPI API 엔드포인트 ---
# Gradio가 호출할 백엔드 API (FastAPI의 핵심 기능)
@app.post("/api/predict")
def predict_iris_api(features: IrisFeatures):
    if model is None:
        return {"error": "모델 로드 실패"}
    
    data_in = [[features.sl, features.sw, features.pl, features.pw]]
    
    prediction = model.predict(data_in)[0]
    proba = model.predict_proba(data_in)[0]
    
    return {
        "species": iris_names[prediction],
        "confidence": np.max(proba)
    }

# --- 4. Gradio 프론트엔드 함수 ---
# Gradio 인터페이스에서 실행될 함수. FastAPI 엔드포인트를 호출하도록 구현합니다.
API_URL = "http://127.0.0.1:8000/api/predict" # 💡 FastAPI가 실행될 주소/포트와 일치해야 합니다.

def predict_species_ui(sl, sw, pl, pw):
    payload = {"sl": sl, "sw": sw, "pl": pl, "pw": pw}
    
    try:
        # 자기 자신(FastAPI)의 API를 호출
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()

        result = response.json()
        
        species = result["species"].capitalize()
        confidence = result["confidence"] * 100
        
        return f"✅ 예측 품종: {species}\n(확신도: {confidence:.2f}%)"
        
    except Exception as e:
        return f"❌ 예측 오류: {e}"

# --- 5. Gradio 인터페이스 정의 ---
iface = gr.Interface(
    fn=predict_species_ui,
    inputs=[
        gr.Slider(4.0, 8.0, 0.1, value=5.1, label="꽃받침 길이 (SL)"),
        gr.Slider(2.0, 4.5, 0.1, value=3.5, label="꽃받침 너비 (SW)"),
        gr.Slider(1.0, 7.0, 0.1, value=1.4, label="꽃잎 길이 (PL)"),
        gr.Slider(0.1, 2.5, 0.1, value=0.2, label="꽃잎 너비 (PW)"),
    ],
    outputs=gr.Textbox(label="예측 결과", lines=3),
    title="Iris 예측 서비스 (FastAPI + Gradio Mount)",
)

#### 실행 방법 안내 ####
'''
Gradio UI 접속: http://127.0.0.1:8000/gradio

FastAPI API (직접 호출): http://127.0.0.1:8000/api/predict (POST 요청)

'''

# --- 6. Gradio 앱을 FastAPI에 마운트 ---
# Gradio 인터페이스를 '/gradio' 경로에 통합합니다.
# 이제 FastAPI 앱이 Gradio 앱을 포함하게 됩니다.
app = mount_gradio_app(app, iface, path="/gradio")

# 💡 참고: '/' 경로를 Gradio로 리디렉션하여 바로 UI를 볼 수도 있습니다.
# from fastapi.responses import RedirectResponse
# @app.get("/")
# def redirect_to_gradio():
#     return RedirectResponse(url="/gradio")