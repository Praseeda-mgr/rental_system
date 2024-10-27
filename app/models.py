from django.db import models
from django.contrib.auth.models import Group

# Create roles
Group.objects.get_or_create(name='Seller')
Group.objects.get_or_create(name='Client')

# Create your models here.
# class property (models.Model):
#     title = models.CharField(max_length=250)
#     owner = models.Foreignkey(User, on_delete=models.CASCADE, related_name='properties')
#     Description = models.TextField()
#     location = models.CharField(max_length=250)
#     price = models.DecimalField(max_digits=10, decimal_places=2)

