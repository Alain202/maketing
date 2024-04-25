from django.contrib import admin
from django.db import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from market.models import Employee
from market.models import Client


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user_id','user','phone', 'solde','parain','idparain')
    ordering = ('user_id',)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('date','idclient','nomclient','idtransfert','telephone','prenom','nomdepot','methoddepot')
    ordering = ('date',)
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = "employee"

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [EmployeeInline]
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Client,ClientAdmin)
# Register your models here.
# Register your models here.
