from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import Movies, Gerne, Director
from .serializers import MovieSerializer, GerneSerializer, DirectorSerializer

# Create your views here.

class MovieApiView(APIView):
    # 1. List all
    def get(self, request, *args, **kwargs):
        movies = Movies.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 2. Create
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'summary': request.data.get('summary'),
            'released_date': request.data.get('released_date')
        }
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
