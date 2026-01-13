from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

# Create your views here.

def first(request):
    books = Book.objects.all()
    return render(request, 'first_temp.html',{'books': books})

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
