from fastapi import APIRouter, HTTPException
import http.client
import json
import logging
from circuitbreaker import circuit

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/facade-todos")


@circuit(failure_threshold=2)
@router.get("/{todo_id}", response_model=dict)
def get_todo_by_id(todo_id: int) -> dict:
    connection = http.client.HTTPConnection("localhost", 5002)
    connection.request("GET", "/api/todos/{}".format(todo_id))
    response = connection.getresponse()
    if response.status != 200:
        logger.info("--> FacadeApi RECEIVED a FAILURE")
        raise HTTPException(status_code=response.status, detail="Error getting todo")
    else:
        logger.info("--> FacadeApi RECEIVED a SUCCESS")
        result = response.read()
        json_data: dict = json.loads(result.decode("utf-8"))
        return json_data
