from pydantic import BaseModel
from typing import List
import csv

# 요청된 필드만 포함하는 Pydantic 모델
class Course(BaseModel):
    교과목명: str
    개설학년: int
    강좌담당교수: str
    수업주수: int
####################################    
### 방법 1
####################################
# 데이터를 저장할 전역 변수
'''
courses_data: List[Course] = []

# 애플리케이션 시작 시 데이터 로드
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

# CRUD API 엔드포인트
# 1. Read: 모든 강의 조회
load_data()
print(courses_data)
'''

####################################    
### 방법 2
####################################
import pandas as pd

file_path = "courses_data.csv" # 자신의 path에 맞게 설정

df = pd.read_csv(file_path, encoding='utf-8')
required_columns = ['교과목명', '개설학년', '강좌담당교수', '수업주수']
df = df[required_columns]
print(df.head())
print(df.shape)

courses_data = df.to_dict(orient='records')
print(courses_data)