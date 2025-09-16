import pandas as pd  # 누락된 import 추가
from fastapi import FastAPI, UploadFile, Form
from models.course_model import CourseModel, Course

model = CourseModel()
app = FastAPI()

@app.post("/upload")
async def upload_csv(file: UploadFile):
    import io
    content = await file.read()
    model.df = pd.read_csv(io.BytesIO(content))
    return {"status": "uploaded"}

@app.get("/")
def root():
    if model.df.empty:
        return "<p>데이터가 없습니다. CSV 파일을 먼저 업로드하세요.</p>"
    df = model.sort_by_professor()
    return df.to_html(index=False)

@app.get("/이름")
def get_by_name(name: str):
    if model.df.empty:
        return "<p>데이터가 없습니다.</p>"
    result = model.search_by_professor(name)
    return result.to_html(index=False)

@app.get("/학점")
def get_by_credit(credit: int):
    if model.df.empty:
        return "<p>데이터가 없습니다.</p>"
    result = model.search_by_credit(credit)
    return result.to_html(index=False)

@app.post("/교수배정")
def add_course(
    교과목명: str = Form(...),
    강좌담당교수: str = Form(...),
    개설학년: int = Form(...),
    교과목학점: int = Form(...)
):
    course = Course(
        교과목명=교과목명,
        강좌담당교수=강좌담당교수,
        개설학년=개설학년,
        교과목학점=교과목학점
    )
    model.add_course(course)
    return {"status": "added"}

@app.post("/교수삭제")
def delete_course(교과목명: str = Form(...)):
    model.delete_course(교과목명)
    return {"status": "deleted"}