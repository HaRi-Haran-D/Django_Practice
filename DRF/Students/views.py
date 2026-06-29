from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student, Task, RankSheet
from .serializers import *
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404

# Create your views here.
class StudentAPI(APIView):

    def get(self, request, id=None):

        # all_students = Student.objects.all()
        # stud_list = []
        # for i in all_students:
        #     student_dict = {
        #         "id": i.id,
        #         "name": i.name,
        #         "age": i.age,
        #     }
        #     stud_list.append(student_dict)
        # return Response(stud_list)

        if id==None:
            student= Student.objects.all()
            serializer = StudentTaskSerializer(student, many=True)
            return Response(serializer.data)
        else:
            student=Student.objects.get(id=id)
            serializer = StudentTaskSerializer(student)
            return Response(serializer.data)


    def post(self, request):
        # print(request.data)
        # new = Student(name= request.data['name'], age=request.data['age'])
        # new.save()
        # return Response("New Student Created")

        new_task = Task(student_ref=request.data['student_ref'])
        task_name = request.data['task_name'],

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

    def get(self, request, id=None):
        if id == None:
            all_task = Task.objects.all()
            task_data = TaskDataSerializer(all_task, many=True)
            return Response(task_data.data)
        else:
            all_task = Task.objects.get(id=id)
            task_data = TaskDataSerializer(all_task)
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





class RankSheetView(APIView):

    def post(self, request):
        total_marks = request.data['tamil'] + request.data['english'] + request.data['maths'] + request.data['science'] + request.data['social']
        average_marks = total_marks/5

        if (request.data['tamil']>=35) and (request.data['english']>=35) and (request.data['maths']>=35) and (request.data['science']>=35) and (request.data['social']>=35):
            student_result = True
        else:
            student_result = False
        new_data = RankSheet(tamil=request.data['tamil'],english=request.data['english'],maths=request.data['maths'],science=request.data['science'],social=request.data['social'], total = total_marks, average = average_marks, result = student_result)
        new_data.save()
        return Response("Data saved")

    def get(self, request, id = None):
        if id == None:
            mark = RankSheet.objects.all()
            serializer = RankSheetSerializer(mark, many=True)
            return Response(serializer.data)
        else:
            mark = RankSheet.objects.get(id=id)
            serializer = RankSheetSerializer(mark)
            return Response(serializer.data)

    def put(self, request, id):
        marksheet = RankSheet.objects.get(id=id)
        total_marks = request.data['tamil'] + request.data['english'] + request.data['maths'] + request.data['science'] + request.data['social']
        average_marks = total_marks/5

        if (request.data['tamil']>=35) and (request.data['english']>=35) and (request.data['maths']>=35) and (request.data['science']>=35) and (request.data['social']>=35):
            student_result = True
        else:
            student_result = False

        marksheet.tamil = request.data['tamil']
        marksheet.english = request.data['english']
        marksheet.maths = request.data['maths']
        marksheet.science = request.data['science']
        marksheet.social = request.data['social']
        marksheet.total = total_marks
        marksheet.average = average_marks
        marksheet.result = student_result
        marksheet.save()

        return Response("Data Updated")

    def patch(self, request, id):
        marksheet = RankSheet.objects.get(id=id)
        total_marks = request.data['tamil'] + request.data['english'] + request.data['maths'] + request.data['science'] + request.data['social']
        average_marks = total_marks/5

        if (request.data['tamil']>=35) and (request.data['english']>=35) and (request.data['maths']>=35) and (request.data['science']>=35) and (request.data['social']>=35):
            student_result = True
        else:
            student_result = False

        marksheet.tamil = request.data['tamil']
        marksheet.english = request.data['english']
        marksheet.maths = request.data['maths']
        marksheet.science = request.data['science']
        marksheet.social = request.data['social']
        marksheet.total = total_marks
        marksheet.average = average_marks
        marksheet.result = student_result
        marksheet.save()

        return Response("Data Updated")

    def delete(self, request, delete):
        marksheet = get_object_or_404(RankSheet, id=id)
        marksheet.delete()
        return Response("Data Deleted")




@api_view(["GET", "POST"])
def task_list_create(request):

    if request.method == "GET":
        all_task = Task.objects.all()
        serializer = TaskSerializer(all_task, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        new_task = TaskSerializer(data=request.data)
        if new_task.is_valid():
            new_task.save()
            return Response("New Task Added")
        return Response(new_task.errors)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def task_update_delete(request, id):
    task_data = Task.objects.get(id=id)

    if request.method == "GET":
        serializer = TaskSerializer(task_data)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = TaskSerializer(task_data, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Task Updated")
        return Response(serializer.errors)

    elif request.method == "PATCH":
        serializer = TaskSerializer(task_data, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Task Updated")
        return Response(serializer.errors)

    elif request.method == "DELETE":
        task_data.delete()
        return Response("Task Deleted")
