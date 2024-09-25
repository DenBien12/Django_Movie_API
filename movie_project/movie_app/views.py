from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import Movies
from .serializers import MovieSerializer

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
            'director': request.data.get('director'),
            'released_date': request.data.get('released_date')
        }
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MoviesDetailApiView(APIView):

    def get_object(self, movie_id):
        try:
            return Movies.objects.get(id=movie_id)
        except Movies.DoesNotExist:
            return None

    def get(self, request, movie_id, *args, **kwargs):
        movie_instace = self.get_object(movie_id)
        if not movie_id:
            return Response(
                {"res": "Object does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = MovieSerializer(movie_instace)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, movie_id, *args, **kwargs):
        movie_instace = self.get_object(movie_id)
        if not movie_instace:
            return Response(
                {'res': "Object does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'director': request.data.get('director'),
            'released_date': request.data.get('released_date')
        }
        serializer = MovieSerializer(instance=movie_instace ,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)