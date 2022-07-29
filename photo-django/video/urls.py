from django.urls import path
from .views import VideoApiView

urlpatterns = [
    path('video/', VideoApiView.as_view()),
]
