
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


import requests

def get_public_ip():
    try:
        # 공인 IP를 알려주는 서비스에 요청
        response = requests.get('https://api64.ipify.org?format=json')
        response.raise_for_status()  # HTTP 오류 발생 시 예외 발생
        
        # 응답에서 IP 주소 추출
        ip_data = response.json()
        public_ip = ip_data.get('ip')
        
        return public_ip
    except requests.RequestException as e:
        print(f"오류 발생: {e}")
        return None

if __name__ == "__main__":
    ip_address = get_public_ip()
    if ip_address:
        print(f"나의 공인 IP 주소: {ip_address}")
    else:
        print("공인 IP 주소를 확인할 수 없습니다.")
