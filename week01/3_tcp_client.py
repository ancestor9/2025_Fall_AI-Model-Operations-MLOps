# ChatGPT 100% 활용하여 배우는 파이썬 네트워크 프로그래밍 A to Z

# TCP (서버, 클라이언트)

import socket
import time

# 서버 IP와 포트 설정
HOST = '127.0.0.1'
PORT = 9999

# 소켓 객체 생성
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 서버에 연결 요청
    s.connect((HOST, PORT))

    while True:
        # 서버에 메시지 전송
        s.sendall(b'Hello, world')
        data = s.recv(1024)
        print('받은 데이터:', data.decode())
        time.sleep(1)

