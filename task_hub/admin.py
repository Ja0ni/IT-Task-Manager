from django.contrib import admin

from task_hub.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "deadline", "priority")
    list_filter = ("priority",)
    search_fields = ("name",)
