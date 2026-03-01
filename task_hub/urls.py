from django.urls import path

from task_hub.views import index, WorkerCreateView, WorkerListView, WorkerDetailView, WorkerUpdateView, \
    WorkerDeleteView, TaskCreateView, TaskListView, TaskDetailView, TaskCompleteView, TaskUpdateView, TaskDeleteView, \
    TeamListView, TeamCreateView, TeamUpdateView, TeamDeleteView, TeamDetailView

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
    path("teams/", TeamListView.as_view(), name="team-list"),
    path("teams/create/", TeamCreateView.as_view(), name="team-create"),
    path("teams/<int:pk>/update/", TeamUpdateView.as_view(), name="team-update"),
    path("teams/<int:pk>/delete/", TeamDeleteView.as_view(), name="team-delete"),
    path("teams/<int:pk>/", TeamDetailView.as_view(), name="team-detail"),
]

app_name = "task_hub"
