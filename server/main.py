import logging
from fastapi import FastAPI
from logging.config import dictConfig
from sqlalchemy import text

from server.log import LogConfig
from db import session

dictConfig(LogConfig().dict())
logger = logging.getLogger("mycoolapp")

app = FastAPI()


@app.get("/")
async def read_root():
    logger.debug("Hllo World")
    return {"Hello": "World"}

@app.get("/ready")
async def ready():
    result = session.execute(text("SELECT now();")).fetchall()
    logger.debug("Ready %s", result)
    return {"Hello": "World"}
