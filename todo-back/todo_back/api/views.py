import json
from django.shortcuts import render
from api.models import TaskList, Task
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.serializers import TaskListSerializer, TaskListSerializer2, TaskSerializer
# Create your views here.
@csrf_exempt
def show_taskLists(request):
    if request.method == 'GET':
        taskLists = TaskList.objects.all()
        serializer = TaskListSerializer2(taskLists, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        serializer = TaskListSerializer2(data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    return JsonResponse({'error': 'bad request'})
@csrf_exempt
def show_current_taskList(request, pk):
    try:
        taskList = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({{'error': str(e)}}, safe=False)
    if request.method == 'GET':
        serializer = TaskListSerializer(taskList)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = TaskListSerializer(instance=taskList, data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        taskList.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})
def show_current_tasks(request, pk):
    try:
        taskList = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({{'error': str(e)}}, safe=False)
    if request.method == 'GET':
        tasks = taskList.task_set.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse({'error': 'bad request'})
