from django.contrib import admin
from .models import User
from .models import TodoList


class UserAdmin(admin.ModelAdmin):
    search_fields = ['nickname']


admin.site.register(User, UserAdmin)


class TodoListAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(TodoList, TodoListAdmin)
