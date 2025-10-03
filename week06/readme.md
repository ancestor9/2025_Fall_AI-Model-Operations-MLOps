### sqlite3와 pydantic 을 사용하여 DB를 생성하고, 조회, 업데이트하는 fast API 코드를 생성하기
#### 1. Monolithiv file 구조
- main_orm.py
#### 2. MVC 구조
-
- ├── main.py              # 🏠 앱 진입점 (FastAPI 인스턴스, 라우터 연결)
- ├── database.py          # ⚙️ DB 연결 및 세션 관리 (Dependency)
- ├── models.py            # 📦 Model: SQLAlchemy ORM 모델 및 Pydantic 스키마
- └── crud.py              # 🛠️ Service/Repository: DB 로직 (CRUD 함수)
