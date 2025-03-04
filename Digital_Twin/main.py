import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

import settings
from preprocessing.main import DataProcessor
from utility.common import format_logger

try:
    logging.basicConfig(level=settings.LOG_LEVEL)
except TypeError:
    logging.error(f"Log level {settings.LOG_LEVEL} invalid. Setting log level to {settings.DEFAULT_LOG_LEVEL}.")
    logging.basicConfig(level=settings.DEFAULT_LOG_LEVEL)
logger = logging.getLogger(__name__)
format_logger(logger)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

class DataRequest(BaseModel):
    data: dict

stored_request_data: Optional[dict] = None
stored_results: Optional[dict] = None

@app.get("/")
async def read_root():
    return {"message": "Welcome to the EDIAQI Digital Twin application!"}

@app.post("/run")
async def run_script(request: DataRequest):
    global stored_request_data, stored_results
    stored_request_data = request.data
    request_data = request.data
    data_processor = DataProcessor()
    for _ in range(100):
        stored_results = data_processor.run(request_data)
        for target in settings.TARGETS_FOR_ML_MODELS:
            request_data["indoor"][settings.COLUMNS_IN_INPUT[target]] = stored_results[target]['With_filter']
    return {"results": stored_results}

@app.get("/results")
async def get_results():
    if stored_results is None:
        return {"message": "No results available. Please send a POST request to /run first."}
    return {"results": stored_results}

@app.get("/data")
async def get_request_data():
    if stored_request_data is None:
        return {"message": "No request data available. Please send a POST request to /run first."}
    return {"data": stored_request_data}
