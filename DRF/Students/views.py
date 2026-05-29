from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student, Task
from .serializers import TaskSerializer

# Create your views here.
class StudentAPI(APIView):

    def get(self, request):
        all_students = Student.objects.all()
        stud_list = []
        for i in all_students:
            student_dict = {
                "id": i.id,
                "name": i.name,
                "age": i.age,
            }
            stud_list.append(student_dict)
        return Response(stud_list)

    def post(self, request):
        print(request.data)
        new = Student(name= request.data['name'], age=request.data['age'])
        new.save()
        return Response("New Student Created")

    def patch(self, request, id):
        student_data = Student.objects.filter(id=id)
        student_data.update(name= request.data['name'], age=request.data['age'])
        return Response("Student Data Updated")

    def put(self, request, id):
        student_data = Student.objects.filter(id=id)
        student_data.update(name= request.data['name'], age=request.data['age'])
        return Response("Student Data Updated")

    def delete(self, request, id):
        student_data = Student.objects.get(id=id)
        student_data.delete()
        return Response("Student Data Deleted")


class TaskView(APIView):

    def post(self, request):
        new_task = TaskSerializer(data=request.data)
        if new_task.is_valid():
            new_task.save()
            return Response("New Task Added")
        else:
            return Response(new_task.errors)

    def get(self, request):
        all_task = Task.objects.all()
        task_data = TaskSerializer(all_task, many=True)
        return Response(task_data.data)

class TaskViewByID(APIView):

    def get(self, request, id):
        get_task = Task.objects.get(id=id)
        task_data = TaskSerializer(get_task)
        return Response(task_data.data)

    def patch(self, request, id):
        task = Task.objects.get(id=id)
        update_task = TaskSerializer(task, data=request.data, partial=True)
        if update_task.is_valid():
            update_task.save()
            return Response("Task Updated")
        else:
            return Response(update_task.errors)

    def put(self, request, id):
        task = Task.objects.get(id=id)
        update_task = TaskSerializer(task, data=request.data, partial=True)
        if update_task.is_valid():
            update_task.save()
            return Response("Task Updated")
        else:
            return Response(update_task.errors)
    
    def delete(self, request, id):
        task = Task.objects.get(id=id)
        task.delete()
        return Response("Task Deleted")