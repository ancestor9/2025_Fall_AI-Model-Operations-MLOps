import google.generativeai as genai
import os
from dotenv import load_dotenv 

## 1. Load the variables from the .env file into the environment
load_dotenv() 
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

#####################################   
# 1. 페르소나 만들기
#####################################
# system_instruction = "당신은 유치원 선생님입니다. 사용자는 유치원생입니다. 쉽고 친절하게 이야기하되 3문장 이내로 짧게 얘기하세요."
# model = genai.GenerativeModel("gemini-2.5-flash", 
#                               system_instruction=system_instruction)

# chat_session = model.start_chat(history=[])  # ChatSession 객체 반환
# user_queries = ["인공지능이 뭐에요?", "그럼 스스로 생각도 해요?", "그럼 동요를 하나 만들어줘요."]

# for user_query in user_queries:
#     print(f"[사용자]: {user_query}")
#     response = chat_session.send_message(user_query)
#     print(f"[모델]: {response.text}")
    
#####################################
# 2. 답변 형식 지정하기
#####################################
# import json
# system_instruction='JSON schema로 주제별로 답하되 3개를 넘기지 말 것:{{"주제": <주제>, "답변":<두 문장 이내>}}'
# model = genai.GenerativeModel("gemini-2.5-flash", 
#                               system_instruction=system_instruction, 
#                               generation_config={"response_mime_type": "application/json"})
# chat_session = model.start_chat(history=[])  # ChatSession 객체 반환
# user_queries = ["인공지능의 특징이 뭐에요?", "어떤 것들을 조심해야 하죠?"]

# for user_query in user_queries:
#     print(f'[사용자]: {user_query}')
#     response = chat_session.send_message(user_query)
#     answer_dict = json.loads(response.text)
#     print(answer_dict)

##############################################
## 3.1. 구조화된 출력(Structured output) 사용하기
## JSON Schema 정의하기
#############################################
# json_schema = {
#     'properties': {
#         'product_name': {
#             'type': 'string'
#         },
#         'size': {
#             'enum': ['S', 'M', 'L', 'XL'],
#             'type': 'string'
#         },
#         'price': {
#             'type': 'integer'
#         },
#     },
#     'required': ['price', 'size', 'product_name'],
#     'type': 'object'
# }

# model = genai.GenerativeModel("gemini-2.0-flash")
# response = model.generate_content(
#     "덩치가 크고 등산을 좋아하는 남성의 옷을 추천해주세요",
#     generation_config=genai.GenerationConfig(
#         response_mime_type="application/json", response_schema=json_schema
#     ),
# )
# print(response.text)

##############################################
## 3.2. 구조화된 출력(Structured output) 사용하기
## TypedDict 및 Enum 정의하기
#############################################
import enum
from typing_extensions import TypedDict
class Size(enum.Enum):
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"

class Prodcut(TypedDict):
    product_name: str
    size: Size
    price: int

model = genai.GenerativeModel("gemini-2.5-flash")
response = model.generate_content(
    "덩치가 크고 등산을 좋아하는 남성의 옷을 추천해주세요",
    generation_config=genai.GenerationConfig(
        response_mime_type="application/json", response_schema=Prodcut
    ),
)
print(response.text)
