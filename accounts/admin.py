import imp
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *

class CustomAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser

    list_display =["username", "email", "is_staff"]
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets

admin.site.register(CustomUser, CustomAdmin)
    