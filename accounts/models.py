from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_adminV = models.BooleanField(default=False)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

class Adminv(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)


class Leave(models.Model):
    sender=models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    reciever=models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever')
    start_date=models.DateField(auto_now=False, auto_now_add=False)
    end_date=models.DateField(auto_now=False, auto_now_add=False)
    application=models.TextField()
    torf=models.BooleanField(default=False)