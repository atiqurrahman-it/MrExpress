from django.db import models
from product_category.models import Category
# Create your models here.

class Product(models.Model):
    status = (
        ('True',True),
        ('False',False),
    )

    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    details = models.TextField()
    image = models.ImageField(upload_to='product_pic/')
    New_price = models.DecimalField(max_digits=15,decimal_places=2)
    Old_price = models.DecimalField(max_digits=15,decimal_places=2)
    stock=models.IntegerField()
    status = models.CharField(max_length=50, choices=status)
    # product_amount = models.IntegerField(default=0)
    # min_product_amount = models.IntegerField(default=4)
    slug = models.SlugField(null=True,unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
