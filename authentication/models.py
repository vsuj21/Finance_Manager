from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class user_registration(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.username