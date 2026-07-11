from fastapi import FastAPI
from pydantic import BaseModel
from model import predict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="MHS Predictor API", description="Menstrual Health Intelligence Backend")

# Allow all origins so Netlify frontend can talk to this Render backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    age: int
    awareness: int
    income: int
    rural: int

@app.get("/")
def home():
    return {"message": "MHS Predictor Backend Running"}

@app.post("/predict")
def get_prediction(data: InputData):
    result = predict(data.dict())
    return {
        "prediction": result,
        "meaning": "Will Use Kit" if result == 1 else "Likely Not Using"
    }
