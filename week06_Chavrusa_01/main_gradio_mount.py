# main_gradio_mounted.py

import pickle
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.datasets import load_iris
import gradio as gr
import uvicorn  # Added for running the FastAPI server

# --- 1. 모델 로드 ---
MODEL_FILENAME = "iris_model.pkl"
try:
    with open(MODEL_FILENAME, "rb") as f:
        model = pickle.load(f)
    print(f"✅ 모델 로드 완료")
except FileNotFoundError:
    print(f"❌ '{MODEL_FILENAME}' 파일을 찾을 수 없습니다. 모델 파일이 올바른 경로에 있는지 확인하세요.")
    model = None
except Exception as e:
    print(f"❌ 모델 로드 중 오류 발생: {str(e)}")
    model = None

iris_names = load_iris().target_names

# --- 2. FastAPI 앱 ---
app = FastAPI()

class IrisFeatures(BaseModel):
    sl: float
    sw: float
    pl: float
    pw: float

# --- 3. 예측 함수 ---
def get_prediction(sl: float, sw: float, pl: float, pw: float):
    if model is None:
        return {"error": "모델 로드 실패"}
    
    data_in = [[sl, sw, pl, pw]]
    prediction = model.predict(data_in)[0]
    proba = model.predict_proba(data_in)[0]
    
    return {
        "species": iris_names[prediction],
        "confidence": float(np.max(proba))
    }

# --- 4. API 엔드포인트 ---
@app.post("/api/predict")
def predict_api(features: IrisFeatures):
    return get_prediction(features.sl, features.sw, features.pl, features.pw)

# --- 5. Gradio 함수 ---
def predict_ui(sl, sw, pl, pw):
    result = get_prediction(sl, sw, pl, pw)
    
    if "error" in result:
        return f"❌ {result['error']}"
    
    species = result["species"].capitalize()
    confidence = result["confidence"] * 100
    
    return f"✅ 예측 품종: {species}\n(확신도: {confidence:.2f}%)"

# --- 6. Gradio 인터페이스 ---
with gr.Blocks(title="붓꽃 예측") as demo:
    gr.Markdown("# 🌸 붓꽃 품종 예측 서비스")
    gr.Markdown("슬라이더를 조절하여 붓꽃의 크기를 입력하세요")
    
    with gr.Row():
        with gr.Column():
            sl = gr.Slider(4.0, 8.0, step=0.1, value=5.1, label="꽃받침 길이 (cm)")
            sw = gr.Slider(2.0, 4.5, step=0.1, value=3.5, label="꽃받침 너비 (cm)")
            pl = gr.Slider(1.0, 7.0, step=0.1, value=1.4, label="꽃잎 길이 (cm)")
            pw = gr.Slider(0.1, 2.5, step=0.1, value=0.2, label="꽃잎 너비 (cm)")
            btn = gr.Button("예측하기", variant="primary")
        
        with gr.Column():
            output = gr.Textbox(label="예측 결과", lines=3)
    
    gr.Examples(
        examples=[
            [5.1, 3.5, 1.4, 0.2],
            [6.7, 3.0, 5.2, 2.3],
            [5.9, 3.0, 4.2, 1.5],
        ],
        inputs=[sl, sw, pl, pw],
    )
    
    btn.click(fn=predict_ui, inputs=[sl, sw, pl, pw], outputs=output)

# --- 7. Gradio 마운트 ---
app = gr.mount_gradio_app(app, demo, path="/gradio")

# --- 8. 서버 실행 ---
if __name__ == "__main__":
    print("\n" + "="*60)
    print("🚀 서버 시작!")
    print("="*60)
    print("📍 Gradio UI:      http://127.0.0.1:8000/gradio")
    print("📍 API Docs:       http://127.0.0.1:8000/docs")
    print("📍 API Endpoint:   http://127.0.0.1:8000/api/predict")
    print("="*60 + "\n")
    
    # Run the FastAPI server with uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# 💡 참고: '/' 경로를 Gradio로 리디렉션하여 바로 UI를 볼 수도 있습니다.
# from fastapi.responses import RedirectResponse
# @app.get("/")
# def redirect_to_gradio():
#     return RedirectResponse(url="/gradio")