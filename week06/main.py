'''
MVC (Model-View-Controller) 패턴은 웹 애플리케이션의 코드를 책임에 따라 나누어 관리하기 위한 디자인 패턴
FastAPI는 전통적인 웹 프레임워크와 달리 'View'에 해당하는 부분이 명확하지 않지만, 일반적으로 다음과 같이 코드를 모듈화
- Model: 데이터의 구조와 로직 (SQLAlchemy ORM 모델, Pydantic 스키마)
- Controller: 요청을 받고 응답을 처리하는 로직 (FastAPI 라우트 함수)
- Database/Service: 데이터베이스 연결, 세션 관리, CRUD 로직 (데이터베이스 의존성, CRUD 함수)
- 디렉토리 구조:
├── main.py              # 🏠 앱 진입점 (FastAPI 인스턴스, 라우터 연결)
├── database.py          # ⚙️ DB 연결 및 세션 관리 (Dependency)
├── models.py            # 📦 Model: SQLAlchemy ORM 모델 및 Pydantic 스키마
└── crud.py              # 🛠️ Service/Repository: DB 로직 (CRUD 함수)
'''