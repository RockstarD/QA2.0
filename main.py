import pickle
from fastapi import FastAPI, Body
from typing import Union
from mymodal import predictAnswer
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origin = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# server html file at '/' route
@app.get('/')
async def index():
    return FileResponse('./src/index.html')

@app.post('/predict')
async def predict(data: dict = Body(...)):
    print(data)
    questions = []
    for i in data:
        # questions.append(data[i].values()) add valuse to list
        questions.append(data[i].get('question'))
    print(questions)
    ans  = predictAnswer( questions)
    return {
        'data': ans
    }


