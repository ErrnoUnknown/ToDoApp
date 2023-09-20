from django.apps import AppConfig


class ToDoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todoapp'  # Make sure this matches the actual app name.