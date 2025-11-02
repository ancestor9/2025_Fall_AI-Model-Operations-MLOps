from fastapi import FastAPI, File, UploadFile

# UploadFile 객체의 read() 메서드는 비동기 함수

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    # Access file content using await file.read() in memory
    '''
    file: UploadFile 객체의 read() 메서드는 비동기적으로(asynchronously) 파일 데이터를 읽어오는 작업을 수행
    await의 역할: await 키워드는 파이썬에게 "이 파일 읽기 작업(I/O 작업)이 끝날 때까지 기다려라. 
    하지만 기다리는 동안 CPU를 점유하지 말고 다른 비동기 작업을 처리할 수 있도록 제어권을 넘겨라"고 지시
    '''
    contents = await file.read()
    # Save the file to disk or process its contents
    # For example, save to a local directory:
    '''
    with open(...) 구문은 await file.read()가 완료된 후 실행
    contents = await file.read(): 클라이언트가 보낸 파일 내용 전체를 메모리(RAM)에 바이너리 데이터로 로드하는 작업이 끝나면,
    with open(...): 파일 내용이 모두 메모리에 들어온 후에, 
    디스크에 새 파일을 열고 메모리(contents)의 내용을 디스크에 동기적으로 기록하는 작업을 수행
    '''
    with open(f"uploaded_files/{file.filename}", "wb") as f:
        f.write(contents)
        
    print(f"Saved file: {file.filename}, Content Type: {file.content_type}, Size: {len(contents)} bytes")
    
    return {"filename": file.filename, "content_type": file.content_type, "size": len(contents)}

'''
file.read()는 네트워크 I/O(클라이언트로부터 데이터 수신)와 관련된 비동기 작업이며, 
with open(...)은 로컬 디스크 I/O(디스크에 쓰기)와 관련된 작업으로, 
코드 상의 await 때문에 순차적으로 실행
'''