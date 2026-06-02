from rest_framework.serializers import ModelSerializer
from .models import Student, Task, RankSheet

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','taskname', 'description']

class RankSheetSerializer(ModelSerializer):
    class Meta:
        model = RankSheet
        fields = '__all__'