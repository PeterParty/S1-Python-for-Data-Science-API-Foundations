from fastapi import FastAPI
from pydantic import BaseModel
from models import User_input
# todo: Adaug in docker fastapi si celelelalte librari
app = FastAPI()

# class User_input(BaseModel):
#     age :int
#     income :int
#     loan_ammount:int
#     credit_score:int


@app.post('/predict')
async def scoring(item:User_input):
    return item