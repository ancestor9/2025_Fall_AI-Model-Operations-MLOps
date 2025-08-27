# ChatGPT 100% 활용하여 배우는 파이썬 네트워크 프로그래밍 A to Z

# UDP (서버, 클라이언트)

import socket

# 서버의 IP 주소와 포트 번호
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# UDP 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 소켓을 주소에 바인딩
server_socket.bind((UDP_IP, UDP_PORT))

print("UDP 서버가 시작되었습니다.")

while True:
    # 클라이언트로부터 데이터 수신
    data, addr = server_socket.recvfrom(1024)
    print(f"수신된 데이터: {data.decode()}")

    # 클라이언트에게 데이터 전송
    server_socket.sendto(data, addr)
