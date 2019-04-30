from django.urls import path
from .views import show_taskLists,show_current_taskList, TaskLists,TaskListsDetail,UserList, logout,login
    # show_current_taskList, show_current_tasks
# urlpatterns = [
#     path('task_lists/', show_taskLists),
#     path('task_lists/<int:pk>/', show_current_taskList),
#     # path('task_lists/<int:pk>/tasks/', show_current_tasks)
# ]

urlpatterns = [
    path('task_lists/', TaskLists.as_view()),
    path('task_lists/<int:pk>/', TaskListsDetail.as_view()),
    # path('task_lists/<int:pk>/tasks/', show_current_tasks)
    path('users/', UserList.as_view()),
    path('login/',login),

]
