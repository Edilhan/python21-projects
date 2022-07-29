from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

User = get_user_model()

class TemplateView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        return Response()