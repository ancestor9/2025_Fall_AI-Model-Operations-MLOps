### 1. FastAPI Review
#### [Using FastAPI to Build Python Web APIs : self study](https://realpython.com/fastapi-python-web-apis/)

### 2. 사전학습(Python I/O 세 가지 방식) : file_operation.py
#### 2.1. Text files
#### 2.2. Buffered binary files
#### 2.3. Raw binary files
$$\text{프로그램 } (\text{str}) \xleftarrow{\text{Text I/O}} \text{버퍼} (\text{bytes}) \xleftarrow{\text{Buffered I/O}} \text{운영체제} (\text{bytes}) \xleftarrow{\text{Raw I/O}} \text{디스크}$$
-       Text I/O: 프로그래머가 f.write("안녕하세요\n") (str) 호출 --> 문자열을 바이트로 인코딩
        Buffered I/O: 인코딩된 바이트를 버퍼에 저장하고 관리 --? 버퍼가 차면 Raw I/O로 플러시
        Raw I/O: 버퍼링된 바이트 데이터를 운영체제에 전달하여 실제 디스크에 기록합니다.

- [Reading and Writing Files in Python ](https://realpython.com/read-write-files-python/)
- [Python i/o stream](https://docs.python.org/ko/3.13/library/io.html)
#### 2.4. CRUD 과제 ([sqlite3](https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial))
- shopping_list: List[str] = ["사과", "바나나", "우유"] 의 CRUD 예제(지난 주)를 sqlite3로 만들어 보기
- CRUD를 with 구문 (context manager)으로 구성하기
### 3. 과제 수행하기 
#### 3.1. 요구사항 정의
- (Requirements) sqlite3와 pydantic 을 사용하여 DB를 생성하고, 조회, 업데이트하는 fast API 코드를 생성하기
- Databae 생성하기([sqlite3](https://docs.python.org/3/contents.html)), sqlalchemy 실행

#### 3.2. 핵심 요소
- Pydantic 모델 (ItemCreate, ItemResponse): 데이터 유효성 검사 및 데이터 직렬화/역직렬화를 담당
- SQLAlchemy 모델 (Item): 데이터베이스의 테이블 구조를 정의
- 의존성 주입(Dependancy Injection) : Depends(get_db)를 사용하여 각 API 엔드포인트 함수가 호출될 때마다 독립적인 DB 세션을 자동으로 생성하고, 요청 처리가 끝난 후에는 자동으로 닫아 리소스를 정리
- CRUD 로직:
-     Create (POST): Pydantic 모델로 받은 데이터를 SQLAlchemy 모델 객체로 만들어 db.add(), db.commit()으로 저장
      Read (GET): db.query(Item).all()이나 db.query(Item).filter(...)를 사용해 데이터를 조회
      Update (PUT): 기존 객체를 조회하여 필드를 변경한 후 db.commit()으로 변경 사항을 저장

#### 3.3. 개발 방안  
##### 3.3.1. 모놀리식 아키텍쳐(Monolithic Architecture, MA)
- main_orm.py
##### 3.3.2. 마이크로 서비스 아키텍처(Microservices Architecture, MSA)
-       모듈화된 분산 구조(MVC)
        ├── main.py              # 🏠 앱 진입점 (FastAPI 인스턴스, 라우터 연결)
        ├── database.py          # ⚙️ DB 연결 및 세션 관리 (Dependency)
        ├── models.py            # 📦 Model: SQLAlchemy ORM 모델 및 Pydantic 스키마
        └── crud.py              # 🛠️ Service/Repository: DB 로직 (CRUD 함수)
