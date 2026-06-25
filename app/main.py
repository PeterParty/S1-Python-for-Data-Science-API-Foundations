from fastapi import FastAPI

app = FastAPI()

@app.post('/predict')
async def scoring():
    return{"hello":"world"}