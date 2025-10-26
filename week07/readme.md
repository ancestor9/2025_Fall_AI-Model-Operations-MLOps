### 0. FastAPI Review
#### [Using FastAPI to Build Python Web APIs : self study](https://realpython.com/fastapi-python-web-apis/)

### 1. Python I/O 세 가지 방식 : file_operation.py
-        2.1. Text files
        2.2. Buffered binary files
        2.3. Raw binary files
$$\text{프로그램 } (\text{str}) \xleftarrow{\text{Text I/O}} \text{버퍼} (\text{bytes}) \xleftarrow{\text{Buffered I/O}} \text{운영체제} (\text{bytes}) \xleftarrow{\text{Raw I/O}} \text{디스크}$$
-       Text I/O: 프로그래머가 f.write("안녕하세요\n") (str) 호출 --> 문자열을 바이트로 인코딩
        Buffered I/O: 인코딩된 바이트를 버퍼에 저장하고 관리 --? 버퍼가 차면 Raw I/O로 플러시
        Raw I/O: 버퍼링된 바이트 데이터를 운영체제에 전달하여 실제 디스크에 기록합니다.

- [Reading and Writing Files in Python ](https://realpython.com/read-write-files-python/)
- [Python i/o stream](https://docs.python.org/ko/3.13/library/io.html)

### 2. FastAPI + UI with Database
#### 2.1. python CLI(Command Line Interface)로 sqlite3 CRUD 실습
- sqlite3_introduction.ipynb 을 따라하기

#### 2.2. CRUD 과제 ([sqlite3](https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial))
- shopping_list: List[str] = ["사과", "바나나", "우유"] 의 CRUD 예제(지난 주)를 sqlite3로 만들어 보기
-         CRUD를 with 구문 (context manager)으로 구성하기
- supabase(cloud postgres)와 connect..

