from fastapi import FastAPI
import gradio as gr

####################################################
# FastAPI와 Gradio 통합 예제
####################################################
app = FastAPI()
@app.get("/")
def read_main():
    return {"message": "This is your main app"}
io = gr.Interface(lambda x: "Hello, " + x + "!", "textbox", "textbox")
app = gr.mount_gradio_app(app, io, path="/gradio")

####################################################
# FastAPI와 Gradio 별도 분리 예제
# 🚀 Gradio와 FastAPI를 별도 서버로 실행하는 방법
####################################################
