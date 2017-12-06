from django.contrib import admin

from crud_ws.apps.tasks.models import Task


class TaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(Task, TaskAdmin)
