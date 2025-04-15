import os
import requests
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow frontend on port 5173 to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

# Put your actual Groq API key here or set it via an environment variable
GROQ_API_KEY = "------------------ur api key---------"  # <--- Replace with your actual Groq API key

@app.post("/generate")
async def generate(request: PromptRequest):
    prompt = request.prompt

    # Actual request to Groq API
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "messages": [
                {"role": "system", "content": "You are an expert assistant"},
                {"role": "user", "content": prompt}
            ],
            "model": "llama3-70b-8192",
            "temperature": 0.7
        }
    )

    if response.status_code != 200:
        return {"answer": f"Error contacting AI model: {response.text}"}

    data = response.json()
    answer = data['choices'][0]['message']['content']
    return {"answer": answer}
