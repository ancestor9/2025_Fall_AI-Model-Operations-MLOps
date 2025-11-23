### FastAPI를 이용해 AI 기반 REST API 서버를 설계하고 구현
#### [Gemini API: Getting started with Gemini models](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started.ipynb#scrollTo=eVmFDcYOSNiV)
- Streamlit/gradio을 활용하여 데이터 기반 웹 인터페이스를 구축
- 두 기술을 통합하여 상호작용 가능한 웹 서비스를 만들고, 실제 AI 모델 또는 LLM을 연동
- [RAG](https://mintcdn.com/langchain-5e9cc07a/I6RpA28iE233vhYX/images/rag_indexing.png?w=840&fit=max&auto=format&n=I6RpA28iE233vhYX&q=85&s=1838328a870c7353c42bf1cc2290a779) 실전 프로젝트를 통해 기획부터 배포까지의 전 과정을 경험
- RAG(Retrieval-Augmented Generation) '검색 증강 생성'을 의미하며, AI 모델이 답변을 생성할 때 외부 정보 소스에서 관련 내용을 검색하여 활용함으로써 정확성과 신뢰성을 높이는 기술

#### Google Gemini API와 File Search API
- [복잡한 LangChain이나 VectorDB 설정 없이도](https://docs.langchain.com/oss/python/langchain/rag) 내 파일 기반으로 답변하는 AI (RAG)를 만드는 방법
- Google의 새로운 File Search API를 사용하면 단 몇 줄의 파이썬 코드로 이 모든 것을 간단하게 구현
- google_file_search.ipynb : RAG
-     1. 특정 텍스트 파일(txt)을 업로드하고, (Gemini Grounding 기능)
      2. AI가 오직 그 파일의 내용만을 '검색'하고 '참고'하여
      3. 질문에 답변하도록 만드는 전체 과정을 코드를 실행하며 단계별로 구현
