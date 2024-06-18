import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from logging.config import dictConfig
from sqlalchemy import text
from fastapi.middleware.cors import CORSMiddleware

from server.log import LogConfig
from db import session  # Adjust the import here
from api.endpoints import router as api_router  # Adjust the import here

dictConfig(LogConfig().dict())
logger = logging.getLogger("mycoolapp")

app = FastAPI()

# Allow CORS for local development (adjust as necessary for your deployment)
origins = [
    "http://localhost",
    "http://localhost:8100",  # default Ionic port
    "http://localhost:4200",  # another common port for development
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    logger.debug("Hello World")
    return {"Hello": "World"}

@app.get("/ready")
async def ready():
    result = session.execute(text("SELECT now();")).fetchall()
    logger.debug("Ready %s", result)
    return {"Hello": "World"}

# Include the new router
app.include_router(api_router)


@app.exception_handler(Exception)
async def exception_handler(request, exc):
    resp = {
        "error": exc.__class__.__name__,
        "messsage": exc.message
    }
    return JSONResponse(status_code=exc.status_code, content=resp)
