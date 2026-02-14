from fastapi import FastAPI
import os
import openai

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
def home():
    return {"status": "Digital Holding AI Online"}

@app.get("/chat")
def chat(msg: str):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": msg}]
    )
    return {"response": response.choices[0].message.content}
