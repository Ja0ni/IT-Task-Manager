from django.contrib.auth.models import AbstractUser
from django.db import models

from task_manager import settings


class Worker(AbstractUser):
    position = models.ForeignKey("Position", on_delete=models.CASCADE, null=True, blank=True, related_name="workers")
    team = models.ForeignKey("Team", on_delete=models.SET_NULL, null=True, blank=True, related_name="members")

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}({self.position})"


class Task(models.Model):
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    VERY_HIGH = 3
    URGENT = 4

    CHOICES_PRIORITY = (
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High"),
        (VERY_HIGH, "Very High"),
        (URGENT, "Urgent"),
    )

    name = models.CharField(max_length=63)
    description = models.TextField(max_length=500, blank=True)
    deadline = models.DateTimeField()
    is_complete = models.BooleanField(default=False)
    priority = models.IntegerField(choices=CHOICES_PRIORITY, default=LOW)
    task_type = models.ForeignKey("TaskType", on_delete=models.CASCADE, related_name="tasks")
    project = models.ForeignKey("Project", on_delete=models.CASCADE, null=True, blank=True, related_name="tasks")
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


class Team(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=63)
    description = models.TextField(max_length=500, blank=True)
    team = models.ForeignKey("Team", on_delete=models.CASCADE, null=True, blank=True, related_name="projects")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
