'''
https://fastapi.tiangolo.com/ko/tutorial/
자습서 - 사용자 안내서
'''
######### 1 ######
# FastAPI 설치
# pip install fastapi   # FastAPI 설치
# pip install "uvicorn[standard]"  # Uvicorn 설치   # Uvicorn은 ASGI 서버로, FastAPI 애플리케이션을 실행하는 데 사용


######### 2 ######
# FastAPI 애플리케이션 생성
# main.py 파일 생성 (02_learn_FastAPI.py 생성)
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

######### 3 ######
# 경로 매개변수
# main.py 파일에 다음 코드 추가

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id} 

#######
from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}    

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

       