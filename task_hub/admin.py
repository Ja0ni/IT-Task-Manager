from django.contrib import admin

from task_hub.models import Task, TaskType, Position, Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "position", "list_teams"]
    list_filter = ["position"]
    search_fields = ["username", "first_name", "last_name"]

    def list_teams(self, obj):
        return ", ".join([team.name for team in obj.teams.all()])
    list_teams.short_description = "Teams"


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


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["name"]
