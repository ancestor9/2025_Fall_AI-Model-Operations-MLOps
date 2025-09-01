## 2주차 학습 내용
## 1. 웹서버(Web Server)
### 1.1. 파이썬 http server 이해 및 작동
- 클라이언트(사용자 브라우저 등)로부터 요청을 받아 웹 페이지나 데이터를 응답하는 소프트웨어 또는 하드웨어 시스템
- 사용자가 주소창에 URL을 입력했을 때 웹 서버가 해당 요청을 처리해 결과(HTML, 이미지, JSON 등)를 돌려주는 역할
- 실습 : "간단한 HTML을 만들고 comand창에서 http server로 작동" @ VSCODE
                - from http.server import HTTPServer, SimpleHTTPRequestHandler
                - # 8000번 포트에서 실행되는 간단한 웹서버
                - server = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
                - print("웹서버 실행 중: http://localhost:8000")
                - server.serve_forever()

  
## 2. 병렬성(Parallelism) 과 동시성(Concurrency)
### 2.1. 멀티쓰레드(multithread)
- (quest) 멀티쓰레드(multithread)를 설명해줘. TCP IP방식으로 client server 아키텍쳐로 예제 코드를 주고 주석과 함께 동작방식을 알려줘

📌 멀티쓰레드(multithread)란?
- 하나의 프로세스 안에서 여러 개의 실행 단위를 동시에 실행하는 방식.
- 서버 프로그램에서는 여러 클라이언트가 동시에 접속할 때 멀티쓰레드를 사용하면, 각 클라이언트 요청을 별도의 쓰레드에서 처리할 수 있음.
- 즉, 서버가 한 클라이언트 요청만 처리하지 않고, 동시에 여러 클라이언트를 대응할 수 있게 해줌.
  
📌 TCP/IP Client-Server 구조
- Server :
> socket()으로 서버 소켓 생성 > bind()로 IP와 Port 연결 > listen()으로 클라이언트 접속 대기 > accept()로 클라이언트 연결 수락 > 클라이언트가 연결되면 새로운 쓰레드를 만들어 해당 클라이언트 전담 처리
- Client
> socket()으로 클라이언트 소켓 생성 > connect()로 서버에 연결 요청 > 서버와 메시지를 송수신


### 2.2. 멀티프로세싱(multiprocessing)
- (quest) 멀티프로세싱(multiprocessing)를 설명해줘. TCP IP방식으로 client server 아키텍쳐로 예제 코드를 주고 주석과 함께 동작방식을 알려줘.

📌 멀티프로세싱(multiprocessing)이란?
- 멀티프로세싱은 하나의 프로그램에서 여러 개의 프로세스를 동시에 실행시키는 방식
- 각 프로세스는 독립된 메모리 공간을 가지며, CPU의 여러 코어를 활용할 수 있기 때문에 병렬 처리가 가능
- 멀티스레딩(multithreading)과 달리, GIL(Global Interpreter Lock)의 제약을 받지 않아 CPU 집약적인 작업에 유리
- TCP/IP 기반 서버에서 다수의 클라이언트가 동시에 접속할 경우, 프로세스를 분기(fork)시켜 각 클라이언트와 독립적으로 통신
- 
📌 동작 방식(파이썬코드 참고)
- 서버 시작 : 서버는 포트 5000에서 클라이언트 연결 대기
- 클라이언트 접속 : 클라이언트가 서버에 접속하면 accept()로 연결을 수락
- 프로세스 생성 : multiprocessing.Process를 통해 새로운 프로세스를 생성하고, 해당 프로세스에서 handle_client()가 실행
- 각 클라이언트는 독립된 프로세스에서 처리되므로 여러 클라이언트가 동시에 통신
- 데이터 송수신 : 클라이언트는 메시지를 보내고, 서버는 받은 데이터를 그대로 돌려주는(에코 서버) 방식으로 동작
- 종료 : 클라이언트가 "exit" 입력 시 연결 종료

### 3.멀티쓰레드(multithread)과 멀티프로세싱(multiprocessing)의 차이점과 어떤 작업에 적합한가?
