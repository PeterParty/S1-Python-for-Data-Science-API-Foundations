from fastapi import FastAPI ,Request
from pydantic import BaseModel
from models import User_input
import logging
import sys
from utils.logger import logger 

# logger = logging.getLogger(name=__name__)
# formatter =logging.Formatter(
#     fmt ="%(asctime)s - %(name)s- %(levelname)s - %(message)s", datefmt = "%Y-%m-%d %H:%M:%S"
# )

# handler = logging.StreamHandler(sys.stdout)
# handler.setFormatter(fmt=formatter)
# logger = logging.getLogger(__name__)
# logger.setLevel(level=logging.INFO)
# logger.addHandler(hdlr = handler)

app = FastAPI(title = "L1 -Python for data science and api foundations -Style ML Scoring API")
logger.info("Starting API...")

@app.middleware("http")
async def log_middleware(request: Request,call_next):
    log_dict={
        'url':request.url.path,
        'method':request.method
    }
    logger.info(log_dict)

    response = await call_next(request)
    return response


@app.get('/')
async def root():
    logger.info("Helth check requested")
    return {"stasus":"healthy"}

@app.post('/predict')
async def scoring(item:User_input):
    logger.info(f"User input is {item}")
    return item