from django.urls import path

from task_hub.views import index, WorkerCreateView, WorkerListView, WorkerDetailView, WorkerUpdateView, \
    WorkerDeleteView, TaskCreateView, TaskListView, TaskDetailView, TaskCompleteView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/<int:pk>/complete/", TaskCompleteView.as_view(), name="task-complete"),
]

app_name = "task_hub"
