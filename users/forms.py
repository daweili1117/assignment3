from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email',  'is_employee', 'is_manager', 'role', 'year_of_experience', 'employee_cell_phone')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email',  'is_employee', 'is_manager', 'role', 'year_of_experience', 'employee_cell_phone')
