from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone

from task_hub.forms import WorkerCreateForm, TaskCreateForm, TeamCreateForm, ProjectCreateForm, TaskSearchForm, \
    WorkerSearchForm, TeamSearchForm
from task_hub.models import Worker, Task, Team, Project


@login_required
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "task_hub/index.html")


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreateForm
    success_url = reverse_lazy("task_hub:worker-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    template_name = "task_hub/worker_list.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = Worker.objects.all()

        form = WorkerSearchForm(self.request.GET)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            if username:
                queryset = queryset.filter(username__icontains=username)

        return queryset


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


class TaskCompleteView(LoginRequiredMixin, generic.TemplateView):
    @staticmethod
    def post(request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_complete = True
        task.save()
        return redirect("task_hub:task-detail", pk=pk)


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("task_hub:task-list")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "task_hub/task_list.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = Task.objects.all().prefetch_related("assignees")

        form = TaskSearchForm(self.request.GET)

        if form.is_valid():
            name = form.cleaned_data.get("name")
            if name:
                queryset = queryset.filter(name__icontains=name)

        if self.request.GET.get("my"):
            queryset = queryset.filter(assignees=self.request.user)

        now = timezone.now()
        for task in queryset:
            if task.deadline:
                task.is_last_day = 0 <= (task.deadline - now).days <= 1
            else:
                task.is_last_day = False

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = TaskSearchForm(self.request.GET)
        return context


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "task_hub/task_detail.html"
    context_object_name = "task"


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = [
        "name",
        "description",
        "deadline",
        "priority",
        "task_type",
        "project",
        "assignees",
    ]
    template_name = "task_hub/task_form.html"
    success_url = reverse_lazy("task_hub:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "task_hub/task_confirm_delete.html"
    success_url = reverse_lazy("task_hub:task-list")


class TeamCreateView(LoginRequiredMixin, generic.CreateView):
    model = Team
    form_class = TeamCreateForm
    success_url = reverse_lazy("task_hub:team-list")



class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Team
    template_name = "task_hub/team_list.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = Team.objects.all()

        form = TeamSearchForm(self.request.GET)

        if form.is_valid():
            name = form.cleaned_data.get("name")
            if name:
                queryset = queryset.filter(name__icontains=name)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = TeamSearchForm(self.request.GET)
        return context


class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team
    template_name = "task_hub/team_detail.html"


class TeamUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Team
    form_class = TeamCreateForm
    success_url = reverse_lazy("task_hub:team-list")


class TeamDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Team
    template_name = "task_hub/team_confirm_delete.html"
    success_url = reverse_lazy("task_hub:team-list")


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    form_class = ProjectCreateForm
    success_url = reverse_lazy("task_hub:project-list")


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    template_name = "task_hub/project_list.html"
    paginate_by = 5


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    template_name = "task_hub/project_detail.html"


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    form_class = ProjectCreateForm
    success_url = reverse_lazy("task_hub:project-list")


class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    template_name = "task_hub/project_confirm_delete.html"
    success_url = reverse_lazy("task_hub:project-list")


class ProjectAddTasksView(LoginRequiredMixin, generic.ListView):
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)

        tasks = Task.objects.filter(project__isnull=True)

        return render(
            request,
            "project_add_tasks.html",
            {
                "project": project,
                "tasks": tasks,
            }
        )

    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        task_ids = request.POST.getlist("tasks")

        Task.objects.filter(id__in=task_ids).update(project=project)

        return redirect("task_hub:project-detail", pk=project.pk)
