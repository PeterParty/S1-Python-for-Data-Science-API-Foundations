from pydantic import BaseModel

class User_input(BaseModel):
    age :int
    income :int
    loan_ammount:int
    credit_score:int