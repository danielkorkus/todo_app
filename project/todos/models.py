from django.db import models

# Creating ORM model for todo app table
class Todo(models.Model):
    name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)