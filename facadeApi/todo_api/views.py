from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import http.client
import json
import logging
from retrying import retry
from circuitbreaker import circuit

logger = logging.getLogger(__name__)


class TodoApiView(APIView):

    @circuit(failure_threshold=2, expected_exception=ConnectionError, recovery_timeout=60)
    @retry(stop_max_attempt_number=10, stop_max_delay=30000, wait_fixed=3000)
    def get(self, request, todo_id, *args, **kwargs):
        connection = http.client.HTTPConnection("localhost", 5002)
        connection.request("GET", "/api/todos/{}".format(todo_id))
        response = connection.getresponse()
        if response.status == 500:
            logger.error('--> FacadeApi RECEIVED a FAILURE')
            raise ConnectionError("Can't connect after 10 retries")
        else:
            logger.error('--> FacadeApi RECEIVED a SUCCESS')
            result = response.read()
            json_data: dict = json.loads(result.decode("utf-8"))
            return Response(json_data, status=status.HTTP_200_OK)
