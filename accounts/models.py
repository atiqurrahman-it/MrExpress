from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=250, blank=True)
    address_1 = models.TextField(blank=True)
    img = models.ImageField(upload_to='/coustomer')
    city = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name + "'s profile"
