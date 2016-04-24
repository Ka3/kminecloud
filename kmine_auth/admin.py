from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.
from kmine_auth.models import User_Profile

admin.site.register(User_Profile)

class ProfileInline(admin.StackedInline):
    model = User_Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)    