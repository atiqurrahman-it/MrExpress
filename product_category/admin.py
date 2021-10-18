from django.contrib import admin
from product_category.models import Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}  # auto slug created
    list_display = ('id', 'category_name', 'slug', 'created')
    list_display_links=('id','category_name')
    search_fields = ('id', 'category_name')
    list_filter = ('category_name', 'created')


admin.site.register(Category, CategoryAdmin)
