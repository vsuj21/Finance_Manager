from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class Expense(models.Model):
    
    description = models.TextField()
    date = models.DateTimeField(default=now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        ordering: ['-date']

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'