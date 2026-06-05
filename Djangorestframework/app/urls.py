from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentView.as_view()),
    path('<int:id>/', views.StudentView.as_view())
]
