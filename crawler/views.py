from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostObjectSerializer
from .parser import Parser


@api_view(['POST'])
def parse_url(request):
    '''
    Takes url and depth as input and returns crawled image urls
    '''

    serializer = PostObjectSerializer(data=request.data)
    if serializer.is_valid():
        parser = Parser(serializer.data['url'], serializer.data['depth'])
        return Response(parser.results, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
