## 출처 : https://wikidocs.net/229760

import google.generativeai as genai
import os
from dotenv import load_dotenv # 💡 Import the necessary function

# 1. Load the variables from the .env file into the environment
load_dotenv() 

# 2. os.getenv() can now successfully retrieve the key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    # Always good to check!
    raise ValueError("GOOGLE_API_KEY is not set. Check your .env file.")

genai.configure(api_key=api_key)

#####################################
# single_turn.py
#####################################
# model = genai.GenerativeModel('gemini-2.5-flash') 
# response = model.generate_content("인공지능에 대해 한 문장으로 설명하세요.")
# print(response.text)

#####################################
# multi_turn.py
model = genai.GenerativeModel('gemini-2.5-flash')
chat_session = model.start_chat(history=[]) #ChatSession 객체 반환
user_queries = ["인공지능에 대해 한 문장으로 짧게 설명하세요.", " 왜 인공지능을 배워야 하는가?", "어떤 프로그램언어가 인공지능을 구현하는데 가장 적합한가?"]
for user_query in user_queries:
    print(f'[사용자]: {user_query}')   
    response = chat_session.send_message(user_query)
    print(f'[모델]: {response.text}')