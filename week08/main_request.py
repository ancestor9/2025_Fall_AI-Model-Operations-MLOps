##############################
from fastapi import FastAPI, Request
# from typing import Optional
# Request 객체는 경로 함수의 매개변수에 Request 타입 힌트를 지정하여 FastAPI가 자동으로 주입

app = FastAPI()

@app.get("/request-info/")
async def get_request_info(request: Request): # 👈 Request 객체를 주입받음
    """
    들어온 HTTP 요청의 다양한 정보를 반환하는 엔드포인트입니다.
    """

    # 1. 클라이언트 정보 가져오기 (IP 주소)
    client_host = request.client.host if request.client else "Unknown"
    
    # 2. 요청 메소드와 전체 URL 가져오기
    method = request.method
    full_url = str(request.url)
    
    # 3. 특정 헤더 값 가져오기 (예: User-Agent)
    user_agent = request.headers.get("user-agent", "N/A")
    
    # 4. 쿼리 매개변수 직접 접근
    # 'q'라는 쿼리 매개변수가 있다면 가져오고, 없으면 None
    custom_query = request.query_params.get("custom_q")
    
    return {
        "client_host": client_host,
        "http_method": method,
        "request_url": full_url,
        "user_agent": user_agent,
        "custom_query_param": custom_query,
        "message": "Request 객체를 통해 요청의 세부 정보에 접근했습니다."
    }

@app.post("/request-raw-body/")
async def process_raw_body(request: Request):
    """
    요청 본문을 Pydantic 모델 대신 Raw 데이터(바이트)로 직접 처리합니다.
    """
    
    # await request.body()를 사용하여 요청 본문을 비동기적으로 읽어옵니다.
    raw_body = await request.body()
    
    return {
        "received_body_length": len(raw_body),
        "first_50_bytes": raw_body[:50].decode('utf-8', errors='ignore'),
        "data_type": "Raw Bytes"
    }

# 사용자가 body를 받으려면, 해당 엔드포인트에 HTTP POST 요청을 보내야 하며, 
# 요청 시 **본문(Body)**에 서버로 전달하고 싶은 데이터를 포함

# ----------------------------------------------------
# 1. Pydantic 모델: 일반적인 JSON 요청 본문을 위한 정의 (비교용)
# ----------------------------------------------------
from pydantic import BaseModel
from typing import Union

class Item(BaseModel):
    name: str
    price: float
    description: Union[str, None] = None

@app.post("/items/json/")
def create_item(item: Item):
    """
    일반적인 방법: Pydantic을 사용하여 JSON 요청 본문을 자동 파싱하고 유효성 검사.
    (Content-Type: application/json 필요)
    """
    return {"message": "Item processed by Pydantic", "item_name": item.name}

# ----------------------------------------------------
# 2. Request 객체를 사용하여 Raw Body를 처리하는 엔드포인트
# ----------------------------------------------------
@app.post("/request-raw-body-direct/")
async def process_raw_body(request: Request):
    """
    Request 객체의 request.body() 메서드를 사용하여
    요청 본문을 Raw 바이트 데이터로 직접 읽어 처리합니다.
    """
    
    # request.body()는 비동기 함수(await 필요)이며, 요청 본문을 bytes로 반환합니다.
    try:
        raw_body_bytes = await request.body()
    except Exception as e:
        # 본문을 읽는 중 오류가 발생할 경우 (매우 드묾)
        return {"error": f"Failed to read body: {e}"}

    # 받은 바이트 데이터를 분석하여 응답으로 반환
    body_length = len(raw_body_bytes)
    
    # 받은 바이트를 문자열로 변환 (UTF-8 디코딩)
    # 데이터가 텍스트가 아닐 경우를 대비해 오류 무시(ignore) 옵션 사용
    decoded_body = raw_body_bytes.decode('utf-8', errors='ignore')
    
    return {
        "received_data_type": "Raw Bytes",
        "body_length_bytes": body_length,
        "decoded_content_preview": decoded_body[:100], # 앞 100자만 미리보기
        "http_method": request.method,
        "client_ip": request.client.host if request.client else "N/A"
    }

