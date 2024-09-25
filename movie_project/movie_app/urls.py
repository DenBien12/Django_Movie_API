from django.urls import path, include
from .views import (
    MovieApiView,
)

urlpatterns = [
    path('api', MovieApiView.as_view()),
]