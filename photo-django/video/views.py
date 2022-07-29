from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import VideoSerializer

class VideoApiView(APIView):
    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response('Video Created', status = 200)

