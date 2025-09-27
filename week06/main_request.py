from fastapi import FastAPI, Response, status

app = FastAPI()

# 딕셔너리 반환:
# FastAPI가 자동으로 상태 코드를 200 OK로 설정하고, 
# JSON 콘텐츠 타입 헤더를 추가하여 HTTPResponse를 생성합니다.
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# 상태 코드와 헤더 직접 설정:
# Response 객체를 사용해 HTTP 응답을 명시적으로 제어합니다.
@app.get("/custom-response", status_code=status.HTTP_201_CREATED)
def custom_response(response: Response):
    # 헤더를 직접 설정할 수 있습니다.
    response.headers["X-Custom-Header"] = "This is a custom header"
    
    # 이 딕셔너리도 자동으로 JSON 바디가 됩니다.
    return {"status": "success"}

# 바이너리 데이터(파일) 반환:
# FileResponse를 사용해 파일을 HTTP 응답으로 보냅니다.
from fastapi.responses import FileResponse

@app.get("/image")
def get_image():
    # 'star.png' 파일을 HTTP 응답의 바디로 보냅니다.
    # FastAPI가 Content-Disposition 헤더 등을 자동으로 설정합니다.
    return FileResponse(r"D:\2025_Fall_AI-Model-Operations-MLOps\스크린샷 2025-09-20 130257.png", media_type="image/png")

# HTML 페이지 반환:
# HTMLResponse를 사용해 HTML 콘텐츠를 보냅니다.
from fastapi.responses import HTMLResponse

@app.get("/html", response_class=HTMLResponse)
async def read_html():
    content = """
    <html>
        <body>
            <h1>안녕하세요, FastAPI!</h1>
            <p>이것은 HTML 응답입니다.</p>
        </body>
    </html>
    """
    return content

from pydantic import BaseModel
from fastapi import Request

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

@app.get("/home")
async def get_request_info(request: Request):
    client_host = request.client.host
    method = request.method
    headers = request.headers
    return {
        "client_host": client_host,
        "method": method,
        "headers": headers,
        "path": request.url.path,
        "query_params": request.query_params
    }

@app.get("/items")
async def read_item(request: Request):
    client_host = request.client.host
    headers = request.headers
    query_params = request.query_params
    url = request.url
    path_params = request.path_params
    http_method = request.method
    
    return {
            "client_host": client_host,
            "headers": headers,
            "query_params": query_params,
            "path_params": path_params,
            "url": str(url),
            "http_method":  http_method
        }


@app.get("/items/{item_group}")
async def read_item_p(request: Request, item_group: str):
    client_host = request.client.host
    headers = request.headers 
    query_params = request.query_params
    url = request.url
    path_params = request.path_params
    http_method = request.method

    return {
        "client_host": client_host,
        "headers": headers,
        "query_params": query_params,
        "path_params": path_params,
        "url": str(url),
        "http_method":  http_method
    }

@app.post("/items_json/")
async def create_item_json(item: Item):
    # FastAPI automatically handles the parsing and validation
    print("received_item:", item.model_dump()) # Parse JSON bodㅛ
    return {"received_item": item}


@app.post("/items_form/")
async def create_item_form(request: Request):
    data = await request.form() # Parse Form body
    print("received_data:", data)
    return {"received_data": data}