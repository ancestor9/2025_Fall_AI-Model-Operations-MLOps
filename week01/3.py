
# ChatGPT와 함께하는 파이썬 네트워크 프로그래밍 완전 정복

# 생활 속 네트워크 (인프런 접속 시 일어나는 일, IP Address, Wi-Fi, Cellular)

# 서브넷 마스크, 라우터의 IP 주소, Gateway

# 아, IP 주소라는 것은 네트워크 상에서 유일하게 식별할 수 있는 주소구나!

# 종류가 두가지가 있구나. 공인 IP (Cellular, 직접 랜선 포트에 연결된 공유기), 사설 IP (Wi-fi 내 기기들)

# 공유기에 전원을 연결한다. 랜선이 연결되어 있어야 한다.


# 벽에 있는 랜선 포트로부터 연결되어 있다. - 공유기 - Wi-Fi를 만들어준다. 그 와이파이에 맥북, 아이폰이 연결되어 있다.

# 전세계에서 유일한 IP 주소 (Public IP) -> 공유기 -> 내부 네트워크 안에 맥북, 아이폰


# 셀룰러를 켰을 때 -> 공유기를 통해 나가는게 X -> 바로 기지국으로 연결됨

# 하나는 컴퓨터 (바로 랜선 포트에 다이렉트에 연결되어 있음.)

# 다른 하나는 다른 방에 있는 랜선 포트에 공유기에 연결되어 있는 아이폰

# 공유기 입장에서
# 맥북 192.168.68.100
# 아이폰 192.168.68.104



import socket

def get_private_ip():
    try:
        # 구글 DNS 서버 (8.8.8.8)와의 연결 시도
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        s.connect(('8.8.8.8', 80))
        private_ip = s.getsockname()[0]
        s.close()
        return private_ip
    except Exception as e:
        return str(e)

print("Private IP Address:", get_private_ip())
