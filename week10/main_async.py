from fastapi import FastAPI
import asyncio

app = FastAPI()

from fastapi import FastAPI
import asyncio

app = FastAPI()

# 1. 비동기 "긴 작업" 함수 정의
async def simulate_long_task():
    # 5초 동안 논블로킹 방식으로 대기 (I/O 작업 시뮬레이션)
    await asyncio.sleep(5) 
    return "Task completed!"

# 2. API 경로 정의 및 비동기 함수 호출
@app.get("/long-task/")
async def long_task():
    # 긴 작업을 기다리지만, 그동안 다른 요청을 처리할 수 있음
    result = await simulate_long_task() 
    return {"message": result}

# 3. 추가: 즉시 응답하는 빠른 API 경로 (비교용)
@app.get("/quick-task/")
async def quick_task():
    return {"message": "Quick response!"}

# async def simulate_long_task():
#     await asyncio.sleep(5)  # Simulates a long task (like a network request)
#     return "Task completed!"

# @app.get("/long-task/")
# async def long_task():
#     result = await simulate_long_task()  # Await the long task
#     return {"message": result}