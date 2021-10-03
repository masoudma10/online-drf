from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Profile
from django.contrib.auth.models import Group


class UserAdmin(BaseUserAdmin):
    list_display = ('first_name','last_name','email','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None,{'fields':('email','first_name','last_name','password','phone')}),
        ('personal info',{'fields':('is_active',)}),
        ('Permissions',{'fields':('is_admin',)}),
    )

    add_fieldsets = (
        (None,{
            'fields':('email','first_name','last_name','password1','password2'),
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class ExtendedProfileAdmin(UserAdmin):
    inlines = (ProfileInline,)


# admin.site.unregister(User)
admin.site.register(User, ExtendedProfileAdmin)
admin.site.unregister(Group)