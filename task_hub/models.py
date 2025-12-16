from django.contrib.auth.models import AbstractUser
from django.db import models

from task_manager import settings


class Worker(AbstractUser):
    position = models.ForeignKey("Position", on_delete=models.CASCADE, related_name="positions")

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}({self.position})"


class Task(models.Model):
    name = models.CharField(max_length=63)
    description = models.TextField(max_length=500)
    deadline = models.DateTimeField()
    is_complete = models.BooleanField(default=False)
    priority = models.IntegerField()
    task_type = models.ForeignKey("TaskType", on_delete=models.CASCADE, related_name="task_types")
    assignees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="assigned_tasks")

    class Meta:
        ordering = ["name"]


class TaskType(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
