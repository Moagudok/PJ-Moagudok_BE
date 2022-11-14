from django.contrib import admin
from sharedb.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass