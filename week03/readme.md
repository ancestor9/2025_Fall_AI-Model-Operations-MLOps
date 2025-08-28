## 3주차에 배울 내용
### 1. 암호화
- SSL (Secure Sockets Layer), TLS (Transport Layer Security)
- Encoding, Decoding, [rsa online 알고리즘 실습](https://www.devglan.com/online-tools/rsa-encryption-decryption)

### 2. SSL/TLS 동작 방식 (핸드셰이크 과정)
- TLS 연결을 맺을 때 핸드셰이크(Handshake) 절차가 있음. (단순화 버전)
- 클라이언트 Hello
- 브라우저가 서버에 "TLS를 쓰자" 요청, 지원 가능한 암호화 알고리즘 목록 전달.
- 서버 Hello
- 서버가 사용할 암호화 방식 선택.
- 서버 인증서(공개키 포함)를 클라이언트에게 전달.
- 인증서 검증
- 클라이언트는 서버 인증서를 CA(인증기관) 공개키로 검증.
- 올바른 서버인지 확인.
- 대칭키 공유
- 클라이언트와 서버가 세션키(대칭키)를 교환하거나 Diffie-Hellman 방식으로 생성.
- 암호화된 통신 시작
- 이후 데이터는 모두 세션키로 암호화하여 통신.

### 2. MVC (Model-View-Controller) 패턴이란?
- 소프트웨어 공학에서 사용되는 **모델-뷰-컨트롤러(Model-View-Controller)**라는 디자인 패턴
- 애플리케이션의 데이터(모델), 사용자 인터페이스(뷰), 그리고 데이터와 뷰 사이의 논리 및 흐름을 제어하는(컨트롤러) 세 부분으로 나누는 방법

<img src="https://tecoble.techcourse.co.kr/static/c73f913a7c220ec8cb3ee9a8579468b4/73a7d/mvc.avif" width="600" height="500">
        - source : https://tecoble.techcourse.co.kr/post/2021-04-26-mvc/

<img src="https://www.simform.com/wp-content/uploads/2021/05/webapparchitecture5.png" width="800" height="600">
        - source: https://www.simform.com/blog/web-application-architecture/

## 3. Fast API
- https://fastapi.tiangolo.com/ko/
