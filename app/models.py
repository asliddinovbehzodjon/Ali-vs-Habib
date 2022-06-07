from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     description = models.TextField()
     start = models.DateTimeField()
     finish = models.DateTimeField()
     status = models.BooleanField(default=False)
     