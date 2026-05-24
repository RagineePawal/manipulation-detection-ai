from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Manipulation Detection API Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: Message):

    # Dummy prediction
    result = {
        "intent": "coercive",
        "type": "emotional_blackmail",
        "domain": "personal",
        "severity": "high",
        "confidence": 0.91
    }

    return result
