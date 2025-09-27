# from fastapi import FastAPI

# test_DB = {"item1": "This is item 1", 'customer1': 'Sangoo',
#            "item2": "This is item 2",   'customer2': 'Alice'}   

# app = FastAPI()
# @app.get("/")
# def read_root():
#     return {"Hello": "Sangoo"}

# @app.get("/items/{item_id}")
# def read_item(item_id: str):
#     return {"item_id": item_id, "desc": test_DB.get(item_id, "Not Found")}

# @app.get("/customers/{customer_id}")
# def read_customer(customer_id: str):
#     return {"customer_id": customer_id, "name": test_DB.get(customer_id, "Not Found")}

# @app.post("/items/post/{item_id}")
# def create_item(item_id: str, desc: str):
#     test_DB[item_id] = desc
#     return {"item_id": item_id, "desc": test_DB[item_id]}

# @app.post("/customers/post/{customer_id}")
# def create_customer(customer_id: str, name: str):
#     test_DB[customer_id] = name
#     return {"customer_id": customer_id, "name": test_DB[customer_id]}   

# import pandas as pd

# file_path = 'courses_data.csv'
# df = pd.read_csv(file_path)

# @app.get("/students")
# def get_students():
#     return df.to_dict(orient='records')

# @app.get("/teachers/{teacher_name}")
# def get_student(teacher_name: str):
#     student = df[df['강좌담당교수'] == teacher_name]
#     if student.empty:
#         return {"error": "Student not found"}
#     return student.to_dict(orient='records') # student.to_dict(orient='records')[0]

###############################
### Router Path Parameters
###############################
from fastapi import FastAPI
import product # product.py에서 정의한 라우터 가져오기
import customer # customer.py에서 정의한 라우터 가져오기

app = FastAPI(title="Product & Customer API")

# product 라우터를 메인 앱에 포함
# 경로: /product/...
app.include_router(product.router)

# customer 라우터를 메인 앱에 포함
# 경로: /customer/...
app.include_router(customer.router)

@app.get("/")
def read_root():
    """루트 경로 (/)는 기본 메시지를 반환합니다."""
    return {"message": "Welcome to the API! Use /product or /customer paths."}