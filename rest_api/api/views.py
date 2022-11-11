from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator

from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets

from api.models import TransactionData, UsageData, SearchData
from api.serializer import TransactionDataSerializer, UsageDataSerializer, SearchDataSerializer
from api.get_data import makeFile

import os
import pandas as pd
# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class TransactionDataViewSet(CreateAPIView):
    queryset = TransactionData.objects.all()
    serializer_class = TransactionDataSerializer
    
    def get(self, request):
        queryset = self.get_queryset()
        serializer = TransactionDataSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        makeFile(request.data, 'transaction_data.csv')

        return self.create(request, *args, **kwargs)

@method_decorator(csrf_exempt, name='dispatch')
class UsageDataViewSet(CreateAPIView):
    queryset = UsageData.objects.all()
    serializer_class = UsageDataSerializer
    
    def get(self, request):
        queryset = self.get_queryset()
        serializer = UsageDataSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        makeFile(request.data, 'usage_data.csv')

        return self.create(request, *args, **kwargs)

@method_decorator(csrf_exempt, name='dispatch')
class SearchDataViewSet(CreateAPIView):
    queryset = SearchData.objects.all()
    serializer_class = SearchDataSerializer
    
    # GET method
    def get(self, request):
        queryset = SearchData.objects.all()
        serializer = SearchDataSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = SearchDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            f = os.path.join(os.path.join(os.path.dirname(__file__),'../'), 'transaction_data.csv')
            df = pd.read_csv(f)
            df = df[df['timestamp'] == float(data['timestamp'])]

            df.to_csv(str(data['timestamp'])+'.csv', index=False)

            return Response(serializer.data)

        return JsonResponse(serializer.errors, status=400)
