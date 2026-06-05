from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

class StudentView(APIView):

    def get(self, request,id=None):
        if id==None:
            stud = Student.objects.all()
            serializer = StudentSerializer(stud, many=True)
            return Response(serializer.data)
        else:
            stud = Student.objects.get(id=id)
            serializer = StudentSerializer(stud)
            return Response(serializer.data)
    
    def post(self, request):
        stud = StudentSerializer(data=request.data)
        if stud.is_valid():
            stud.save()
            return Response("Student Data Added")
        return Response(stud.errors)
    
    def put(self, request, id):
        stud = Student.objects.get(id=id)
        serializer = StudentSerializer(stud, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Student Data Updated")
        return Response(serializer.errors)
    
    def patch(self, request, id):
        stud = Student.objects.get(id=id)
        serializer = StudentSerializer(stud, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Student Data Updated")
        return Response(serializer.errors)
    
    def delete(self, request, id):
        stud = Student.objects.get(id=id)
        stud.delete()
        return Response("Student Deleted")