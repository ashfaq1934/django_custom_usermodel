from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from user.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView

User = get_user_model()


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
