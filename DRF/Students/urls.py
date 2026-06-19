from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.StudentAPI.as_view(), name="api"),
    path('api/<int:id>/', views.StudentAPI.as_view(), name="apipatch"),
    
    path('task/', views.TaskView.as_view(), name="taskview"),
    path('task/<int:id>/', views.TaskView.as_view(), name="taskview"),

    path('rank/', views.RankSheetView.as_view()),
    path('rank/<int:id>/', views.RankSheetView.as_view()),

    path('task/list/create/',views.task_list_create),
    path('task/list/create/<int:id>/',views.task_update_delete),
]
