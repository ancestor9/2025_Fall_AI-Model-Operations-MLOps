'''
https://fastapi.tiangolo.com/ko/learn/
FastAPI를 배우기 위한 입문 자료
'''

# def get_full_name(first_name, last_name):
#     full_name = first_name.title() + " " + last_name.title()
#     return full_name


# print(get_full_name("john", "doe"))

#### 동기 부여

def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))

def get_name_with_age(name: str, age: int):
    # name_with_age = name + " is this old: " + age
    name_with_age = name + " is this old: " + str(age)
    return name_with_age

print(get_name_with_age("조상", 25))

#######
#bytes는 파일, 네트워크 데이터 등과 같은 이진 데이터를 다룰 때 사용하고, str은 텍스트 데이터를 다룰 때 사용
#######
def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e

print(get_items("apple", 3, 3.5, True, b"hello"))


def get_items_01(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: str):
    return item_a, item_b, item_c, item_d, item_d, item_e

print(get_items_01("apple", 3, 3.5, True, "hello"))

######

# from typing import List

# def process_items(items: List[str]):
#     for item in items:
#         print(item)
        
# process_items(["apple", "banana", "cherry"])

#######
from typing import Dict


def process_items(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)
        
process_items({"apple": 0.99, "banana": 0.59, "cherry": 2.99})

#######
from typing import Optional

def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")
        
say_hi("Alice")
say_hi()
########

class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name

print(get_person_name(Person("Bob")))

#####
from datetime import datetime
from typing import List, Union

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: Union[datetime, None] = None
    friends: List[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)

print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123


'''
과제 : course_data.csv 파일을 읽어서
각 행을  , 리스트에 저장하고 출력하세요.
'''
## 과제 수행
import pandas as pd
from typing import List
from pydantic import BaseModel

df = pd.read_csv("D:\python\evertrial\courses_data.csv")
# print(df)
print(df.columns)
ef = df[['교과목명', '개설학년', '영역구분', '수강인원',  '강좌담당교수', '수업주수', '교과목학점']]
# print(ef)
ef.dropna(inplace=True)
print(ef)
print(ef.isnull().sum())

from pydantic import BaseModel, Field, conint, confloat, constr
from typing import Optional

class Course(BaseModel):
    교과목명: Optional[str] = None
    개설학년: Optional[int] = None
    영역구분: Optional[str] = None
    수강인원: Optional[int] = None
    강좌담당교수: Optional[str] = None
    수업주수: Optional[int] = None
    교과목학점: Optional[int] = None
    
# 3. 데이터프레임의 각 행을 Pydantic 모델 객체로 변환
courses_list = [Course(**row) for row in ef.to_dict('records')]

# 4. Pydantic 모델 리스트를 JSON 형태로 변환
# `json()` 메서드는 모델을 JSON 문자열로 변환합니다.
# `model_dump_json()` 메서드는 Pydantic v2에서 사용됩니다.
# `indent=2`를 사용하여 가독성을 높입니다.
json_output = [course.model_dump_json(indent=2) for course in courses_list[:5]]

# 결과 출력
for item in json_output:
    print(item)