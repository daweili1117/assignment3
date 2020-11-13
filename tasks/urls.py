from django.urls import path
from .views import TaskListView, TaskNewView



urlpatterns = [
    path('tasklist/', TaskListView.as_view(), name='taskslist'),
    path('tasknew/', TaskNewView.as_view(), name='TaskNew'),
    # path('workOrderNew/', workOrderCreatView.as_view(), name='workOrderNew'),
    # path('<int:pk>/edit/', workOrderEditView.as_view(), name='work_order_edit'),
    # path('<int:pk>/', WorkOrdeDetailView.as_view(), name='work_order_pull'),
    #
]
