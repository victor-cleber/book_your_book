from django.contrib import admin
from .models import User

#admin.site.register(User) or
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'password')

