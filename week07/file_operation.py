######## Text File Handling #######

# file = open('dog_breeds.txt')
# print(type(file))
# print(file.read())
# file.close()

# reader = open('dog_breeds.txt')
# # try:
# #     # Further file processing goes here
# for i in range(3):
#     print(reader.readline())
    
# # finally:
# #     reader.close()

# with open('dog_breeds.txt') as reader:
#     for i in range(3):
#         print(reader.readline())
#     # Further file processing goes here
    
# file = open('dog_breeds.txt', 'wb')
# print(type(file))
# #<class '_io.TextIOWrapper'>

import io

# # StringIO 객체 생성 및 초기화
# f = io.StringIO("some initial text data") 

# # 현재 위치에서 읽기
# print(f.read())  # 출력: some initial text data

# # 쓰기
# f.write(" and more data")

# # 커서를 스트림의 시작(0)으로 이동
# f.seek(0)

# # 전체 내용 다시 읽기
# print(f.read())  # 출력: some initial text data and more data

# ####### Binary File Handling #######
# f = open("Felis_silvestris_silvestris_small_gradual_decrease_of_quality.png", "rb")
# print(type(f))

# f = io.BytesIO(b"some initial binary data: \x00\x01")
# print(f.read())  # 출력: b'some initial binary data: \x00\x01'

####### Unbuffered Binary File Handling #######
f = open("Felis_silvestris_silvestris_small_gradual_decrease_of_quality.png", "rb", buffering=0)
print(type(f))