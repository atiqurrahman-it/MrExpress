from django.db import models

# Create your models here.

class Category(models.Model):
    status = (
        ('True', True),
        ('False', False),
    )
    category_name=models.CharField(max_length=55,unique=True)
    short_description=models.TextField(max_length=255,blank=True)
    slug=models.SlugField(max_length=100,unique=True)
    cat_img=models.ImageField(upload_to='photos/categories',blank=True)
    status = models.CharField(max_length=50, choices=status)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name
