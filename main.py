from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import joblib
from pydantic import BaseModel, validator
import numpy as np

app = FastAPI()
model = joblib.load('svr_model.pkl')

class InputData(BaseModel):
    Gender: int
    Age: float
    Height: float
    Weight: float
    Duration: float
    Heart_Rate: float
    Body_Temp: float

@app.post('/predict')
def predict(data: InputData):
    X = np.array([[
        data.Gender, data.Age, data.Height, data.Weight,
        data.Duration, data.Heart_Rate, data.Body_Temp
    ]])
    prediction = model.predict(X)
    return {'calories': round(float(prediction[0]), 2)}

@app.get('/', response_class=HTMLResponse)
def index():
    with open('index.html') as f:
        return f.read()

@validator('Duration')
def duration_must_be_valid(cls, v):
    if v > 30:
        raise ValueError('Duration maksimal 30 menit sesuai data training')
    return v