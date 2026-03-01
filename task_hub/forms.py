from django import forms
from django.contrib.auth.forms import UserCreationForm

from task_hub.models import Worker, Task, Team, Project


class WorkerCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "deadline",
            "is_complete",
            "priority",
            "task_type",
            "project",
            "assignees",
        )
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(
                attrs={"class": "form-control", "rows": 3}
            ),
            "deadline": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "priority": forms.Select(attrs={"class": "form-select"}),
            "task_type": forms.Select(attrs={"class": "form-select"}),
            "project": forms.Select(attrs={"class": "form-select"}),
            "is_complete": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "assignees": forms.CheckboxSelectMultiple(),
        }


class TeamCreateForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = Team
        fields = ("name", "members")
        widgets = {
            "members": forms.CheckboxSelectMultiple(),
        }


class ProjectCreateForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = Project
        fields = (
            "name",
            "description",
            "team",
            "start_date",
            "end_date",
        )
