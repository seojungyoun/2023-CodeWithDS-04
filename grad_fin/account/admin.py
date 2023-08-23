from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin) :
    list_display = ('username', 'name', 'email', 'phonenumber', 'birthdate')
    exclude = ('password',)