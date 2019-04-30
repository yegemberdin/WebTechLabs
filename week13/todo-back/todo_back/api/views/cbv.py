from ..models import TaskList, Task
from ..serializers import TaskListSerializer, TaskListSerializer2, TaskSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

class TaskLists(APIView):

    def get(self,request):
        taskLists = TaskList.objects.all()
        serializer = TaskListSerializer2(taskLists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskListSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TaskListsDetail(APIView):

    def get_object(self,pk):
         try:
             return TaskList.objects.get(id=pk)
         except TaskList.DoesNotExist:
             # raise Http404
             return False,Response({'error': 'not found'},status=status.HTTP_404_NOT_FOUND)
    def get(self, request,pk):

        found,taskList=self.get_object(pk)
        if found:
            serializer = TaskListSerializer(taskList)
            return Response(serializer.data)
        return taskList

    def put(self, request,pk):
        taskList=self.get_object(pk)
        serializer = TaskListSerializer(instance=taskList, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self, request,pk):
        taskList=self.get_object(pk)
        taskList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
