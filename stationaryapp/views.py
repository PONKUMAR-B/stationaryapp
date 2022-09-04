from http.client import HTTPResponse
from django.shortcuts import HttpResponse
from rest_framework import viewsets

from .serializers import ProductSerializer
from .models import Products

# Create your views here.

class ProductView(viewsets.ModelViewSet):
   queryset = Products.objects.all()
   serializer_class = ProductSerializer

    