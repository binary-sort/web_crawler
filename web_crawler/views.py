from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def hello_world(request):
    '''
    Returns hello world response
    '''

    return Response({'key': 'Hello World'}, status=status.HTTP_200_OK)
