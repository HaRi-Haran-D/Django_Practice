from rest_framework.serializers import ModelSerializer
from .models import Student, Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','taskname', 'description']