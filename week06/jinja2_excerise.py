###############################################
# 1. Render Your First Jinja Template
###############################################
# import jinja2

# environment = jinja2.Environment()
# template = environment.from_string("Hello, {{ name }}!")
# template.render(name="World")

# print(template.render(name="World"))

###############################################
# 2. Render a Template from a External File
################################################

# from jinja2 import Environment, FileSystemLoader
# import os 

# max_score = 100
# test_name = "Python Challenge"
# students = [
#     {"name": "Sandrine",  "score": 100},
#     {"name": "Gergeley", "score": 87},
#     {"name": "Frieda", "score": 92},
# ]

# environment = Environment(loader=FileSystemLoader("templates/"))
# template = environment.get_template("message1.txt")

# for student in students:
#     # filename = f"message_{student['name'].lower()}.txt"
#     # 'templates/' 경로를 파일명 앞에 추가하여 저장 경로를 지정
#     filename = os.path.join("templates", f"message1_{student['name'].lower()}.txt") 
   
#     content = template.render(
#         student,
#         max_score=max_score,
#         test_name=test_name
#     )
#     with open(filename, mode="w", encoding="utf-8") as message:
#         message.write(content)
#         print(f"... wrote {filename}")
        
###############################################
# 3. Use if Statements
###############################################
# from jinja2 import Environment, FileSystemLoader
# import os 

# max_score = 100
# test_name = "Python Challenge"
# students = [
#     {"name": "Sandrine",  "score": 100},
#     {"name": "Gergeley", "score": 87},
#     {"name": "Frieda", "score": 92},
#     {"name": "Fritz", "score": 40},
#     {"name": "Sirius", "score": 75},
# ]

# environment = Environment(loader=FileSystemLoader("templates/"))
# template = environment.get_template("message2.txt")

# for student in students:
#     # filename = f"message_{student['name'].lower()}.txt"
#     # 'templates/' 경로를 파일명 앞에 추가하여 저장 경로를 지정
#     filename = os.path.join("templates", f"message2_{student['name'].lower()}.txt") 
   
#     content = template.render(
#         student,
#         max_score=max_score,
#         test_name=test_name
#     )
#     with open(filename, mode="w", encoding="utf-8") as message:
#         message.write(content)
#         print(f"... wrote {filename}")
        
###############################################
# 4. Leverage for Loops
###############################################        

# from jinja2 import Environment, FileSystemLoader
# import os
        

# max_score = 100
# test_name = "Python Challenge"
# students = [
#     {"name": "Sandrine",  "score": 100},
#     {"name": "Gergeley", "score": 87},
#     {"name": "Frieda", "score": 92},
#     {"name": "Fritz", "score": 40},
#     {"name": "Sirius", "score": 75},
# ]

# results_filename = "templates\students_results.html"
# environment = Environment(loader=FileSystemLoader("templates/"))

# results_template = environment.get_template("results.html")
# print(results_template)

# context = {
#     "students": students,
#     "test_name": test_name,
#     "max_score": max_score,
# }

# with open(results_filename, mode="w", encoding="utf-8") as results:
#     results.write(results_template.render(context))
#     print(f"... wrote {results_filename}")
    
    
###############################################
# 5. Leverage for Loops with Conditionals
###############################################        

# from jinja2 import Environment, FileSystemLoader
# import os
        

# max_score = 100
# test_name = "Python Challenge"
# students = [
#     {"name": "Sandrine",  "score": 100},
#     {"name": "Gergeley", "score": 87},
#     {"name": "Frieda", "score": 92},
#     {"name": "Fritz", "score": 40},
#     {"name": "Sirius", "score": 75},
# ]

# results_filename = "templates\students_results_if.html"
# environment = Environment(loader=FileSystemLoader("templates/"))

# results_template = environment.get_template("results_if.html")
'''
This means: If a student's score is greater than 80, the HTML output will include a 😀 emoji.
Otherwise (if the score is 80 or less), the output will include a 😟 emoji.
'''

# context = {
#     "students": students,
#     "test_name": test_name,
#     "max_score": max_score,
# }

# with open(results_filename, mode="w", encoding="utf-8") as results:
#     results.write(results_template.render(context))
#     print(f"... wrote {results_filename}")


###############################################
# 6. Template 
# https://fastapi.tiangolo.com/advanced/templates/#template-url-for-arguments
###############################################   

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )
    
'''
파일/폴더 설명 ---> 
jinja2_excerse.py: FastAPI 앱을 초기화하고, Jinja2Templates를 templates 디렉토리로 설정하며, 경로 작동(라우트) 함수를 정의하는 Python 파일

templates/	: Jinja2와 같은 템플릿 엔진이 찾을 HTML 파일(.html)을 저장하는 폴더로 jinja2_excerse.py에서 이 폴더를 지정

static/	: CSS, JavaScript, 이미지 파일 등 브라우저에 직접 제공되는 정적 파일들을 저장하는 폴더로 jinja2_excerse.py에서 StaticFiles를 사용하여 이 폴더를 마운트
'''