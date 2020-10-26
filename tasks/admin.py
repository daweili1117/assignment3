from django.contrib import admin

# Register your models here.
from django.contrib import admin
# from .forms import UserCreationForm, UserChangeForm
from .models import Project, Task


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ['project_id',
                    'project_manager',
                    'project_name',
                    'project_description',
                                   ]


class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = [
        'task_no',
        # 'create_by',
        'employee_code',
        'employee_test',
        'project',
        'task',
        'description',
        'note',
        'work_creat_date',
        'work_code_date',
        'work_test_date',
        'work_done_date',
        'status']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)