from django.contrib.auth.models import AbstractUser
from django.db import models

Role = (
    ('Select Status', "Select Status"),
    ('Business Analysis', "Business Analysis"),
    ('UX Designer', "UX Designer"),
    ('Quality Assurance', "Quality Assurance"),
    ('Front-end Developer', "Front-end Developer"),
    ('Back-end Developer', "Back-end Developer"),
    ('Fullstack Developer', "Fullstack Developer"),
    ('Manager', "Manager"),
)


class CustomUser(AbstractUser):
    is_employee = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=True)
    role = models.CharField(max_length=50, choices=Role, null=True, blank=True)
    year_of_experience = models.PositiveIntegerField(null=True, blank=True)
    employee_cell_phone = models.CharField(max_length=50, default=' ', null=True, blank=True)

    def __str__(self):
        return "%s" % self.username


class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    skill = models.CharField(max_length=50, default='Skills', null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.user, self.skill)


class Manager(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    PMP_certificate_number = models.CharField(max_length=50, default='please type in your PMP certificate number', null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.user, self.PMP_certificate_number)
