from django.urls import path
from .views import Product_detail
from .views import SaleList, SaleDetail,DataPointList, DataPointDetail
from rest_framework.routers import DefaultRouter
from rest_framework import filters
from .views import DataPointList, DataPointDetail,DataPointFilteredList



urlpatterns = [

    path('sales/', SaleList.as_view(), name='sale-list'),
    path('sales/<int:pk>/', SaleDetail.as_view(), name='sale-detail'),
    path('dashboard',Product_detail.as_view({'post': 'dashboard'}),
    path('datapoints/', DataPointList.as_view(), name='datapoint-list'),
    path('datapoints/<int:pk>/', DataPointDetail.as_view(), name='datapoint-detail'),
    path('datapoints/filter/', DataPointFilteredList.as_view(), name='datapoint-filtered-list'),
]

