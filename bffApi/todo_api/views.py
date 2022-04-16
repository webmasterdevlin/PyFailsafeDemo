from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def get_todo_by_id(request, todo_id):
    if request.method == 'GET':
        return Response(status=status.HTTP_200_OK, data={'id': todo_id})
