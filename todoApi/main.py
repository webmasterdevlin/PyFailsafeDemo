from fastapi import FastAPI
from routers import todo
import logging

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


app = FastAPI(title="Todo Service")


app.include_router(todo.router, prefix="/api", tags=["todos"])
