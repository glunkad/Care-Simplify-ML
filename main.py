from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI()

# Load the model pipeline
pipe = pipeline("text-generation", model="m42-health/Llama3-Med42-8B")

# Request body schema
class MessageRequest(BaseModel):
    role: str
    content: str

@app.post("/generate")
def generate_text(request: MessageRequest):
    try:
        response = pipe(request)
        
        return {"responses": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/hello")
def hello():
    return {"message": "API is running successfully!"}
