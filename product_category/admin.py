from django.contrib import admin
from product_category.models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name','slug','created')

admin.site.register(Category, CategoryAdmin)

