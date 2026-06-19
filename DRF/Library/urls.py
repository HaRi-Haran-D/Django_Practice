from django.urls import path, include
# from .router import library_router
from rest_framework.routers import DefaultRouter
from .views import *

library_router = DefaultRouter()
library_router.register(r'book', BookViewSet)


urlpatterns = [
    path('api/', include(library_router.urls)),
    path('laptop/', LaptopView.as_view()),
    path('laptop/<int:pk>/', LaptopViewByID.as_view()),
]