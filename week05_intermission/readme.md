## Intermission 1 (추석연휴 이후~~)
### 1. [Type : 10 Important Python Concepts In 20 Minutes](https://www.youtube.com/watch?v=Gx5qb1uHss4)
-      name: str = 'Bob'
       age: int = 15 # 'Eleven'
       print(f'{name} age is {age) years old')
-      class Fruit: 
           def __init__(self, name: str) -> None:
           self.name = name
       banana: Fruit = Fruit("banana") # 타입 힌트(banana: Fruit)를 사용하여 이 변수가 Fruit 타입임을 명시
       Fruit = Fruit("banana")
       print(banana.name, Fruit.name)
       # https://www.youtube.com/watch?v=1I3fuDR2S9A&t=193s (Dunder Methods)
-      from typing import List, Optional
       shopping_list: List[str] = ["사과", "바나나", "우유"]
       def add_item(item: str) -> None:
           shopping_list.append(item)
           print(f"✅ '{item}'이 리스트에 추가되었습니다.")
       def get_all_items() -> List[str]:
           return shopping_list
       def update_item(old_item: str, new_item: str) -> bool:
           index = shopping_list.index(old_item)
           shopping_list[index] = new_item
           return True  
       def remove_item(item: str) -> bool:
           shopping_list.remove(item)
           return True
       if __name__ == "__main__":
           print(get_all_items())
           add_item("빵"); add_item("치즈")
           print(f"현재 목록: {get_all_items()}")
           update_item("바나나", "파인애플")    
           remove_item("우유")
           print(f"최종 목록: {get_all_items()}")

### 2. if  _name_ == _main_ 구문과 module
### 3. mini project 1 : path, query에 FastAPI를 만들고 Swagger UI 대신 Gradio UI를 만들어라
- gradio_from_swagger.py
- [Mount a gradio.Blocks to an existing FastAPI application](https://www.gradio.app/docs/gradio/mount_gradio_app)
### 4. cURL은 Client URL
- URL 구문을 사용하여 데이터를 전송하기 위한 명령줄 도구 및 라이브러리(HTTP, HTTPS, FTP, SMTP 등 다양한 프로토콜을 지원하여 웹 서버와 통신하고, 데이터를 주고받는 데 사용)
- [curlconverter](https://curlconverter.com/) : FastAPI Swagg UI에서 Curl 명령어를 python으로 변경하여 확인
- [curl 명령어 수행](https://reqbin.com/curl) : : curl 명령어 수행, vscode에서 new terminal에서 >>> 변경된 pyton 코드 실행하기
### 5. mini project 2 : google ai studio에서 API Key를 발급받아 colab에서 LLM 기반 챗봇 화면을 서비스하라 
- Get_started_LLM-gemini.ipynb chat 생성하기
- gemini chat화면을 gradio로만들어 외부 url로 publish 하기
### 6. mini project 3 : gemini(LLM) ai를 활용하여 데이터를 읽고 EDA (Exploratory Data Analysis)를 외부에 배포하라
- 파일위치 : "https://raw.githubusercontent.com/ancestor9/2025_Fall_AI-Model-Operations-MLOps/main/data/courses_data.csv"
- gemini_gradio.ipynb

