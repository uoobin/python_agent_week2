from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from middleware.tasks import get_usage
# Create your views here.
class BackgroundTasks(APIView):
    def get(self, request):
        get_usage(repeat=5)
        return Response()