import requests
from prompt import TONE_REWRITE_PROMPT
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3:3.8b"


def rewrite_text(text: str, tone: str) -> str:
    prompt = TONE_REWRITE_PROMPT.format(
        text=text,
        tone=tone
    )

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()
    return response.json()["response"].strip()


