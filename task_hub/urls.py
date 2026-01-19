from django.urls import path

from task_hub.views import index, WorkerCreateView, WorkerListView, WorkerDetailView, WorkerUpdateView, WorkerDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
]

app_name = "task_hub"
