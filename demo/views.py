from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

# Create your views here.

# def first(request):
#     books = Book.objects.all()
#     return render(request, 'first_temp.html',{'books': books})

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
