## 3주차에 배울 내용
### 1. 네트워크 암호화
- SSL (Secure Sockets Layer), TLS (Transport Layer Security)
- Encoding, Decoding, [rsa online 알고리즘 실습](https://www.devglan.com/online-tools/rsa-encryption-decryption)
- 대칭키와 비대팅키(공개키 + 비밀키)
- SSL/TLS 동작 방식 (핸드셰이크 과정)

### 2. HTTP Request Message 구성 및 HTTP 메소드

### 3. MVC (Model-View-Controller) 패턴이란?
- 소프트웨어 공학에서 사용되는 **모델-뷰-컨트롤러(Model-View-Controller)**라는 디자인 패턴
- 애플리케이션의 데이터(모델), 사용자 인터페이스(뷰), 그리고 데이터와 뷰 사이의 논리 및 흐름을 제어하는(컨트롤러) 세 부분으로 나누는 방법

<img src="https://tecoble.techcourse.co.kr/static/c73f913a7c220ec8cb3ee9a8579468b4/73a7d/mvc.avif" width="600" height="500">

- Can you recognize model, view, controller in the below playing Logo picture? 

![](https://images.unsplash.com/photo-1575364289437-fb1479d52732?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fCVFQiU4NiU4MCVFQiU4QiVBNHxlbnwwfHwwfHx8MA%3D%3D)

### 3. Modern Web Architecture
<img src="https://www.simform.com/wp-content/uploads/2021/05/webapparchitecture5.png" width="600" height="500">

## 4. Fast API
- https://fastapi.tiangolo.com/ko/
- 사전 지식
  . Decorator 함수 : 다른 함수를 wrapping하는 함수
  . if __name__ == __main__
- 가상환경 생성과 Fast API 설치(웹서버 uvicorn)
- Fast API 시작
- Path와 Query Parameter 이해
-     REST API 설계 시 path는 “무엇(리소스)”을 요청하는지, query는 “어떻게(조건, 옵션)”을 요청하는지 전달하는 방식으로 구분해 활용
- Pydantic 모듈 (Request Body, POST Method)
