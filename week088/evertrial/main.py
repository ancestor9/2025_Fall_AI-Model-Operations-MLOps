from controllers.course_controller import app
import uvicorn
import threading
from views.course_view import demo

def run_gradio():
    demo.launch(server_name="0.0.0.0", server_port=7860, share=True)

if __name__ == "__main__":
    threading.Thread(target=run_gradio).start()
    uvicorn.run(app, host="0.0.0.0", port=8000)