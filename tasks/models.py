from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Project(models.Model):
    project_id = models.AutoField(auto_created=True, primary_key=True)
    project_manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
                                        related_name='+')
    project_name = models.CharField(max_length=255, null=True, blank=True)
    project_description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "%s" % self.project_name
    #
    # def get_absolute_url(self):
    #     return reverse('building_detail', args=[str(self.id)])


Status = (
    ('Select Status', "Select Status"),
    ('Backlog', "Backlog"),
    ('Working in Progress', "Working in Progress"),
    ('Testing', "Testing"),
    ('Done', "Done"),
)


class Task(models.Model):
    task_no = models.AutoField(auto_created=True, primary_key=True)
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='Created by', blank=True,
                                  null=True, related_name='+')
    employee_code = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='Coded by',
                                      blank=True, null=True, related_name='+')
    employee_test = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='Tested by',
                                      blank=True, null=True, related_name='+')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default='', blank=True, null=True)
    task = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    note = models.TextField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, choices=Status, null=True, blank=True)
    work_creat_date = models.DateTimeField(auto_now_add=True)
    work_code_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    work_test_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    work_done_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return "%s" % self.task_no


# brew install graphviz
# pip install pyparsing pydot
# (venv) daweili@Daweis-MacBook-Pro MAH % python manage.py graph_models -a > erd.dot
# (venv) daweili@Daweis-MacBook-Pro MAH % python manage.py graph_models -a -g -o ERD.png