from rest_framework import serializers


class PostObjectSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)
    depth = serializers.IntegerField(required=True)
