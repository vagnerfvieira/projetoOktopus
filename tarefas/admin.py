from django.contrib import admin
from .models import TodoList, Status
# Register your models here.


admin.site.register(TodoList)
admin.site.register(Status)