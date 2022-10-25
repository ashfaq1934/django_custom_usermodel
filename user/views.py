from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from user.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

def api_users(request):
    try:
        users = User.objects.all()
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        print(users)
        serializer = UserSerializer(users)
        return Response(serializer.data)
