### 1. gradio UI
- 1.1. FastAPI로 머신러닝 학습/예측 ----> api.py(서버), app_gradio.py(클아이언트)
-             a. POST 방식을 UI에 표현할 필요성 이해  ----> api.py
              b. UI화면이 별도 필요하여 별도 웹서버    ----> app_gradio.py with api.py
              c. Front/BackEnd 별도 서버로 snippet    ----> gradio_fastapi_twoservers.py
              d. gradio를 FastAPI에 Mount 단일 서버   ----> main_gradio_mount.py
- 1.2. gradio를 FastAPI에 Mount / Seperate port 실습 ----> gradio_mount.py



### 2. mini project : Gradio와 FastAPI 별도 서버
- (모델학습 및 저장) train_model.py: 모델을 학습시키고 에측모형을 *.pkl 파일로 저장
- (백엔드) api.py: FastAPI 백엔드 (저장된 모델을 로드하여 API 제공)
- (프론트엔드) app_gradio.py: Gradio 프론트엔드 (API 호출을 통해 사용자 인터페이스 제공)
- (외부 배포) To create a public link, set `share=True` in `launch()

| 구분              | 파일명          | 역할                           | 실행 주소 (기본 포트)      | 핵심 엔드포인트 / 함수       | 설명                                                                 |
|-------------------|----------------|--------------------------------|----------------------------|-------------------------------|----------------------------------------------------------------------|
| 백엔드 (서버)     | api.py         | FastAPI 서버 (모델 서빙)       | http://127.0.0.1:8000      | POST /predict/                | - 저장된 붓꽃 예측 모델(iris_model.pkl) 로드<br>- 입력 특성(sl, sw, pl, pw) 처리<br>- 예측 결과를 JSON 형태로 반환 |
| 프론트엔드 (클라이언트) | app_gradio.py   | Gradio 인터페이스 (UI/UX)      | http://127.0.0.1:7860      | predict_species()              | - 사용자에게 슬라이더 입력 제공<br>- FastAPI 서버(/predict) 호출<br>- 예측 결과를 UI에 표시 |
| 연결 URL          | app_gradio.py   | requests 모듈                  | http://127.0.0.1:8000/predict/ | requests.post(FASTAPI_URL, ...) | - Gradio 클라이언트가 FastAPI 서버에 데이터 전송<br>- API 호출을 통해 예측 요청 수행 |

### 3. mini project  : 단일 서버
- 🚀 Gradio Mount 통합 간결 코드 (main_gradio_mount.py) :
-     train_model.py를 먼저 실행하여 iris_model.pkl 파일이 생성되어 있다는 가정 하에 작동
      브라우저 주소창에 http://127.0.0.1:8000/api/predict  접근하는 것은 기본적으로 GET HTTP 메소드를 사용하면
      정의된 것이 없거나 허용되지 않았기 때문에 405 Method Not Allowed 오류를 반환하며, JSON으로 {"detail":"Method Not Allowed"}를 표시
      FastAPI swagger 혹은 http://127.0.0.1:8000/gradio/ 에서 POST 메소드 실행하면 됨
