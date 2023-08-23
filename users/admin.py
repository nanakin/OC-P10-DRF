from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "birth_date", "can_be_contacted", "can_data_be_shared")


admin.site.unregister(Group)
