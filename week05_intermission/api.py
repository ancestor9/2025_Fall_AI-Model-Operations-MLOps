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

iris_names = load_iris().target_names # 품종 이름

app = FastAPI(title="Iris Prediction API")

class IrisFeatures(BaseModel):
    sl: float # Sepal Length
    sw: float # Sepal Width
    pl: float # Petal Length
    pw: float # Petal Width    

@app.post("/predict/")
def predict_iris(features: IrisFeatures):
    if model is None:
        return {"error": "모델 로드 실패"}
    
    # 입력 데이터 [sl, sw, pl, pw]
    data_in = [[features.sl, features.sw, features.pl, features.pw]]
    
    prediction = model.predict(data_in)[0]
    proba = model.predict_proba(data_in)[0]
    
    return {
        "species": iris_names[prediction],
        "confidence": np.max(proba)
    }

# 실행 명령어: uvicorn api:app --reload --port 8000