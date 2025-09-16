import pandas as pd
from pydantic import BaseModel

class Course(BaseModel):
    교과목명: str
    강좌담당교수: str
    개설학년: int
    교과목학점: int

class CourseModel:
    def __init__(self):
        self.df = pd.DataFrame()

    def load_csv(self, file_path):
        self.df = pd.read_csv(file_path)
        # CSV 파일 로드 후 컬럼명 확인 및 정리
        print("CSV 컬럼명:", self.df.columns.tolist())

    def sort_by_professor(self):
        # 컬럼 존재 여부 확인
        if '강좌담당교수' in self.df.columns:
            return self.df.sort_values("강좌담당교수", ascending=False)
        else:
            print("사용 가능한 컬럼:", self.df.columns.tolist())
            return self.df

    def search_by_professor(self, name):
        if '강좌담당교수' in self.df.columns:
            return self.df[self.df["강좌담당교수"] == name][["교과목명", "개설학년", "교과목학점"]]
        else:
            return pd.DataFrame()

    def search_by_credit(self, credit):
        if '교과목학점' in self.df.columns:
            return self.df[self.df["교과목학점"] == credit][["교과목명", "강좌담당교수", "개설학년", "교과목학점"]]
        else:
            return pd.DataFrame()

    def add_course(self, course):
        # Course 객체와 딕셔너리 모두 처리 가능하도록 수정
        if isinstance(course, Course):
            course_dict = course.model_dump()  # Pydantic v2에서는 model_dump() 사용
        else:
            course_dict = course
        
        # DataFrame에 새 행 추가
        new_row = pd.DataFrame([course_dict])
        self.df = pd.concat([self.df, new_row], ignore_index=True)

    def delete_course(self, subject):
        if '교과목명' in self.df.columns:
            self.df = self.df[self.df["교과목명"] != subject]