from fastapi import APIRouter, HTTPException
from random import randrange
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/todos")


@router.get("/{todo_id}", response_model=dict)
def get_todo_by_id(todo_id: int) -> dict:
    random_number = randrange(100)
    if random_number >= todo_id:
        logger.info("--> TodoService Returned 500 ERROR")
        raise HTTPException(status_code=500, detail="Todo Service is down")
    else:
        logger.info("--> TodoService Returned 200 OK")
        return {"id": todo_id, "activity": "eat"}
