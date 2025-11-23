### Jinja2,  HTTP Request, Response
- [jinja2](https://jinja.palletsprojects.com/en/stable/api/#basics)
- jinja2_excerise.py
#### 1. main.py 파일과 FastAPI Color Generator.pdf 파일을 참고하여 시스템을 완성하기
#### 2. HTMLResponse
-     HTML 응답을 전문으로 처리하는 도구 상자(설계도) ===> class HTMLResponse
      FastAPI는 기본적으로 데이터를 JSON 형식(딕셔너리 {key: value} 형태)으로 응답하도록 설정
      하지만 우리가 웹 브라우저에 예쁜 화면(HTML)을 보여주고 싶을 때는 JSON이 아니라 HTML 코드를 보내야 함
      이때 사용하는 것이 HTMLResponse 클래스
#### 3. "FastAPI를 이용한 랜덤 색상 생성기(Random Color Generator)" 웹 애플리케이션 만들기
[How to Serve a Website With FastAPI Using HTML and Jinja2](https://realpython.com/fastapi-jinja2-template/?utm_source=rpnewsletter&utm_medium=email&utm_campaign=2025-11-21)
- [jinja-templating](https://realpython.com/primer-on-jinja-templating/)
  -     templates 폴더 > message1.txt, message2.txt, results.html, results_if.html
        jinja2_excercise.py (jinja2.py 사용은 안됨)
- [Fast API with Templates](https://fastapi.tiangolo.com/advanced/templates/)
  -     templates 폴더의 index.html, static 폴더의 style.css --> rendering
#### 4. API Router Review (optional)
- main_router_controller.py, controller 폴더
- main_request.py, main_response.py

## Ever Tried, Ever Failed ?
- React와 TypeScript에는 Jinja2와 같은 '템플릿 엔진'은 없지만, 그보다 훨씬 강력한 JSX (또는 TSX)라는 문법
-       Jinja2는 HTML 텍스트 안에 구멍을 뚫고 데이터를 채워 넣는 방식이라면, React는 JavaScript(TypeScript) 로직 자체가 HTML 구조를 만들어내는 방식
- 내가 만들고 싶은 것(my neeeds, ploblem, requirements, etc)을 정리하고 colab에서 gemini LLM 과 재미나이게 코딩(FastAPI_ngrok.ipynb)
- Google AI Studio --> Vibe Code GenAI App :
-     Scikit-learn의 Iris 예측모형을 gemini로 만들기
      FastAPI를 이용한 랜덤 색상 생성기(Random Color Generator)
- [데이터베이스_Fast API with DB](https://tech.osci.kr/fastapi-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B0%84%EB%8B%A8%ED%95%98%EA%B2%8C-%EC%9B%B9-api-%EB%A7%8C%EB%93%A4%EA%B8%B0/)
