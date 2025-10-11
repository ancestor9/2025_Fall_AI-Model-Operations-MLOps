## Intermission 1 (추석연휴 이후~~)
### 1. [Type : 10 Important Python Concepts In 20 Minutes](https://www.youtube.com/watch?v=Gx5qb1uHss4)
-      name: str = 'Bob'
       age: int = 'Eleven'
       print(f'{name}' age is {age) years old')
-      from typing import List, Optional
       shopping_list: List[str] = ["사과", "바나나", "우유"]
       def add_item(item: str) -> None:
           shopping_list.append(item)
           print(f"✅ '{item}'이 리스트에 추가되었습니다.")
       def get_all_items() -> List[str]:
           return shopping_list
       def get_item_by_index(index: int) -> Optional[str]:
           return shopping_list[index]
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
           item_at_index_0 = get_item_by_index(0)
           print(f"인덱스 0의 항목: {item_at_index_0}")
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
### 7. mini project 4 : Gradio와 FastAPI 별도 서버
- (모델학습 및 저장) train_model.py: 모델을 학습시키고 에측모형을 *.pkl 파일로 저장
- (백엔드) api.py: FastAPI 백엔드 (저장된 모델을 로드하여 API 제공)
- (프론트엔드) app_gradio.py: Gradio 프론트엔드 (API 호출을 통해 사용자 인터페이스 제공)
- (외부 배포) To create a public link, set `share=True` in `launch()

| 구분              | 파일명          | 역할                           | 실행 주소 (기본 포트)      | 핵심 엔드포인트 / 함수       | 설명                                                                 |
|-------------------|----------------|--------------------------------|----------------------------|-------------------------------|----------------------------------------------------------------------|
| 백엔드 (서버)     | api.py         | FastAPI 서버 (모델 서빙)       | http://127.0.0.1:8000      | POST /predict/                | - 저장된 붓꽃 예측 모델(iris_model.pkl) 로드<br>- 입력 특성(sl, sw, pl, pw) 처리<br>- 예측 결과를 JSON 형태로 반환 |
| 프론트엔드 (클라이언트) | app_gradio.py   | Gradio 인터페이스 (UI/UX)      | http://127.0.0.1:7860      | predict_species()              | - 사용자에게 슬라이더 입력 제공<br>- FastAPI 서버(/predict) 호출<br>- 예측 결과를 UI에 표시 |
| 연결 URL          | app_gradio.py   | requests 모듈                  | http://127.0.0.1:8000/predict/ | requests.post(FASTAPI_URL, ...) | - Gradio 클라이언트가 FastAPI 서버에 데이터 전송<br>- API 호출을 통해 예측 요청 수행 |

### 8. mini project 5 : 단일 서버
- 🚀 Gradio Mount 통합 간결 코드 (main_gradio_mount.py) :
-     train_model.py를 먼저 실행하여 iris_model.pkl 파일이 생성되어 있다는 가정 하에 작동
      브라우저 주소창에 http://127.0.0.1:8000/api/predict  접근하는 것은 기본적으로 GET HTTP 메소드를 사용하면
      정의된 것이 없거나 허용되지 않았기 때문에 405 Method Not Allowed 오류를 반환하며, JSON으로 {"detail":"Method Not Allowed"}를 표시
      FastAPI swagger 혹은 http://127.0.0.1:8000/gradio/ 에서 POST 메소드 실행하면 됨

