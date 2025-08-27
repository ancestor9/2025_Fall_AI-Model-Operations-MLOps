# ChatGPT 100% 활용하여 배우는 파이썬 네트워크 프로그래밍 A to Z

# UDP (서버, 클라이언트)

import socket

# 서버의 IP 주소와 포트 번호
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# UDP 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("전송할 메시지 입력: ")

    # 서버에 데이터 전송
    client_socket.sendto(message.encode(), (UDP_IP, UDP_PORT))

    # 서버로부터 데이터 수신
    data, addr = client_socket.recvfrom(1024)
    print(f"서버로부터 수신된 데이터: {data.decode()}")

client_socket.close()
