### 1. Gradio와 FastAPI 별도 서버
- (모델학습 및 저장) train_model.py: 모델을 학습시키고 .pkl 파일로 저장
- (백엔드) api.py: FastAPI 백엔드 (저장된 모델을 로드하여 API 제공)
- (프론트엔드) app_gradio.py: Gradio 프론트엔드 (API 호출을 통해 사용자 인터페이스 제공)
- (외부 배포) To create a public link, set `share=True` in `launch()
| 구분              | 파일명          | 역할                           | 실행 주소 (기본 포트)      | 핵심 엔드포인트 / 함수       | 설명                                                                 |
|-------------------|----------------|--------------------------------|----------------------------|-------------------------------|----------------------------------------------------------------------|
| 백엔드 (서버)     | api.py         | FastAPI 서버 (모델 서빙)       | http://127.0.0.1:8000      | POST /predict/                | - 저장된 붓꽃 예측 모델(iris_model.pkl) 로드<br>- 입력 특성(sl, sw, pl, pw) 처리<br>- 예측 결과를 JSON 형태로 반환 |
| 프론트엔드 (클라이언트) | app_gradio.py   | Gradio 인터페이스 (UI/UX)      | http://127.0.0.1:7860      | predict_species()              | - 사용자에게 슬라이더 입력 제공<br>- FastAPI 서버(/predict) 호출<br>- 예측 결과를 UI에 표시 |
| 연결 URL          | app_gradio.py   | requests 모듈                  | http://127.0.0.1:8000/predict/ | requests.post(FASTAPI_URL, ...) | - Gradio 클라이언트가 FastAPI 서버에 데이터 전송<br>- API 호출을 통해 예측 요청 수행 |


### 2. Gradio mount_gradio_app 기능으로 단일 서버
- FastAPI 앱 내부에 Gradio 인터페이스를 직접 통합(mount) : [Mount a gradio.Blocks to an existing FastAPI application](https://www.gradio.app/docs/gradio/mount_gradio_app)
- 두 서버의 실행 대신 하나의 Uvicorn 프로세스로 FastAPI API와 Gradio UI를 동시에 서비스하여 코드가 훨씬 간결해지고 실행이 편리해짐
- FastAPI 백엔드(api.py)와 Gradio 프론트엔드(app_gradio.py)의 기능을 **하나의 파일(main_mounted.py)**로 합친 간결한 코드
- 🚀 Gradio Mount 통합 코드 (main_mounted.py) : train_model.py를 먼저 실행하여 iris_model.pkl 파일이 생성되어 있다는 가정 하에 작동
-     브라우저 주소창에 http://127.0.0.1:8000/api/predict  접근하는 것은 기본적으로 GET HTTP 메소드를 사용하면
      정의된 것이 없거나 허용되지 않았기 때문에 405 Method Not Allowed 오류를 반환하며, JSON으로 {"detail":"Method Not Allowed"}를 표시
      FastAPI swagger 혹은 http://127.0.0.1:8000/gradio/ 에서 POST 메소드 실행하면 됨

