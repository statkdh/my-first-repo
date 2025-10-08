# gemini_helper.py
import os
from google import genai

def gm_call(prompt: str,
               model: str = "gemini-2.5-flash",
               api_key: str | None = None) -> str:
    """
    Gemini 모델에 프롬프트를 전달해 텍스트 응답을 반환하는 함수.
    """
    try:
        key = os.getenv("GEMINI_API_KEY")
        if not key:
            raise ValueError("API 키가 설정되지 않았습니다. 환경 변수 GEMINI_API_KEY를 설정하세요.")
        
        client = genai.Client(api_key=key)
        response = client.models.generate_content(
            model=model,
            contents=prompt
        )
        return response.text.strip()
    
    except Exception as e:
        return f"[Error] {type(e).__name__}: {e}"
