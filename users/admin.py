from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Manager, Employee


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'username',
        'first_name',
        'last_name',
        'email',
        'employee_cell_phone',
        'is_staff',
        'is_employee',
        'is_manager',
        'role',
        'year_of_experience']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'employee_cell_phone', 'role', 'year_of_experience')}),
        ('Permissions', {'fields': ('is_superuser', 'is_active', 'is_staff', 'is_employee', 'is_manager', 'groups', 'user_permissions'), }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


class ManagerAdmin(admin.ModelAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = Manager
    list_display = ['user', 'PMP_certificate_number']


class EmployeeAdmin(admin.ModelAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = Employee
    list_display = ['user', 'skill']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Employee, EmployeeAdmin)
