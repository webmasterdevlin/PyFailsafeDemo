from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import http.client
import json
from retrying import retry
from circuitbreaker import circuit
from failsafe import Failsafe, RetryPolicy


class TodoApiView(APIView):

    @retry(stop_max_delay=60000, stop_max_attempt_number=10, wait_fixed=3000)
    # @circuit(failure_threshold=3, expected_exception=ConnectionError, recovery_timeout=60)
    def get(self, request, todo_id, *args, **kwargs):
        connection = http.client.HTTPConnection("localhost", 5002)
        connection.request("GET", "/api/todos/{}".format(todo_id))
        response = connection.getresponse()
        if response.status != 200:
            raise ConnectionError("Error")
        else:
            result = response.read()
            json_data: dict = json.loads(result.decode("utf-8"))
            return Response(json_data, status=status.HTTP_200_OK)
