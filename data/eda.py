
#  class 예제
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        # print("who.")
        return "명멍."
    
pet1 = Dog('바둑이', 5)

a = pet1.bark()

print(a)
#########################################

import pandas as pd

# CSV 파일 경로
csv_path = r'D:\2025_Fall_AI-Model-Operations-MLOps\data\courses_data.csv'
csv_path = 'courses_data.csv'

# 데이터프레임으로 읽기
df = pd.read_csv(csv_path)

# 데이터프레임 출력
# print(df)
# root 
print(df.sort_values(by='강좌담당교수', ascending=True).head()) # root

# 강좌담당교수 기준 오름차순 정렬 후 상위 5개 행 출력하는 endpoint
# 사용자로부터 강좌대표교수 이름 입력 받기
professor_name = input("강좌대표교수 이름을 입력하세요: ")

# 해당 교수의 교과목명과 수강인원 출력
result = df[df['강좌대표교수'] == professor_name][['교과목명', '개설학년', '수강인원', '수업주수', '교과목학점']]

if result.empty:
    print("해당 교수의 데이터가 없습니다.")
else:
    print(result)