@app.post("/request-process/")
async def process_full_request(request: Request):
    """
    HTTP POST 요청의 헤더, 클라이언트 정보, Raw 요청 본문을 모두 읽어 반환합니다.
    """
    
    # 1. Raw 요청 본문 읽기 (비동기 처리 필요)
    try:
        raw_body_bytes = await request.body()
    except Exception:
        raw_body_bytes = b"" # 본문이 없거나 읽기 실패 시 빈 바이트 처리
    
    # 2. 요청 정보 분석
    client_ip = request.client.host if request.client else "N/A"
    
    # Content-Type 헤더 가져오기 (클라이언트가 보낸 데이터 타입)
    content_type = request.headers.get("content-type", "N/A")
    
    # User-Agent 헤더 가져오기 (클라이언트 소프트웨어 정보)
    user_agent = request.headers.get("user-agent", "N/A")

    # 3. 본문 디코딩 및 미리보기
    body_length = len(raw_body_bytes)
    
    # Raw 바이트를 문자열로 변환하여 본문 내용 일부를 미리 보여줍니다.
    decoded_body_preview = raw_body_bytes.decode('utf-8', errors='ignore')[:100]

    return {
        "status": "success",
        "message": "Full request details received and processed.",
        "client_info": {
            "ip": client_ip,
            "method": request.method,
            "url": str(request.url)
        },
        "request_data": {
            "content_type_header": content_type,
            "user_agent_header": user_agent,
            "body_length_bytes": body_length,
            "body_preview": decoded_body_preview
        }
    }



#################################

# from fastapi import FastAPI, Response, status

# app = FastAPI()

# # 딕셔너리 반환:
# # FastAPI가 자동으로 상태 코드를 200 OK로 설정하고, 
# # JSON 콘텐츠 타입 헤더를 추가하여 HTTPResponse를 생성합니다.

# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}

# # 상태 코드와 헤더 직접 설정:
# # Response 객체를 사용해 HTTP 응답을 명시적으로 제어합니다.
# @app.get("/custom-response", status_code=status.HTTP_201_CREATED)
# def custom_response(response: Response):
#     # 헤더를 직접 설정할 수 있습니다.
#     response.headers["X-Custom-Header"] = "This is a custom header"
    
#     # 이 딕셔너리도 자동으로 JSON 바디가 됩니다.
#     return {"status": "success"}

# # 바이너리 데이터(파일) 반환:
# # FileResponse를 사용해 파일을 HTTP 응답으로 보냅니다.
# from fastapi.responses import FileResponse

# @app.get("/image")
# def get_image():
#     # 'star.png' 파일을 HTTP 응답의 바디로 보냅니다.
#     # FastAPI가 Content-Disposition 헤더 등을 자동으로 설정합니다.
#     return FileResponse(r"D:\2025_Fall_AI-Model-Operations-MLOps\스크린샷 2025-09-20 130257.png", media_type="image/png")

# # HTML 페이지 반환:
# # HTMLResponse를 사용해 HTML 콘텐츠를 보냅니다.
# from fastapi.responses import HTMLResponse

# @app.get("/html", response_class=HTMLResponse)
# async def read_html():
#     content = """
#     <html>
#         <body>
#             <h1>안녕하세요, FastAPI!</h1>
#             <p>이것은 HTML 응답입니다.</p>
#         </body>
#     </html>
#     """
#     return content

# from pydantic import BaseModel
# from fastapi import Request

# class Item(BaseModel):
#     name: str
#     price: float
#     description: str | None = None

# @app.get("/home")
# async def get_request_info(request: Request):
#     client_host = request.client.host
#     method = request.method
#     headers = request.headers
#     return {
#         "client_host": client_host,
#         "method": method,
#         "headers": headers,
#         "path": request.url.path,
#         "query_params": request.query_params
#     }

# @app.get("/items")
# async def read_item(request: Request):
#     client_host = request.client.host
#     headers = request.headers
#     query_params = request.query_params
#     url = request.url
#     path_params = request.path_params
#     http_method = request.method
    
#     return {
#             "client_host": client_host,
#             "headers": headers,
#             "query_params": query_params,
#             "path_params": path_params,
#             "url": str(url),
#             "http_method":  http_method
#         }


# @app.get("/items/{item_group}")
# async def read_item_p(request: Request, item_group: str):
#     client_host = request.client.host
#     headers = request.headers 
#     query_params = request.query_params
#     url = request.url
#     path_params = request.path_params
#     http_method = request.method

#     return {
#         "client_host": client_host,
#         "headers": headers,
#         "query_params": query_params,
#         "path_params": path_params,
#         "url": str(url),
#         "http_method":  http_method
#     }

# @app.post("/items_json/")
# async def create_item_json(item: Item):
#     # FastAPI automatically handles the parsing and validation
#     print("received_item:", item.model_dump()) # Parse JSON bodㅛ
#     return {"received_item": item}


# @app.post("/items_form/")
# async def create_item_form(request: Request):
#     data = await request.form() # Parse Form body
#     print("received_data:", data)
#     return {"received_data": data}