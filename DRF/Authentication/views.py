from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import *
from .serializers import *


# Create your views here.

class UserView(APIView):

    def post(self, request):
        # user_data = UserSerializer(data=request.data)
        # if user_data.is_valid():
        #     user_data.save()
        #     return Response("User Added")
        # return Response(user_data.errors)

        new_user = User(username = request.data['username'], is_superuser = request.data['is_superuser'])
        new_user.set_password(request.data['password'])
        new_user.save()
        return Response("New User Created")


class UserLoginView(APIView):

    def post(self, request):
        user_verification = authenticate(username= request.data['username'], password= request.data['password'])
        if user_verification == None:
            return Response("Invalid Username or Password")
        else:
            print(f"Username: {user_verification.username} Created_at:{user_verification.date_joined}")
            return Response('Valid User')