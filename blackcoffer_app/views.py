from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics,filters
from .models import Sale, Event, DataPoint
from .serializers import SaleSerializer,DataPointSerializer,EventSerializer
from rest_framework import DjangoFilterBackend

class Product_detail(viewsets.ViewSet):

    def dashboard(request):
        sales_data = Sale.objects.all()
        return render(request, 'backcoffer_app/dashboard.html', {'sales_data': sales_data})

class SaleList(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class DataPointList(generics.ListCreateAPIView):
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer

class DataPointDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer

class DataPointFilteredList(generics.ListAPIView):
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filterset_fields = {
        'year': ['exact', 'gte', 'lte'],
        'topics': ['exact', 'icontains'],
        'sector': ['exact', 'icontains'],
        'region': ['exact', 'icontains'],
        'pest': ['exact', 'icontains'],
        'source': ['exact', 'icontains'],
        'swot': ['exact', 'icontains'],
        'country': ['exact', 'icontains'],
        'city': ['exact', 'icontains'],
    }




