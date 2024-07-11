from django.db import models

# Create your models here.

class Signup(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    phone_number = models.CharField(max_length = 20)
    password = models.CharField(max_length = 100)
    confirm_password = models.CharField(max_length = 100)