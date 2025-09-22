import gradio as gr
from models.course_model import CourseModel, Course

model = CourseModel()

def upload_csv(file):
    model.load_csv(file.name)
    return "업로드 완료!"

def show_sorted():
    if model.df.empty:
        return "<p>데이터가 없습니다. CSV 파일을 먼저 업로드하세요.</p>"
    return model.sort_by_professor().to_html(index=False)

def search_professor(name):
    if model.df.empty:
        return "<p>데이터가 없습니다.</p>"
    result = model.search_by_professor(name)
    if result.empty:
        return f"<p>'{name}' 교수를 찾을 수 없습니다.</p>"
    return result.to_html(index=False)

def search_credit(credit):
    if model.df.empty:
        return "<p>데이터가 없습니다.</p>"
    result = model.search_by_credit(credit)
    if result.empty:
        return f"<p>{credit}학점 과목을 찾을 수 없습니다.</p>"
    return result.to_html(index=False)

def add_course(교과목명, 강좌담당교수, 개설학년, 교과목학점):
    # Course 객체로 생성하여 일관성 유지
    course = Course(
        교과목명=교과목명,
        강좌담당교수=강좌담당교수,
        개설학년=int(개설학년),
        교과목학점=int(교과목학점)
    )
    model.add_course(course)
    return "추가 완료!"

def delete_course(교과목명):
    model.delete_course(교과목명)
    return "삭제 완료!"

with gr.Blocks() as demo:
    gr.Markdown("# 강좌 관리 시스템")
    
    # CSV 업로드
    file_input = gr.File(label="CSV 업로드", type="filepath")
    upload_output = gr.Textbox(label="업로드 상태")
    file_input.upload(upload_csv, inputs=file_input, outputs=upload_output)
    
    # 교수 내림차순 보기
    sort_btn = gr.Button("교수 내림차순 보기")
    sort_output = gr.HTML()
    sort_btn.click(show_sorted, outputs=sort_output)
    
    # 교수 검색
    prof_input = gr.Textbox(label="교수 이름")
    prof_output = gr.HTML()
    prof_input.submit(search_professor, inputs=prof_input, outputs=prof_output)
    
    # 학점 검색
    credit_input = gr.Number(label="학점")
    credit_output = gr.HTML()
    credit_input.submit(search_credit, inputs=credit_input, outputs=credit_output)

    # 과목 삭제
    삭제_교과목명 = gr.Textbox(label="삭제할 교과목명")
    delete_btn = gr.Button("교수삭제")
    delete_output = gr.Textbox(label="삭제 상태")
    delete_btn.click(
        delete_course,
        inputs=[삭제_교과목명],
        outputs=delete_output
    )

    # 과목 추가
    교과목명 = gr.Textbox(label="교과목명")
    강좌담당교수 = gr.Textbox(label="강좌담당교수")
    개설학년 = gr.Number(label="개설학년")
    교과목학점 = gr.Number(label="교과목학점")
    add_btn = gr.Button("교수배정")
    add_output = gr.Textbox(label="추가 상태")
    add_btn.click(
        add_course,
        inputs=[교과목명, 강좌담당교수, 개설학년, 교과목학점],
        outputs=add_output
    )