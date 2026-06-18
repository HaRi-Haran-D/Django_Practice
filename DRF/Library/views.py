from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


# Create your views here.
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class LaptopView(generics.ListCreateAPIView):

    # def get_queryset(self):
    #     return Laptop.objects.filter(brand='Asus')

    def perform_create(self, serializer):
        serializer.save(user_type="High Performance")

    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer

class LaptopViewByID(generics.RetrieveUpdateDestroyAPIView):

    def perform_update(self, serializer):
        serializer.save(user_type="Low Performance")

    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
