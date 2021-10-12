from django.contrib import admin
from product_store.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','status','stock','created','updated']
    list_filter = ("product_name","created",)
    search_fields = ('product_name','details')
    list_per_page = 10
    prepopulated_fields = {'slug': ('product_name',)} # auto slug created


admin.site.register(Product,ProductAdmin)
