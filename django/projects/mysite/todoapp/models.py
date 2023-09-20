from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.TextField()
    password = models.TextField()

    def __str__(self):
        return self.nickname


class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.TextField()
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.subject