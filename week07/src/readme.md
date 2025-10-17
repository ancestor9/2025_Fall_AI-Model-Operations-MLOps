|  순서 | 파일명           | 해당 코드                                                                             | 기능               |
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

