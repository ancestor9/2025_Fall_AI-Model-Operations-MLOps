
'''
Gradio와 FastAPI를 함께 사용하는 두 가지 주요 방법
---------------------------------------------------------------------------------------------------------------------------
통합 방식	   마운트(Mounting)	                                    별도 서버 실행
실행 구조	   단일 서버	                                        이중 서버 (Two Servers)
FastAPI 포트  FastAPI와 Gradio가 같은 포트(예: 8000)를 사용          FastAPI는 기본 포트(예: 8000)를, Gradio는 별도의 포트(예: 7860)를 사용
Gradio URL   http://127.0.0.1:8000/gradio (FastAPI 경로의 일부)    http://127.0.0.1:7860 (별도의 Gradio 서버)
목적	     Gradio UI를 FastAPI 애플리케이션의 특정 서브 경로에 포함	FastAPI를 API 백엔드로 사용하고 Gradio UI는 완전히 독립된 서비스로 제공하고자 할 때 적합
---------------------------------------------------------------------------------------------------------------------------
'''

########################################################################################
# 1. Example of mounting a Gradio app within a FastAPI application
# https://www.gradio.app/docs/gradio/mount_gradio_app
# Then run uvicorn run:app from the terminal and navigate to http://localhost:8000/gradio.

from fastapi import FastAPI
import gradio as gr
app = FastAPI()

@app.get("/")
def read_main():
    return {"message": "This is your main app"}

io = gr.Interface(lambda x: "Hello, " + x + "!", "textbox", "textbox")
app = gr.mount_gradio_app(app, io, path="/gradio")

# # uvicorn gradio_mount:app --reload --port 8000
# # FastAPI 접근: http://127.0.0.1:8000/
# # Gradio 접근: http://127.0.0.1:8000/gradio

'''
첫 번째 인자 (app): Gradio UI를 연결할 대상인 FastAPI 인스턴스
두 번째 인자 (io): FastAPI에 연결할 Gradio 인터페이스 객체
세 번째 인자 (path="/gradio"): Gradio UI에 접근할 웹 경로를 /gradio로 지정
'''
########################################################################################
# 2. Example of running Gradio in a separate thread alongside FastAPI

# from fastapi import FastAPI
# import gradio as gr
# import threading

# app = FastAPI()

# # 💡 가정: Gradio 인터페이스를 생성하는 함수 (실제 애플리케이션에 따라 내용이 달라짐)
# def launch_gradio():
#     # 이전 예시와 동일한 간단한 인터페이스를 정의
#     io = gr.Interface(
#         fn=lambda x: "Hello, " + x + "!", 
#         inputs="textbox", outputs="textbox"
#     )
#     return io

# @app.get("/")
# def read_main():
#     # FastAPI의 메인 경로 (FastAPI 서버의 포트로 접근)
#     return {"message": "This is your main FastAPI app. Gradio runs on a different port (e.g., 7860)."}

# @app.on_event("startup")
# async def startup_event():
#     """
#     FastAPI 서버가 시작될 때 Gradio 서버를 별도의 스레드에서 실행합니다.
#     """
#     # 1. Gradio 인터페이스를 생성합니다.
#     demo = launch_gradio()
    
#     # 2. 새로운 스레드를 생성하여 Gradio 서버를 실행합니다.
#     #    이렇게 하면 FastAPI의 메인 프로세스를 막지 않고 Gradio가 독립적으로 실행됩니다.
#     thread = threading.Thread(
#         target=lambda: demo.launch(
#             server_name="127.0.0.1", 
#             server_port=7860, # Gradio는 7860 포트에서 실행됩니다.
#             share=True        # 공유 링크를 생성할 수도 있습니다.
#         )
#     )
#     thread.start()
#     print("Gradio server started on port 7860 in a separate thread.")

# # 🚨 실행 방법 (예시): 
# # 이 파일을 'main.py'로 저장했다면, 터미널에서 아래 명령어로 실행할 수 있습니다.
# # uvicorn gradio_mount:app --reload --port 8000
# # FastAPI 접근: http://127.0.0.1:8000/
# # Gradio 접근: http://127.0.0.1:7860/