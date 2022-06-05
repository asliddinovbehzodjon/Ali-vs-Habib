from django.db import models

# Create your models here.
class Todo(models.Model):
     description = models.TextField()
     start = models.DateTimeField()
     finish = models.DateTimeField()
     status = models.BooleanField(default=False)
     