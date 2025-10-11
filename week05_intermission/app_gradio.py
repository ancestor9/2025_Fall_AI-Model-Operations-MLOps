import gradio as gr
import requests

# FastAPI 서버 주소
FASTAPI_URL = "http://127.0.0.1:8000/predict/"

def predict_species(sl, sw, pl, pw):
    """FastAPI를 호출하여 예측 결과를 가져옵니다."""
    
    # API 스펙에 맞게 키 이름 수정
    payload = {
        "sepal_length": sl,
        "sepal_width": sw,
        "petal_length": pl,
        "petal_width": pw
    }
    
    try:
        response = requests.post(FASTAPI_URL, json=payload)
        response.raise_for_status()
        
        result = response.json()
        
        species = result["species"].capitalize()
        confidence = result["confidence"] * 100
        
        return f"✅ 예측 품종: {species}\n(확신도: {confidence:.2f}%)"
        
    except requests.exceptions.ConnectionError:
        return "❌ 오류: FastAPI 서버(8000번 포트)에 연결할 수 없습니다.\n터미널에서 'uvicorn api:app --reload'로 서버를 먼저 실행하세요."
    except requests.exceptions.HTTPError as e:
        return f"❌ HTTP 오류 ({e.response.status_code}): {e.response.text}"
    except Exception as e:
        return f"❌ 예측 오류: {e}"


# --- Gradio 인터페이스 정의 ---
iface = gr.Interface(
    fn=predict_species,
    inputs=[
        gr.Slider(minimum=4.0, maximum=8.0, step=0.1, value=5.1, label="꽃받침 길이 (Sepal Length, cm)"),
        gr.Slider(minimum=2.0, maximum=4.5, step=0.1, value=3.5, label="꽃받침 너비 (Sepal Width, cm)"),
        gr.Slider(minimum=1.0, maximum=7.0, step=0.1, value=1.4, label="꽃잎 길이 (Petal Length, cm)"),
        gr.Slider(minimum=0.1, maximum=2.5, step=0.1, value=0.2, label="꽃잎 너비 (Petal Width, cm)"),
    ],
    outputs=gr.Textbox(label="예측 결과", lines=3),
    title="🌸 붓꽃(Iris) 품종 예측 서비스",
    description="슬라이더를 조절하여 붓꽃의 크기를 입력하고 품종을 예측합니다."
)

if __name__ == "__main__":
    iface.launch()