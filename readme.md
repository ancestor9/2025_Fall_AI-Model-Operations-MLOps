## 교과목 내용
### 5번의 실습과제, 기말과제(교과목/강의실 재정 알고리즘) 제출 및 발표
| 주차 | 핵심 내용 |
|:----:|:-----------|
| 1주차 | 네트워크 기초와 Python 사용 이유에 대한 설명.<br>LLM에 질문하기를 통해 IP 주소, Wi-Fi, TCP/UDP, 소켓 프로그래밍 등 네트워크 기본 개념 학습. |
| 2주차 | 함수, 모듈, 라이브러리, 패키지 복습.멀티쓰레드/멀티프로세싱 이해 실습<br>파이썬 http.server를 사용한 간단한 웹 서버(Web Server) 구현 및 이해. |
| 3주차 | 네트워크 암호화 (SSL/TLS, 인코딩/디코딩, RSA 실습) 학습.<br>HTTP Request Message 구성과 MVC(Model-View-Controller) 디자인 패턴 이해. |
| 4주차 | Modern Web 및 HTTP 구조 (Request Line, Headers, Body) 복습.<br>FastAPI 시작을 위한 환경 설정 (가상환경, FastAPI/uvicorn), Path, Query, Header, Body 및 Router 이해|
| 5주차 | FastAPI 기본 (Path, Query, Header, Body) 및 Router 복습.<br>CRUD, Pydantic, File I/O, Server-Client 구조, CRUD 함수 (추가, 조회, 수정, 삭제) 구현. |
| 6주차 | Front End UI gradio와 Fast API, 병렬서버운영과 단독서버 운영하기|
| 6주차_하브루타 | Iris 데이터로 scikitlearn 분류모델로 예측, 예측모형을 저장하여 FastAPI를 벡엔드로 gradio UI에서 입력데이터를 바탕으로 예측하기 실습|
| 7주차 |  Python I/O (Text, Buffered, Raw binary files) 세 가지 방식 stream 객체 실습, File=Socket, sqlite3를 이용한 CRUD 실습 진행, Dependency Injection |
| 7주차_하브루타 | Microsoft Builder AdventuresSales 데이터를 바탕으로 시각화 하기 |
| 8주차 | Streamlit UI + FastAPI, data_cache, session, ngrok, Monolithic/Microservices 아키텍처 설명. |
| 8주차_하부르타 | ChinookDB 바탕으로 혹은 도서관관리시스템 만들기 MVC, Monolithic/Microservices 아키텍처 실습. |
| 9주차 | Streamlit (Front End)과 FastAPI (Back End) 연동 구조 시각화.<br>sqlite3 CRUD 기능을 Streamlit UI로 구현하는 과제, 인증과 인가 방식(supabase), https://www.youtube.com/watch?v=OJIR1pA7Ceo&si=5Y6Vw3drbFRhXHX_, https://www.youtube.com/watch?v=ip87CHxtoJY&si=rOaVfFoxhIx5UmcQ |
| 10주차 | API Router Review와 HTTP Request/Response 심화.<br>Jinja2 템플릿, Bootstrap, FastAPI with DB 및 ngrok을 사용한 외부 접속 방법 학습. |

## 주요 내용
#### 1. 네트워크 통신 (9시간)
-     HTTP, TCP/IP, Client-Server Architecture, - socket (IP + port),
#### 2. FAST API (25시간)
-     Modern Web Architecture : Fast API, Database(sqlite3) & gradio with ngrok
      Github에 제출할 Homeworks
-     - homework_01: 고객(성명, 연령, 주소, 전화번호)과 상품(상품명, 가격, 설명 등) 정보를 사전형으로 생성하고
        '/'에는 모든 정보를 조회하고, '/customers' 혹은 '/products'에서는 정보의 검색 가능
      - homework_02: 고객이 온라인 상품에 대해 가격 견적을 요청하면 세금 10%를 포함한 세후 가격을 제시
      Mini project 1 (데이터수집-분석-예측, scikit-learn의 toy data로 예측 웹 서비스 만들기 등)
#### 3. 생성형 AI로 chatbot 만들기 (11시간)
-      Deep Learning, LLM API 개발 이해 --> Mini project (LLM을 이용한 서비스 만들기)
#### 4. 기말 과제 제출 (~11.17)
-     교과목과 실습실 배정 및 시각화(학점 60%)
      배정 알고리즘(선형계획법, 유전자알고리즘 등) 개발과 FastAPI로 웹 서비스
- [Opal로 구현 예제](https://opal.google/?flow=drive:/14_wnmShL2IKED5HJxbeYVhXDfALrGyH2&shared&mode=app)
- [교과목/강의실 배정 알고리즘](https://github.com/ancestor9/2025_Fall_AI-Model-Operations-MLOps/blob/main/%EA%B0%95%EC%9D%98%EC%8B%A4%EB%B0%B0%EC%A0%95_%EC%A0%95%EC%88%98%EA%B3%84%ED%9A%8D%EB%B2%95.ipynb)
   
#### 참고 자료
![](https://www.oreilly.com/covers/urn:orm:book:9781098135492/400w/)
- [Essential Math for Data Science, Thomas Nield, O'RELLY](http://103.203.175.90:81/fdScript/RootOfEBooks/E%20Book%20collection%20-%202024%20-%20F/CSE%20%20IT%20AIDS%20ML/Essential_Math_for_Data_Science_Take_Control_of_Your_Data_with_Fundamental.pdf)
- [Dimension Reduction](https://dimensionality-reduction-293e465c2a3443e8941b016d.vercel.app/)
- [Transformer](https://poloclub.github.io/transformer-explainer/)
- [CNN](https://poloclub.github.io/cnn-explainer/)
