from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Union
import numpy as np
from io import BytesIO
import base64
from joblib import load

app = FastAPI()

class Form(BaseModel):
    pregnancies: Union[int, float] = 0
    glucose: Union[int, float] = 0
    insulin: Union[int, float] = 0
    age: Union[int, float] = 0
    bloodPressure: Union[int, float] = 0
    skinThickness: Union[int, float] = 0
    bmi: Union[int, float] = 0
    pedigreeFunction: Union[int, float] = 0

@app.get("/")
async def read_root():
    with open("../front_end/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)
def process(form):
    scaler = load('../model/scaler.joblib')
    model = load('../model/model.joblib')
    pregnancies = form.pregnancies
    glucose = form.glucose
    insulin = form.insulin
    age = form.age
    bloodPressure = form.bloodPressure
    skinThickness = form.skinThickness
    bmi = form.bmi
    pedigreeFunction = form.pedigreeFunction
    X = np.array([[pregnancies, glucose, bloodPressure, skinThickness, insulin, bmi, pedigreeFunction, age]])
    X = scaler.transform(X)
    ypre = model.predict(X)
    return ypre
@app.post("/form")
async def get_form(form: Form):
    # print(form)
    data = process(form)
    print(data[0])
    js = {
        # int(data[0])
        "prediction": int(data[0]),
    }
    return JSONResponse(content=js, status_code=200)
