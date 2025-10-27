from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import os

# Model Logic Import
from model.predictor import IrisFeatures, PredictionResult, predict_species

# --- Configuration ---
app = FastAPI(title="IRIS Species Predictor API")

# Setup for Templates (View)
# 'view' 디렉토리에서 HTML 파일을 찾도록 설정
templates = Jinja2Templates(directory="view")

# Setup for Static Files (Images)
# 'static' 디렉토리를 '/static' URL 경로로 서빙하도록 설정 (이미지 경로)
app.mount("/static", StaticFiles(directory="static"), name="static")

# --- Routes (Controller Logic) ---

@app.get("/", summary="Home Page")
async def home(request: Request):
    """
    Root 경로 요청을 처리하고, View/index.html 파일을 반환합니다.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_model=PredictionResult, summary="Predict Iris Species")
async def predict(features: IrisFeatures):
    """
    POST 요청으로 받은 IRIS 데이터를 사용하여 모델 예측을 수행합니다.
    """
    # 1. Input Validation: Pydantic handles this automatically via IrisFeatures type hint
    
    # 2. Business Logic (Model 호출)
    predicted_index = predict_species(features)
    
    # 3. Response Generation
    return PredictionResult(prediction=predicted_index)

# --- Server Execution ---
# uvicorn main:app --reload

# NOTE: 실제 운영 환경에서는 uvicorn을 사용하여 실행해야 합니다.
# 터미널에서 'uvicorn main:app --reload' 명령어로 실행합니다.