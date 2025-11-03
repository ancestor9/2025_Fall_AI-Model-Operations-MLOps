from fastapi import FastAPI
from pyngrok import ngrok
import uvicorn
import os
import threading
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

def run_uvicorn():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    # 환경변수에서 ngrok API 키 가져오기
    NGROK_API_KEY = os.getenv('NGROK_API_KEY')
    
    if not NGROK_API_KEY:
        print("경고: NGROK_API_KEY가 .env 파일에 설정되지 않았습니다.")
    else:
        print(f"NGROK_API_KEY: {NGROK_API_KEY[:5]}...{NGROK_API_KEY[-2:]}")
        ngrok.set_auth_token(NGROK_API_KEY)
    
    # HTTP 터널을 기본 포트 8000에 열기
    http_tunnel = ngrok.connect(8000)
    print(f"Public URL: {http_tunnel.public_url}")
    
    # uvicorn을 별도 스레드에서 실행
    uvicorn_thread = threading.Thread(target=run_uvicorn)
    uvicorn_thread.start()