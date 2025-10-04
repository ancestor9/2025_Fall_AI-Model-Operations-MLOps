### 요구사항 정의
- (Requirements) sqlite3와 pydantic 을 사용하여 DB를 생성하고, 조회, 업데이트하는 fast API 코드를 생성하기
- Databae 생성하기(sqlite3), sqlalchemy 실행
- [DBeaver 다운로드하여 조회하기](https://dbeaver.io/)

### 핵심 요소
- Pydantic 모델 (ItemCreate, ItemResponse): 데이터 유효성 검사 및 데이터 직렬화/역직렬화를 담당
- SQLAlchemy 모델 (Item): 데이터베이스의 테이블 구조를 정의
- 의존성 주입(Dependancy Injection) : Depends(get_db)를 사용하여 각 API 엔드포인트 함수가 호출될 때마다 독립적인 DB 세션을 자동으로 생성하고, 요청 처리가 끝난 후에는 자동으로 닫아 리소스를 정리
- CRUD 로직:
-     Create (POST): Pydantic 모델로 받은 데이터를 SQLAlchemy 모델 객체로 만들어 db.add(), db.commit()으로 저장
      Read (GET): db.query(Item).all()이나 db.query(Item).filter(...)를 사용해 데이터를 조회
      Update (PUT): 기존 객체를 조회하여 필드를 변경한 후 db.commit()으로 변경 사항을 저장

### 개발 방안  
#### 1. 모놀리식 아키텍쳐(Monolithic Architecture, MA)
- main_orm.py
#### 2. 마이크로 서비스 아키텍처(Microservices Architecture, MSA)
-       모듈화된 분산 구조(MVC)
        ├── main.py              # 🏠 앱 진입점 (FastAPI 인스턴스, 라우터 연결)
        ├── database.py          # ⚙️ DB 연결 및 세션 관리 (Dependency)
        ├── models.py            # 📦 Model: SQLAlchemy ORM 모델 및 Pydantic 스키마
        └── crud.py              # 🛠️ Service/Repository: DB 로직 (CRUD 함수)
