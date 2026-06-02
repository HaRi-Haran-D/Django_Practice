from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.StudentAPI.as_view(), name="api"),
    path('api/<int:id>/', views.StudentAPI.as_view(), name="apipatch"),
    path('task/', views.TaskView.as_view(), name="taskview"),
    path('task/<int:id>/', views.TaskView.as_view(), name="taskview"),
]