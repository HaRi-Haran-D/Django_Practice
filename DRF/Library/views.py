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



"""

generics.CreateAPIView - used to add data to database
generics.ListAPIView - used to get all data from database
generics.RetrieveAPIView - used to get data by id from database
generics.UpdateAPIView - used to update a data from database by id
generics.DestroyAPIView - used to delete a data from database by id
generics.ListCreateAPIView - used to get all from database and also can post new data
generics.RetrieveDestroyAPIView - used to get data by id and delete the data
generics.RetrieveUpdateView - used to get data by id and also update the data
generics.RetrieveUpdateDestroyAPIView - used to get data by id and also update, delete the data

"""

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
