import numpy as np
from pydantic import BaseModel

# Input Data Schema (for type hinting and validation)
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Iris Species Mapping
# 0: Iris Setosa
# 1: Iris Versicolor
# 2: Iris Virginica

def predict_species(features: IrisFeatures) -> int:
    """
    Iris features를 기반으로 종(species)을 예측합니다.
    실제 ML 모델 대신 간단한 규칙 기반 로직을 사용합니다 (예시).
    """
    
    # 데이터를 numpy 배열로 변환
    X = np.array([
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ])

    # 간단한 Decision Tree/Rule-based Logic (Iris Dataset 특성 반영)
    if X[2] < 2.0:  # Petal Length < 2.0 (Strong indicator for Setosa)
        prediction = 0  # Iris Setosa
    elif X[3] < 1.7 and X[2] < 5.0: # Petal Width < 1.7 and Petal Length < 5.0 
        prediction = 1  # Iris Versicolor
    else:
        prediction = 2  # Iris Virginica

    return prediction

# Prediction Result Schema
class PredictionResult(BaseModel):
    prediction: int # 0, 1, or 2