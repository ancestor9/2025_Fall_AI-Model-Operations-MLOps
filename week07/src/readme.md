### 작동 흐름 요약 (MVC 패턴 기준)
1. 애플리케이션 시작:
-     database.py: DB 연결 설정(engine, SessionLocal, Base).
      models.py: 테이블 구조(DBUser)와 데이터 스키마(UserCreate, UserResponse) 정의.
      main.py: FastAPI 앱 초기화 및 테이블 생성(on_startup).

2. 클라이언트 요청 처리:
-     main.py: 엔드포인트가 요청을 받아 Depends(get_db)로 세션을 주입.
      database.py: get_db가 세션을 제공하고 요청 끝나면 자동 정리.
      crud.py: 요청에 따라 DB 작업 수행(create_user, get_users, 등).
      models.py: Pydantic 스키마로 데이터 검증 및 응답 직렬화.

3. 응답:
-     main.py: 처리된 데이터를 UserResponse 또는 리스트 형태로 클라이언트에 반환.

4. 상세 작동 mechanism

| # | 파일명           | 해당 코드                                                                             | 기능               |
| :-: | :------------ | :-------------------------------------------------------------------------------- | :--------------- |
|  1  | `database.py` | `SQLALCHEMY_DATABASE_URL:disable-run`                                             | ⚙️ 데이터베이스 연결 설정  |
|  2  | `database.py` | `SessionLocal = sessionmaker(...)`                                                | 🏭 세션 공장 준비      |
|  3  | `database.py` | `Base = declarative_base()`                                                       | 📐 테이블 설계도 틀 제작  |
|  4  | `models.py`   | `class DBUser(Base):<br>    __tablename__ = "users"`                              | 🏠 users 테이블 청사진 |
|  5  | `models.py`   | `class UserCreate(BaseModel):<br>    name: str`                                   | 📝 데이터 입력 틀 제작   |
|  6  | `main.py`     | `app = FastAPI()`                                                                 | 🚪 앱 문 열기        |
|  7  | `main.py`     | `@app.on_event("startup")<br>def on_startup():`                                   | 🔨 DB에 테이블 짓기    |
|  8  | `database.py` | `def get_db():<br>    db = SessionLocal()`                                        | 📚 세션 대출 마법      |
|  9  | `main.py`     | `@app.post("/users/", ...)<br>def create_new_user(...):`                          | 🆕 새 유저 등록       |
|  10 | `crud.py`     | `def create_user(db: Session, ...):<br>    db_user = DBUser(...)`                 | 📦 유저 상자 저장      |
|  11 | `main.py`     | `@app.get("/users/", ...)<br>def read_all_users(...):`                            | 📋 유저 목록 보여주기    |
|  12 | `crud.py`     | `def get_users(db: Session, ...):<br>    return db.query(DBUser)...`              | 📚 유저 목록 꺼내기     |
|  13 | `main.py`     | `@app.post("/fake-users/{count}", ...)<br>def generate_users(...):`               | 🎭 가짜 유저 생성      |
|  14 | `crud.py`     | `def generate_fake_users_and_save(...):<br>    fake = Faker('ko_KR')`             | 🖌️ 가짜 유저 그리기    |
|  15 | `main.py`     | `@app.put("/users/{user_id}/email", ...)<br>def update_existing_user_email(...):` | ✏️ 이메일 수정        |
|  16 | `crud.py`     | `def update_user_email(db: Session, ...):<br>    db_user = db.query(...)`         | 🔧 유저 정보 고치기     |

5. SessionLocal 클라스 / Session() 객체

| 구분     | SessionLocal (sessionmaker) | Session()              |
| ------ | --------------------------- | ---------------------- |
| 역할     | 세션 생성용 팩토리 (템플릿)            | 직접 세션 인스턴스 생성          |
| 호출 형태  | `SessionLocal()`            | `Session(bind=engine)` |
| 주 사용처  | 애플리케이션 전역 설정 (FastAPI 등)    | 임시 세션 또는 실험용 코드        |
| 설정 일관성 | 유지됨 (한 번 정의 후 반복 사용)        | 수동으로 매번 지정 필요          |
| 관리 방식  | 중앙 집중 관리 가능                 | 개별 세션 독립 관리            |

| 내용                    | 답변                                                                     |
| --------------------- | ---------------------------------------------------------------------- |
| `SessionLocal`은 무엇인가? | `Session`을 생성하는 팩토리 (sessionmaker로 만든 클래스)                             |
| `Session()`과의 차이는?    | `Session()`은 즉시 세션 객체를 생성하지만, `SessionLocal`은 설정된 템플릿을 통해 세션을 일관되게 생성함 |

