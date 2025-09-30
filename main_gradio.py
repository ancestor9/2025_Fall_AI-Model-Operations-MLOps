# from fastapi import FastAPI
# import gradio as gr

# app = FastAPI()
# @app.get("/")
# def read_main():
#     return {"message": "This is your main app"}
# io = gr.Interface(lambda x: "Hello, " + x + "!", "textbox", "textbox")
# app = gr.mount_gradio_app(app, io, path="/gradio")

##################################################
# import gradio as gr
# def echo(text, request: gr.Request):
#     if request:
#         print("Request headers dictionary:", request.headers)
#         print("IP address:", request.client.host)
#         print("Query parameters:", dict(request.query_params))
#         print("Session hash:", request.session_hash)
#     return text

# io = gr.Interface(echo, "textbox", "textbox").launch()

##############################
import gradio as gr

def echo_with_request_info(text, request: gr.Request):
    # 요청 정보를 문자열로 조합합니다.
    info = f"--- 요청 정보 (Request Details) ---\n"
    info += f"입력 텍스트 (Input Text): {text}\n"
    info += f"IP 주소 (IP Address): {request.client.host}\n"
    info += f"세션 해시 (Session Hash): {request.session_hash}\n"
    info += f"쿼리 파라미터 (Query Params): {dict(request.query_params)}\n"
    
    # 헤더는 너무 길 수 있으므로 줄여서 표시합니다.
    # info += f"전체 헤더 (Full Headers):\n{request.headers}\n"

    # 모든 정보를 담은 문자열을 반환하여 웹 브라우저에 표시합니다.
    return info

# 입출력 컴포넌트를 정의합니다. 
# "textbox" 대신 "text"로 입력하고, 출력은 여러 줄을 표시할 수 있도록 "textarea"를 사용하는 것이 좋습니다.
io = gr.Interface(
    fn=echo_with_request_info, 
    inputs=gr.Textbox(label="여기에 텍스트를 입력하세요"), 
    outputs=gr.Textbox(label="요청 정보 출력", lines=10),
    title="Gradio 요청 정보 확인 앱"
).launch()