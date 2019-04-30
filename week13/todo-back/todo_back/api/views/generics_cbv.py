from ..models import TaskList, Task
from ..serializers import TaskListSerializer, TaskListSerializer2, TaskSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class TaskLists(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        taskLists = TaskList.objects.all()
        # .for_user_order_by_name(self.request.user)
        return taskLists

    def get_serializer_class(self):
        return TaskListSerializer2


class TaskListsDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset=TaskList.objects.all()
    serializer_class=TaskListSerializer
