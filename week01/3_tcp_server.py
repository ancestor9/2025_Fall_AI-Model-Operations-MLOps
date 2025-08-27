# ChatGPT 100% 활용하여 배우는 파이썬 네트워크 프로그래밍 A to Z

# TCP (서버, 클라이언트)

# 헨드폰으로 동영상을 볼 때, 네트워크 상에서 패킷(데이터)가 손실되는 경우가 있음. 텍스트, 중요한 정보, 손실이 되면 문제가 생김

# 클라이언트와의 연결 과정이 있다. 3 hand shake
# 종료 과정. 4 hand shake

# 3 hand shake
# SYN: 클라이언트 -> 서버 (나 연결 부탁해)
# SYN + ACK: 서버 -> 클라이언트 (ok. 수락할게. 나 너의 SYN을 잘 받았어.)
# ACK: 클라이언트 -> 서버 (ok. 너가 연결을 수락한다는 것을 잘 받았어.)

# TCP 재전송
# 1. 내가 보낸 데이터가 서버까지 도달하지 못했을 때 (서버로부터 ACK가 안오기 때문에, 재전송이 된다.)
# 2. 내가 보낸 데이터는 서버에 잘 도달을 했어요. 서버가 나한테 ACK를 보내줬는데, ACK를 제가 못받음. (재전송이 된다.)



# 1, 2, 3, 4, 5 데이터를 보낸다.

# 5, 3, 2, 4, 1 -> 1, 2, 3, 4, 5 재조립을 한다. 순서를 보장한다.

import socket

# 서버 IP와 포트 설정
HOST = '127.0.0.1'
PORT = 9999

# 소켓 객체 생성
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 소켓을 HOST와 PORT에 바인딩
    s.bind((HOST, PORT))
    # 클라이언트의 연결 요청 대기
    s.listen()
    print('서버가 시작되었습니다. 클라이언트의 연결을 기다립니다...')
    while True:
    # 연결 수락
      conn, addr = s.accept()
      with conn:
          print('연결되었습니다:', addr)
          while True:
              data = conn.recv(1024)
              if not data:
                  break
              print('받은 데이터:', data.decode())
              conn.sendall(data)  # 받은 데이터를 그대로 클라이언트에 전송
