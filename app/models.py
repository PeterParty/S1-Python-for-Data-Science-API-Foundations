from pydantic import BaseModel

class User_input(BaseModel):
    age :int
    income :int
    loan_ammount:int
    credit_score:int

class User_output(BaseModel):
    risk_score: int
    risk_category:str