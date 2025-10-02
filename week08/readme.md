### 💡 FastAPI와 MVC 패턴을 활용한 RESTful API 구현 과제
- 본 과제는 고성능 웹 프레임워크인 FastAPI를 사용하여 MVC (Model-View-Controller) 패턴의 원칙을 적용하고,
- ORM 없이 순수 SQL과 Pandas를 활용하여 기본적인 CRUD (Create, Read, Update, Delete) 기능을 구현하는 것을 목표

#### 📝 과제 목표
- 모듈화 학습: 애플리케이션의 각 계층(Model, Service, Router)을 별도의 Python 모듈로 분리하여 코드의 재사용성과 유지보수성을 높인다.
- FastAPI 기본기 숙달: FastAPI의 APIRouter, Pydantic Model, Dependency Injection (DI) 등 핵심 기능을 이해하고 적용한다.
- 데이터베이스 기초: ORM 없이 Python의 기본 라이브러리인 sqlite3를 사용하여 데이터베이스 CRUD 작업을 직접 수행한다.
- 데이터 처리: Pandas를 사용하여 외부 파일(PSV)로부터 데이터를 효율적으로 읽어 초기 데이터베이스를 구성하는 방법을 습득한다.

#### 프로젝트 구성 정보

| **항목**         | **내용**                              |
|-------------------|---------------------------------------|
| **프레임워크**   | FastAPI (ASGI 프레임워크)            |
| **서버**        | Uvicorn (ASGI 서버)                  |
| **데이터베이스** | SQLite3 (Python 기본 내장)           |
| **데이터 처리**  | Pandas (외부 데이터 파일 로딩)        |
| **아키텍처**    | Model-Service-Router (MVC 패턴의 변형) |
| **초기 데이터**  | creatures.psv, explorers.psv         |
