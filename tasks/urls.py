from django.urls import path
from .views import TaskListView, TaskNewView, TaskUpdateView, TaskDeleteView



urlpatterns = [
    path('tasklist/', TaskListView.as_view(), name='taskslist'),
    path('tasknew/', TaskNewView.as_view(), name='TaskNew'),
    path('<int:pk>/taskupdate', TaskUpdateView.as_view(), name='TaskUpdate'),
    path('<int:pk>/tasldelete', TaskDeleteView.as_view(), name='TaskDelete'),

]
