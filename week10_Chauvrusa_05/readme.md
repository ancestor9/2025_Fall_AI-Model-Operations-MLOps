### 가장 최소한의 기능만 갖춘 FastAPI 백엔드와 HTML/JavaScript 프론트엔드를 사용하여 Gemini 챗봇을 구현하는 모듈화된 코드를 제시합니다.

- main_gemini.py: FastAPI 백엔드 (Gemini API 호출 처리)
-       index.html: HTML 프론트엔드 (사용자 인터페이스 및 API 호출)
- gemini_client.py: Gemini API 로직 모듈화

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


### Extra code:
- [google ADK: AI 에이전트를 개발/배포하기 위한 유연/모듈화된 오픈소스 프레임워크](https://google.github.io/adk-docs/get-started/python/)
-     1. 가상환경 만들기 (python -m venv myenv)
      2. AKD 인스톨하기 (pip install google-adk)
      3. 프로젝트만들기 (adk create my_agent)
      4. model ='gemini-2.5-flash'를 사용하여 동작하기, CLI / Web 환경에서
- [구글 ADK (Agent Development Kit) 10분만에 이해하기! LangGraph 대항마일까?](https://www.youtube.com/watch?v=iZdqqv-dIYU&t=309s)

