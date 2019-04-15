from django.urls import path
from api.views import show_taskLists, show_current_taskList, show_current_tasks
urlpatterns = [
    path('task_lists/', show_taskLists),
    path('task_lists/<int:pk>/', show_current_taskList),
    path('task_lists/<int:pk>/tasks/', show_current_tasks)
]