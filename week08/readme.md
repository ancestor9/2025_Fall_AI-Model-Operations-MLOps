### 1. Gradio와 FastAPI 별도 서버
- 1.1. train_model.py: 모델을 학습시키고 .pkl 파일로 저장
- 1.2. api.py: FastAPI 백엔드 (저장된 모델을 로드하여 API 제공)
- 1.3. app_gradio.py: Gradio 프론트엔드 (API 호출을 통해 사용자 인터페이스 제공)
- 1.4. To create a public link, set `share=True` in `launch()

### 2. Gradio의 mount_gradio_app 
- 이 기능을 사용하면 FastAPI 앱 내부에 Gradio 인터페이스를 직접 통합(mount)
- 두 서버를 따로 실행할 필요 없이 하나의 Uvicorn 프로세스로 FastAPI API와 Gradio UI를 동시에 서비스할 수 있어 코드가 훨씬 간결해지고 실행이 편리해짐
- FastAPI 백엔드(api.py)와 Gradio 프론트엔드(app_gradio.py)의 기능을 **하나의 파일(main_mounted.py)**로 합친 간결한 코드
- 🚀 Gradio Mount 통합 코드 (main_mounted.py) : train_model.py를 먼저 실행하여 iris_model.pkl 파일이 생성되어 있다는 가정 하에 작동
