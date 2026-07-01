from fastapi import FastAPI
from pydantic import BaseModel
from models import User_input

app = FastAPI()

@app.post('/predict')
async def scoring(item:User_input):
    return item