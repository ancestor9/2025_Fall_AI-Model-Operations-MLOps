#### 4.1. Modern Web
- pdf 참고(1. Modern Web.pdf)
- http 구조 Review
- 4.1. http request 구조 (Client ----request----> Server)
![](https://blog.kakaocdn.net/dna/bUk1MH/btqD9Nwa5bh/AAAAAAAAAAAAAAAAAAAAAHzhVOCLZG0zt7QsnMifVgZPSZI5_n7VfcjEdRimpyAK/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1759244399&allow_ip=&allow_referer=&signature=CLilKKunbdDDtC1W6SJJRWEZ1Nw%3D)
- 4.2. http response 구조 (Client <----response----- Server)
![](https://blog.kakaocdn.net/dna/B1ncV/btsEWyvMlHw/AAAAAAAAAAAAAAAAAAAAAL45lRSwnfiECq9bA3maLS9bNvJKyTAdK1qRYhj5CdIk/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1759244399&allow_ip=&allow_referer=&signature=4W7bFYDbL3y%2BtTjTYJAu2voD%2F2Y%3D)

#### 4.2. Fast API 시작
- FastAPI 맛보기 : 왜 필요한가? ----> Firebase Studio에서 VIBE 코딩
-          - Firebase는 모바일 및 웹 애플리케이션을 개발하기 위한 구글의 플랫폼
  [Firebase](https://www.youtube.com/watch?v=A1Ix7xzjtkM)
- 가상환경 생성과 Fast API 설치(웹서버 uvicorn) -> Optional
-          - FastAPI framework: pip install fastapi
           - Uvicorn web server: pip install uvicorn
           - HTTPie text web client: pip install httpie
           - Requests synchronous web client package: pip install requests
           - HTTPX sync/async web client package: pip install httpx
### Requests (Client)
#### 4.2.1.  Path와 Query Parameter 이해
-     REST API 설계 시 path는 “무엇(리소스)”을 요청하는지, query는 “어떻게(조건, 옵션)”을 요청하는지 전달하는 방식으로 구분해 활용
#### 4.3.2.  Request Body, Head
-     사전형, JSON, Pydantic 모듈 (Request/Response Body, POST Method), 여러 개 Request Body
