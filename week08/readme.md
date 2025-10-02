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

| 계층 | 파일 / 구성 요소 | 주요 역할 | 세부 권고사항 |
|------|----------------|----------|--------------|
| Model (models/) | creature.py, explorer.py | 데이터 구조 정의 | Pydantic 사용<br>세 가지 모델 클래스 구분: Base (기본 구조), Create (입력), Get (출력/ID 포함)<br>모든 필드에 Python 타입 힌트 및 Optional 명시 |
| Data (data/) | psv_loader.py | PSV 파일 로딩 | pandas.read_csv로 '|' 구분자 PSV 파일 읽기<br>DataFrame → List[Dict] 변환<br>결측치는 None으로 변환해 SQLite NULL 대응 |
|  | database.py | DB 연결 및 초기화 | sqlite3 모듈 사용<br>get_db_connection(): Generator(yield)로 구현 → FastAPI DI 지원, 요청 후 자동 close(finally)<br>initialize_db(): psv_loader 호출 → 데이터 로드, CREATE TABLE IF NOT EXISTS, 초기 데이터 삽입 |
| Service (services/) | Service 클래스들 | 비즈니스 로직 및 CRUD 처리 | SQLAlchemy 등 ORM 사용 금지<br>sqlite3.Connection 직접 사용<br>SQL 쿼리 직접 작성 (SELECT, INSERT, UPDATE, DELETE)<br>모든 함수에 타입 힌트 명시 (예: List[Creature], Optional[Explorer]) |
| Router (routers/) | creature.py, explorer.py | API 엔드포인트 정의 | APIRouter 사용, 경로 분리 및 태그 명시<br>모든 엔드포인트 함수는 get_db_connection을 Depends로 주입 |
| CRUD 매핑 | RESTful API 설계 | 엔드포인트 매핑 | Create: POST /resources/ → 201 Created<br>Read (All): GET /resources/<br>Read (One): GET /resources/{id} → 없으면 404 Not Found<br>Update: PUT /resources/{id}<br>Delete: DELETE /resources/{id} → 204 No Content<br>예외 처리: HTTPException(status_code=404), IntegrityError(중복 이름 등) 처리 |




#### 4. FastAPI 권장 구조
project-root/
│── main.py                     # FastAPI 실행 진입점
│── requirements.txt            # 의존성 패키지 (pandas, fastapi, uvicorn 등)
│
├── models/                     # Pydantic 모델 정의
│   ├── creature.py             # Creature 모델 (Base, Create, Get)
│   └── explorer.py             # Explorer 모델 (Base, Create, Get)
│
├── data/                       # 데이터 계층
│   ├── psv_loader.py           # PSV 파일 로더 (| 구분자, None 변환)
│   └── database.py             # DB 연결 관리 및 초기화
│
├── services/                   # 서비스 계층 (비즈니스 로직)
│   ├── creature_service.py     # Creature 관련 CRUD 서비스
│   └── explorer_service.py     # Explorer 관련 CRUD 서비스
│
├── routers/                    # 라우터 계층 (API 엔드포인트)
│   ├── creature.py             # Creature 라우터 (CRUD 엔드포인트)
│   └── explorer.py             # Explorer 라우터 (CRUD 엔드포인트)
│
└── tests/                      # 테스트 코드
    ├── test_creature.py
    └── test_explorer.py


