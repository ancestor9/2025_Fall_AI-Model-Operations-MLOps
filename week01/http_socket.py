
# HTTP (Socket, HTTP, HTTPS, 도메인)
# 소켓: IP + Port (16비트)
# 파이썬을 이용한 소켓 프로그래밍
# http.client, requests
# HTTP get, put, delete, 

# import requests

# def http_get_with_requests(url):
#     # GET 요청 보내기
#     response = requests.get(url)
    
#     # 응답 상태와 헤더 출력
#     print("Status:", response.status_code)
#     print("Reason:", response.reason)
#     print("Headers:", response.headers)
    
#     # 응답 본문 읽기
#     body = response.text
    
#     return body

# # 예시: www.example.com의 루트 경로에 GET 요청 보내기
# url = 'http://www.example.com/'

# response = http_get_with_requests(url)
# print(response)


'''
host, port, path를 인자로 받아 http fh 정보를 get하는 소킷프로그램을 파이썬으로 만들어줘줘
'''
import socket

def http_get_request(host, port, path):
    """
    주어진 호스트, 포트, 경로를 사용하여 HTTP GET 요청을 보냅니다.
    """
    try:
        # 소켓 생성
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 서버 연결
        client_socket.connect((host, port))
        
        # HTTP GET 요청 메시지 생성
        request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
        
        # 요청 메시지를 서버로 전송
        client_socket.sendall(request.encode('utf-8'))
        
        response = b""
        while True:
            # 서버로부터 응답 수신
            data = client_socket.recv(4096)
            if not data:
                break
            response += data
            
        return response.decode('utf-8')
        
    except socket.gaierror as e:
        print(f"호스트 이름을 찾을 수 없습니다: {e}")
    except ConnectionRefusedError:
        print("연결이 거부되었습니다. 서버가 실행 중이지 않거나 잘못된 포트일 수 있습니다.")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
    finally:
        # 소켓 닫기
        client_socket.close()

# 사용 예시
host = "www.google.com"
port = 80
path = "/"
http_response = http_get_request(host, port, path)
print(http_response)