### 0. FastAPI Review
#### [Using FastAPI to Build Python Web APIs : self study](https://realpython.com/fastapi-python-web-apis/)

### 1. Python I/O 세 가지 방식
#### 1.1 file_operation.py으로 실습하기
-         2.1. Text files
          2.2. Buffered binary files
          2.3. Raw binary files
$$\text{프로그램 } (\text{str}) \xleftarrow{\text{Text I/O}} \text{버퍼} (\text{bytes}) \xleftarrow{\text{Buffered I/O}} \text{운영체제} (\text{bytes}) \xleftarrow{\text{Raw I/O}} \text{디스크}$$
-       Text I/O: 프로그래머가 f.write("안녕하세요\n") (str) 호출 --> 문자열을 바이트로 인코딩
        Buffered I/O: 인코딩된 바이트를 버퍼에 저장하고 관리 --? 버퍼가 차면 Raw I/O로 플러시
        Raw I/O: 버퍼링된 바이트 데이터를 운영체제에 전달하여 실제 디스크에 기록합니다.

- [Reading and Writing Files in Python ](https://realpython.com/read-write-files-python/)
- [Python i/o stream](https://docs.python.org/ko/3.13/library/io.html)
  
#### 1.2. file_upload.py로 비동기 실습하기
- 1.2.1. await file.read()는 네트워크 I/O 작업(클라이언트로부터 데이터 수신)이며, 
- 1.2.2. with open(...)은 로컬 디스크 I/O 작업(디스크에 쓰기)으로

| 코드 | 주방에서의 역할 | 설명 |
|------|------------------|------|
| `file.read()` | 수프 끓이기 (시간이 오래 걸리는 I/O 작업) | 서버가 클라이언트로부터 대용량 파일을 수신하는 작업은 시간이 오래 걸림|
| `await` | 수프가 끓을 때까지 다른 테이블 주문받기 | 셰프(CPU)는 수프(파일 읽기)가 다 될 때까지 손 놓고 기다리지 않고. 잠시 다른 직원(이벤트 루프)에게 “수프 냄비를 감시해 줘. 끓으면 나한테 알려주고, 그동안 난 다른 주문(다른 클라이언트 요청)을 처리할게”라고 맡기는 것 : 비동기방식. |
| `contents =` | 끓은 수프를 그릇에 담기 (결과 저장) | 수프가 다 끓었을 때(파일 수신이 완료되었을 때), 셰프는 하던 일을 멈추고 돌아와 수프를 그릇(`contents`)에 담기. |
| `with open(f"uploaded_files/{file.filename}", "wb") as f:` | 그릇을 꺼내 준비하기 (파일을 담을 공간 열기) | 수프를 담을 그릇(파일)을 준비하는 과정, `with open` 구문은 파일을 안전하게 열고 닫는 ‘자동 설거지 시스템’ 역할 |
| `f.write(contents)` | 완성된 수프를 그릇에 붓기 (저장하기) | 끓인 수프(파일 내용)를 실제 그릇(저장소)에 담는 단계로, 이 과정을 통해 서버는 파일을 디스크에 안전하게 저장 |


### 2. FastAPI + UI with Database(Data Persisitency)
#### 2.1. week05 >> main.py
- Thunder Client 로 get, post 방식 실습 해보기(DB 이해)

#### 2.2. python CLI(Command Line Interface)로 sqlite3 CRUD 실습
- sqlite3_introduction.ipynb 을 따라하기 sqlite3_introduction.py로 따라하기

#### 2.3. CRUD 과제 ([sqlite3](https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial))
- shopping_list: List[str] = ["사과", "바나나", "우유"] 의 CRUD 예제(지난 주)를 sqlite3로 만들어 보기
-         CRUD를 with 구문 (context manager)으로 구성하기
- "chinook DB"를 CRUD 실습과제 수행
- supabase(cloud postgres)와 connect..

