from pydantic import BaseModel ,PositiveInt,ValidationError

class User_input(BaseModel):
    age :PositiveInt
    income :PositiveInt
    loan_amount:PositiveInt
    credit_score:PositiveInt

class User_output(BaseModel):
    risk_score: float
    risk_category:str

# except ValidationError as err:
#     print(err)