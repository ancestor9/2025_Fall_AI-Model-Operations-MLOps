import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import os

# 1. 데이터 로드 및 학습 준비
print("모델 학습을 시작합니다...")
iris = load_iris()
X, y = iris.data, iris.target
# 간단한 예제를 위해 훈련/테스트 데이터 분리
X_train, _, y_train, _ = train_test_split(X, y, random_state=42)

# 2. 모델 학습
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 3. 모델 저장 (Serialization)
MODEL_FILENAME = 'iris_model.pkl'
with open(MODEL_FILENAME, 'wb') as file:
    pickle.dump(model, file)
    
print(f"✅ Iris 모델이 '{MODEL_FILENAME}' 파일로 성공적으로 저장되었습니다.")
print(f"저장 경로: {os.path.abspath(MODEL_FILENAME)}")