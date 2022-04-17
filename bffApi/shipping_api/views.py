from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def shipping(request, shipping_id):
    if request.method == 'GET':
        return Response(status=status.HTTP_200_OK, data={'id': shipping_id})
