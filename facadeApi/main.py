from fastapi import FastAPI
from routers import facade_todo
import logging

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI(title="Facade API")

app.include_router(facade_todo.router, prefix="/api", tags=["todos"])
