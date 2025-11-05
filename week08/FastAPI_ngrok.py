# https://ngrok.com/docs/using-ngrok-with/fastAPI

from contextlib import asynccontextmanager
from os import getenv
import ngrok
import uvicorn
from fastapi import FastAPI
from loguru import logger

# 🌟 추가: .env 파일을 로드하는 코드
from dotenv import load_dotenv
load_dotenv() # .env 파일을 로드 (기본적으로 현재 디렉토리에서 찾음)
# 🌟 .env 파일의 변수 이름과 일치하도록 변경
# # .env 파일에 NGROK_AUTH_TOKEN으로 되어 있으므로, getenv에서도 NGROK_AUTH_TOKEN을 사용


NGROK_AUTH_TOKEN = getenv("NGROK_AUTH_TOKEN", "")
APPLICATION_PORT = 5000

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Setting up ngrok Endpoint")
    ngrok.set_auth_token(NGROK_AUTH_TOKEN)
    tunnel = await ngrok.forward(
        addr=APPLICATION_PORT,
    )
    # 이제 tunnel은 터널 객체이며, .url()을 호출할 수 있습니다.
    public_url = tunnel.url()
    logger.info(f"🚀 ngrok Public URL: {public_url}")
    
    yield
    logger.info("Tearing Down ngrok Endpoint")
    ngrok.disconnect()


app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("FastAPI_ngrok:app", host="127.0.0.1", port=APPLICATION_PORT, reload=True)