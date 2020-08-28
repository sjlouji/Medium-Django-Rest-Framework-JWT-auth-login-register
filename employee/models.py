from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Employees(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_mobile = models.TextField()
    emp_email = models.TextField(null = True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
