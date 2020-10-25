# Generated by Django 2.2.4 on 2020-10-24 22:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('project_name', models.CharField(blank=True, max_length=255, null=True)),
                ('project_description', models.CharField(blank=True, max_length=255, null=True)),
                ('project_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_no', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('task', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('note', models.TextField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, choices=[('Select Status', 'Select Status'), ('Backlog', 'Backlog'), ('Working in Progress', 'Working in Progress'), ('Testing', 'Testing'), ('Done', 'Done')], max_length=50, null=True)),
                ('work_creat_date', models.DateTimeField(auto_now_add=True)),
                ('work_code_date', models.DateTimeField(blank=True, null=True)),
                ('work_test_date', models.DateTimeField(blank=True, null=True)),
                ('work_done_date', models.DateTimeField(blank=True, null=True)),
                ('create_by', models.ForeignKey(blank=True, default='Created by', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('employee_code', models.ForeignKey(blank=True, default='Coded by', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('employee_test', models.ForeignKey(blank=True, default='Tested by', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.Project')),
            ],
        ),
    ]
