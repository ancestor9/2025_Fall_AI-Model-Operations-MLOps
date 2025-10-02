### 💡 FastAPI와 MVC 패턴을 활용한 RESTful API 구현 과제
- 본 과제는 고성능 웹 프레임워크인 FastAPI를 사용하여 MVC (Model-View-Controller) 패턴의 원칙을 적용하고,
- ORM 없이 순수 SQL과 Pandas를 활용하여 기본적인 CRUD (Create, Read, Update, Delete) 기능을 구현하는 것을 목표

#### 1. 과제 목표
- 모듈화 학습: 애플리케이션의 각 계층(Model, Service, Router)을 별도의 Python 모듈로 분리하여 코드의 재사용성과 유지보수성을 높인다.
- FastAPI 기본기 숙달: FastAPI의 APIRouter, Pydantic Model, Dependency Injection (DI) 등 핵심 기능을 이해하고 적용한다.
- 데이터베이스 기초: ORM 없이 Python의 기본 라이브러리인 sqlite3를 사용하여 데이터베이스 CRUD 작업을 직접 수행한다.
- 데이터 처리: Pandas를 사용하여 외부 파일(PSV)로부터 데이터를 효율적으로 읽어 초기 데이터베이스를 구성하는 방법을 습득한다.

#### 2. 프로젝트 구성 정보

| **항목**         | **내용**                              |
|-------------------|---------------------------------------|
| **프레임워크**   | FastAPI (ASGI 프레임워크)            |
| **서버**        | Uvicorn (ASGI 서버)                  |
| **데이터베이스** | SQLite3 (Python 기본 내장)           |
| **데이터 처리**  | Pandas (외부 데이터 파일 로딩)        |
| **아키텍처**    | Model-Service-Router (MVC 패턴의 변형) |
| **초기 데이터**  | creatures.psv, explorers.psv         |


#### 3. 작성 가이드 및 핵심 요구사항

- 1. Model 계층 (models/)
Pydantic 사용: creature.py와 explorer.py 파일에 각각의 데이터 구조를 정의
세 가지 모델: 데이터의 목적에 따라 **Base (기본 구조), Create (입력), Get (출력/ID 포함)**의 세 가지 클래스로 분리 권고
타입 힌트: 모든 필드에 정확한 Python 타입 힌트와 Optional을 명시

- 2. Data 계층 (data/)
-        psv_loader.py: pandas.read_csv를 사용하여 | 구분자로 PSV 파일을 읽고, DataFrame을 Python 딕셔너리 리스트(List[Dict])로 변환하여 반환
         (결측치)는 **None**으로 변환하여 SQLite NULL 값에 대응
-      database.py: sqlite3 모듈을 사용하여 데이터베이스 연결을 관리
       get_db_connection() 함수는 FastAPI의 **의존성 주입(DI)**을 위해 Generator (yield)를 사용하며, 요청 처리 후 연결이 자동으로 닫히도록 (finally) 구현
       initialize_db() 함수는 psv_loader를 호출하여 데이터를 로드하고, CREATE TABLE IF NOT EXISTS 구문을 사용하여 테이블을 생성하며, 초기 데이터를 삽입
   
- 3. Service 계층 (services/)
-      비즈니스 로직 분리: 데이터 처리 및 CRUD 로직은 Service 클래스 내부에 캡슐화
       순수 SQL 사용: ORM (SQLAlchemy 등)을 일절 사용하지 않고 sqlite3.Connection 객체를 받아 직접 SQL 쿼리 (SELECT, INSERT, UPDATE, DELETE)를 작성
       타입 지정: 모든 함수는 입력 파라미터와 반환 값에 대한 명확한 타입 힌트(List[Creature], Optional[Explorer] 등)를 명시

4. Router 계층 (routers/)
-     FastAPI APIRouter: creature.py와 explorer.py에서 각각 APIRouter를 생성하여 경로를 분리하고 태그를 명시
      의존성 주입: 모든 엔드포인트 함수는 data/database.py의 get_db_connection을 **Depends**로 받아 데이터베이스 연결

5. CRUD 매핑: 각 엔드포인트는 다음 HTTP 메서드에 매핑 권고
- Create: POST /resources/ (201 Created)
- Read (All): GET /resources/
- Read (One): GET /resources/{id} (404 Not Found 처리 필수)
- Update: PUT /resources/{id}
- Delete: DELETE /resources/{id} (204 No Content)
- 예외 처리: 데이터가 없을 경우 (Read, Update, Delete) **HTTPException(status_code=404)**를 반환해야 하며 IntegrityError (중복 이름 등)에 대해서도 처리

