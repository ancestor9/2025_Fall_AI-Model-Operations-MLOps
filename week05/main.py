

# from typing import Union

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
# #=======
# # 필요한 라이브러리들을 불러옵니다.
# from typing import Union
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel

# # FastAPI 애플리케이션 인스턴스를 생성합니다.
# app = FastAPI()

# # 상품 데이터 모델을 정의합니다.
# # Pydantic을 사용하여 데이터의 형식을 자동으로 검증합니다.
# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

# # 임시로 사용할 인메모리 데이터베이스입니다.
# # 실제 애플리케이션에서는 데이터베이스를 사용해야 합니다.
# items_db = {}

# # 루트 경로 ("/")에 대한 GET 요청을 처리합니다.
# @app.get("/")
# def read_root():
#     return {"message": "Hello, this is a simple FastAPI application!"}

# # 모든 상품 목록을 조회하는 GET 요청을 처리합니다.
# @app.get("/items/")
# def get_all_items():
#     return items_db

# # 특정 상품 ID에 대한 GET 요청을 처리합니다.
# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     # 만약 상품 ID가 데이터베이스에 없으면 404 에러를 반환합니다.
#     if item_id not in items_db:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return items_db[item_id]

# # 새로운 상품을 생성하는 POST 요청을 처리합니다.
# @app.post("/items/{item_id}")
# def create_item(item_id: int, item: Item):
#     # 새로운 상품을 데이터베이스에 추가합니다.
#     items_db[item_id] = item
#     return {"message": "Item created successfully!", "item": item}

# # 특정 상품 ID의 정보를 업데이트하는 PUT 요청을 처리합니다.
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     # 만약 상품 ID가 데이터베이스에 없으면 404 에러를 반환합니다.
#     if item_id not in items_db:
#         raise HTTPException(status_code=404, detail="Item not found")
#     # 기존 상품 정보를 새로운 정보로 업데이트합니다.
#     items_db[item_id] = item
#     return {"message": "Item updated successfully!", "item": item}


#########################################
# 데이터베이스 만들기전에 csv로 만들어 보기
#########################################
# 필요한 라이브러리들을 불러옵니다.
# from typing import Union
# from fastapi import FastAPI, HTTPException
# from fastapi.responses import StreamingResponse
# from pydantic import BaseModel
# import csv
# import io

# # FastAPI 애플리케이션 인스턴스를 생성합니다.
# app = FastAPI()

# # 상품 데이터 모델을 정의합니다.
# # Pydantic을 사용하여 데이터의 형식을 자동으로 검증합니다.
# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

# # 임시로 사용할 인메모리 데이터베이스입니다.
# # 실제 애플리케이션에서는 데이터베이스를 사용해야 합니다.
# items_db = {
#     1: {"name": "Laptop", "price": 1200.0, "is_offer": True},
#     2: {"name": "Mouse", "price": 25.0, "is_offer": False},
#     3: {"name": "Keyboard", "price": 75.0, "is_offer": True}
# }

# # 루트 경로 ("/")에 대한 GET 요청을 처리합니다.
# @app.get("/")
# def read_root():
#     return {"message": "Hello, this is a simple FastAPI application!"}

# # 모든 상품 목록을 조회하는 GET 요청을 처리합니다.
# @app.get("/items/")
# def get_all_items():
#     return items_db

# # 특정 상품 ID에 대한 GET 요청을 처리합니다.
# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     # 만약 상품 ID가 데이터베이스에 없으면 404 에러를 반환합니다.
#     if item_id not in items_db:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return items_db[item_id]

# # 새로운 상품을 생성하는 POST 요청을 처리합니다.
# @app.post("/items/{item_id}")
# def create_item(item_id: int, item: Item):
#     # 새로운 상품을 데이터베이스에 추가합니다.
#     items_db[item_id] = item
#     return {"message": "Item created successfully!", "item": item}

# # 특정 상품 ID의 정보를 업데이트하는 PUT 요청을 처리합니다.
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     # 만약 상품 ID가 데이터베이스에 없으면 404 에러를 반환합니다.
#     if item_id not in items_db:
#         raise HTTPException(status_code=404, detail="Item not found")
#     # 기존 상품 정보를 새로운 정보로 업데이트합니다.
#     items_db[item_id] = item
#     return {"message": "Item updated successfully!", "item": item}

# # CSV 파일을 다운로드하는 GET 요청을 처리합니다.
# @app.get("/download-items-csv")
# def download_items_csv():
#     # CSV 파일을 메모리에 생성하기 위한 StringIO 객체를 만듭니다.
#     output = io.StringIO()
#     writer = csv.writer(output)

#     # CSV 헤더를 작성합니다.
#     writer.writerow(["item_id", "name", "price", "is_offer"])
    
#     # items_db의 데이터를 순회하며 CSV에 씁니다.
#     for item_id, item in items_db.items():
#         writer.writerow([item_id, item['name'], item['price'], item['is_offer']])

#     # 파일 스트림의 시작으로 되돌립니다.
#     output.seek(0)
    
#     # StreamingResponse를 사용하여 CSV 파일을 다운로드할 수 있도록 합니다.
#     # media_type을 'text/csv'로 설정하고, 파일 이름을 지정합니다.
#     return StreamingResponse(
#         io.BytesIO(output.getvalue().encode('utf-8')),
#         media_type='text/csv',
#         headers={"Content-Disposition": "attachment; filename=items.csv"}
#     )
