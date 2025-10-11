# api.py
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.datasets import load_iris
import numpy as np

# --- 모델 로드 및 설정 ---
try:
    with open("iris_model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    print("❌ 오류: 'iris_model.pkl' 파일을 찾을 수 없습니다. train_model.py를 먼저 실행하세요.")
    model = None

iris_names = load_iris().target_names  # 품종 이름

app = FastAPI(title="Iris Prediction API")

class IrisFeatures(BaseModel):
    sepal_length: float  # 소문자 + 언더스코어로 통일
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict/")
def predict_iris(features: IrisFeatures):
    if model is None:
        return {"error": "모델 로드 실패"}
    
    # 입력 데이터
    data_in = [[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]]
    
    prediction = model.predict(data_in)[0]
    proba = model.predict_proba(data_in)[0]
    
    return {
        "species": iris_names[prediction],
        "confidence": float(np.max(proba))  # JSON 직렬화를 위해 float 변환
    }

# 실행 명령어: uvicorn api:app --reload --port 8000