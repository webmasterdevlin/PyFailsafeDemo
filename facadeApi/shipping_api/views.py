from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import http.client
import json
import logging
from retrying import retry
from circuitbreaker import circuit

logger = logging.getLogger(__name__)


@circuit(failure_threshold=2, expected_exception=ConnectionError, recovery_timeout=60)
@retry(stop_max_attempt_number=10, stop_max_delay=30000, wait_fixed=3000)
@api_view(['GET'])
def shipping(request, shipping_id):
    if request.method == 'GET':
        connection = http.client.HTTPConnection("localhost", 5002)
        connection.request("GET", "/api/todos/{}".format(shipping_id))
        response = connection.getresponse()
        if response.status == 500:
            logger.error('--> FacadeApi RECEIVED a FAILURE')
            raise ConnectionError("Can't connect after 10 retries")
        else:
            logger.error('--> FacadeApi RECEIVED a SUCCESS')
            result = response.read()
            json_data: dict = json.loads(result.decode("utf-8"))
            return Response(json_data, status=status.HTTP_200_OK)
