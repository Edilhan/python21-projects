from django.urls import URLPattern, path
from .views import RegisterAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    
]