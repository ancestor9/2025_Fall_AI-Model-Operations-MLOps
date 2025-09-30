# from fastapi import FastAPI
# import gradio as gr

# app = FastAPI()
# @app.get("/")
# def read_main():
#     return {"message": "This is your main app"}
# io = gr.Interface(lambda x: "Hello, " + x + "!", "textbox", "textbox")
# app = gr.mount_gradio_app(app, io, path="/gradio")


import gradio as gr
def echo(text, request: gr.Request):
    if request:
        print("Request headers dictionary:", request.headers)
        print("IP address:", request.client.host)
        print("Query parameters:", dict(request.query_params))
        print("Session hash:", request.session_hash)
    return text

io = gr.Interface(echo, "textbox", "textbox").launch()