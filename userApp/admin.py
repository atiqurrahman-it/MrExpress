from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm

# Register your models here.
from .models import User


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = (
    'email', 'username', 'first_name', 'last_name', 'is_admin', 'is_staff', 'last_login', 'date_joined',)
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name', 'last_name', 'password',)}),
        ('Permissions', {'fields': ('is_admin', 'is_staff')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'is-active', 'first_name', 'last_name', 'password1', 'password2',),
        }),
    )
    search_fields = ('email',)
    ordering = ('-date_joined',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
