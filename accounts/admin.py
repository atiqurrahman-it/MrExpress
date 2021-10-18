from django.contrib import admin

from accounts.models import User_Profile


# Register your models here.

class userprofileAdmin(admin.ModelAdmin):
    list_display = ['id','user','full_name', 'date_joined', 'image_tag']
    list_display_links=('user','full_name',)


admin.site.register(User_Profile, userprofileAdmin)
