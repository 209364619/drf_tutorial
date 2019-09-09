from django.shortcuts import render
from django.contrib.auth.models import User,Group
from quickstart.serializers import UserSerializer,GroupSerializer
from rest_framework import viewsets
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    '''
    允许用户查看或编辑的api路径
    '''
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    '''
    允许查看或编辑api的组路径
    '''

    queryset = User.objects.all()
    serializer_class = GroupSerializer

