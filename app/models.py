from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class UserRegisterModel(models.Model):
    Name = models.CharField(max_length=100)
    DOB = models.DateField()
    Email = models.EmailField(unique=True)
    Phone_number = PhoneNumberField(default=None)

    
    
