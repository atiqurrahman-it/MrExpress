from django.db import models
from django.utils.safestring import mark_safe
# from django.contrib.auth.models import User
from userApp.models import User


# Create your models here.

class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=250, blank=True)
    address_1 = models.TextField(blank=True)
    image = models.ImageField(upload_to='coustomer/')
    city = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    verify = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />' % self.image.url)

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.full_name + "'s profile"
