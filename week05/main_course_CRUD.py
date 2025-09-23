from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import csv
from typing import List, Optional

# 요청된 필드만 포함하는 Pydantic 모델
class Course(BaseModel):
    교과목명: str
    개설학년: int
    강좌담당교수: str
    수업주수: int

# FastAPI 앱 인스턴스 생성
app = FastAPI()

# 데이터를 저장할 전역 변수
courses_data: List[Course] = []

# 애플리케이션 시작 시 데이터 로드
@app.on_event("startup")
def load_data():
    global courses_data
    file_path = "courses_data.csv"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    # 필요한 필드만 추출하여 형 변환
                    course = Course(
                        교과목명=row['교과목명'],
                        개설학년=int(row['개설학년']),
                        강좌담당교수=row['강좌담당교수'],
                        수업주수=int(row['수업주수'])
                    )
                    courses_data.append(course)
                except (ValueError, KeyError) as e:
                    # 데이터 변환 또는 필드 누락 오류 처리
                    print(f"Error processing row: {row}. Error: {e}")
                    continue  # 문제가 있는 행은 건너뛰고 계속 진행
    except FileNotFoundError:
        # 파일이 없을 경우, 서버 시작을 중단하고 오류를 발생시킴
        raise RuntimeError(f"Error: The file '{file_path}' was not found.")

# CRUD API 엔드포인트는 이전과 동일합니다.
# 1. Read: 모든 강의 조회
@app.get("/courses/", response_model=List[Course])
def read_courses():
    return courses_data

# 2. Read: 특정 강의 조회 (교과목명 사용)
@app.get("/courses/{course_name}", response_model=Course)
def read_course(course_name: str):
    for course in courses_data:
        if course.교과목명 == course_name:
            return course
    raise HTTPException(status_code=404, detail="Course not found")

# 3. Create: 새로운 강의 추가
@app.post("/courses/", response_model=Course)
def create_course(new_course: Course):
    courses_data.append(new_course)
    return new_course

# 4. Update: 기존 강의 정보 수정 (교과목명 사용)
@app.put("/courses/{course_name}", response_model=Course)
def update_course(course_name: str, updated_course: Course):
    for index, course in enumerate(courses_data):
        if course.교과목명 == course_name:
            courses_data[index] = updated_course
            return updated_course
    raise HTTPException(status_code=404, detail="Course not found")

# 5. Delete: 특정 강의 삭제 (교과목명 사용)
@app.delete("/courses/{course_name}")
def delete_course(course_name: str):
    for index, course in enumerate(courses_data):
        if course.교과목명 == course_name:
            del courses_data[index]
            return {"message": "Course deleted successfully"}
    raise HTTPException(status_code=404, detail="Course not found")

# 실행: `uvicorn main:app --reload`