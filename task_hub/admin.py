from django.contrib import admin

from task_hub.models import Task, TaskType


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "deadline", "priority")
    list_filter = ("priority",)
    search_fields = ("name",)

@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
