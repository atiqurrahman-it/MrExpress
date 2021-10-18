from django.contrib import admin
from product_store.models import Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'category', 'stock', 'status', 'created', 'updated']
    list_display_links = ('id', 'product_name')
    list_filter = ("product_name", "created",)
    search_fields = ('id','category','product_name', 'details')
    list_per_page = 10
    prepopulated_fields = {'slug': ('product_name',)}  # auto slug created


admin.site.register(Product, ProductAdmin)
