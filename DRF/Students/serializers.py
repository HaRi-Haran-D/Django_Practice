from rest_framework.serializers import ModelSerializer
from .models import Student, Task, RankSheet

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class RankSheetSerializer(ModelSerializer):
    class Meta:
        model = RankSheet
        fields = '__all__'


class StudentTaskSerializer(ModelSerializer):
    all_task = TaskSerializer()
    class Meta:
        model = Student
        fields = '__all__'


class TaskDataSerializer(ModelSerializer):
    student_ref = StudentSerializer()
    class Meta:
        model = Task
        fields = "__all__"