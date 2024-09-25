from django.urls import path, include
from .views import (
    MovieApiView,
    MoviesDetailApiView
)

urlpatterns = [
    path('api', MovieApiView.as_view()),
    path('api/<int:movie_id>/', MoviesDetailApiView.as_view())
]