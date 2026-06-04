from django.urls import path, include
from .router import library_router

urlpatterns = [
    path('api/', include(library_router.urls)),
]