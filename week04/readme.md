### 4.1. http 구조 Review
#### 4.1.1. http request 구조 (Client ----request----> Server)
![](https://blog.kakaocdn.net/dna/bUk1MH/btqD9Nwa5bh/AAAAAAAAAAAAAAAAAAAAAHzhVOCLZG0zt7QsnMifVgZPSZI5_n7VfcjEdRimpyAK/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1759244399&allow_ip=&allow_referer=&signature=CLilKKunbdDDtC1W6SJJRWEZ1Nw%3D)
#### 4.3.2. http response 구조 (Client <----response----- Server)
![](https://blog.kakaocdn.net/dna/B1ncV/btsEWyvMlHw/AAAAAAAAAAAAAAAAAAAAAL45lRSwnfiECq9bA3maLS9bNvJKyTAdK1qRYhj5CdIk/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1759244399&allow_ip=&allow_referer=&signature=4W7bFYDbL3y%2BtTjTYJAu2voD%2F2Y%3D)

#### 4.2. Ever Tried, Ever Failed ?
- 내가 만들고 싶은 것(my neeeds, ploblem, requirements, etc)을 정리하고 colab에서 gemini LLM 과 재미나이게 코딩
- py 파일로 다운로드
- MVC 개념으로 파일을 나누기
- "evertrail" 폴더 전체적인 구조 이해하기
- Getting Started with Fast API

#### 4.3. Fast API 시작
- 가상환경 생성과 Fast API 설치(웹서버 uvicorn) -> Optional

- Path와 Query Parameter 이해
-     REST API 설계 시 path는 “무엇(리소스)”을 요청하는지, query는 “어떻게(조건, 옵션)”을 요청하는지 전달하는 방식으로 구분해 활용
- Pydantic 모듈 (Request Body, POST Method)
