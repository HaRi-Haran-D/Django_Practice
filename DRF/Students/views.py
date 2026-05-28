from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student

# Create your views here.
class StudentAPI(APIView):

    def get(self, request):
        all_students = Student.objects.all()
        return Response(all_students)

    def post(self, request):
        print(request.data)
        new = Student(name= request.data['name'], age=request.data['age'])
        new.save()
        return Response("New Student Created")