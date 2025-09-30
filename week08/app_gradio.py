import gradio as gr
import requests 
import json

# FastAPI 서버 주소 (FastAPI가 8000번 포트에서 실행된다고 가정)
FASTAPI_URL = "http://127.0.0.1:8000/predict/"

def predict_species(sl, sw, pl, pw):
    """FastAPI를 호출하여 예측 결과를 가져옵니다."""
    
    payload = {"sl": sl, "sw": sw, "pl": pl, "pw": pw}
    
    try:
        response = requests.post(FASTAPI_URL, json=payload)
        response.raise_for_status()

        result = response.json()
        
        # 💡 이 부분이 수정되었습니다: 'species'와 'confidence' 키를 사용합니다.
        species = result["species"].capitalize()
        confidence = result["confidence"] * 100
        
        return f"✅ 예측 품종: {species}\n(확신도: {confidence:.2f}%)"
        
    except requests.exceptions.ConnectionError:
        return "❌ 오류: FastAPI 서버(8000번 포트)에 연결할 수 없습니다."
    except Exception as e:
        # 이전에 발생했던 422 오류를 잡기 위해 추가 점검
        if "422 Client Error" in str(e):
             return "❌ 입력 오류 (422): FastAPI 서버로 전달된 데이터 형식에 문제가 있습니다. 변수 이름(sl, sw, pl, pw)을 확인하세요."
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
    outputs=gr.Textbox(label="예측 결과", lines=10),
    title="FastAPI (PKL Load) + Gradio: 붓꽃(Iris) 품종 예측 서비스",
    description="슬라이더를 조절하여 붓꽃의 크기를 입력하고 품종을 예측합니다."
)

if __name__ == "__main__":
    iface.launch()