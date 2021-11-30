from django.contrib import admin
from .models import Task, Check

# Register your models here.

class CheckInline(admin.StackedInline):
    model = Check
    extra = 0


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_opening', 'date_of_created']
    list_filter = ['owner']
    inlines = [
        CheckInline,
    ]

@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_display = ['id', 'task', 'user', 'time_checked']
    list_filter = ['task', 'user']
    search_fields = ['id']