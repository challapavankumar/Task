from django.contrib import admin
from .models import Task
# Register your models here
@admin.register(Task)
class Admin_Task(admin.ModelAdmin):
    list_display = ['id','name','description','published']
