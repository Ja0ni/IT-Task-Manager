from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task_hub.forms import WorkerCreateForm
from task_hub.models import Worker


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_visits": num_visits + 1,
    }
    return render(request, "task_hub/index.html", context=context)


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreateForm
    success_url = reverse_lazy("task_hub:worker-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    template_name = "task_hub/worker_list.html"
    context_object_name = "workers"
    paginate_by = 5


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    template_name = "task_hub/worker_detail.html"
    context_object_name = "worker"


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    fields = [
        "first_name",
        "last_name",
        "email",
        "position",
        "team",
    ]
    template_name = "task_hub/worker_form.html"
    success_url = reverse_lazy("task_hub:worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("task_hub:worker-list")
    template_name = "task_hub/worker_confirm_delete.html"
