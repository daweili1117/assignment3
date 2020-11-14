from django import forms
from .models import Task, Project
from django.forms import ModelForm


class CreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task',
                  'project',
                  'description',
                  'note',
                  'status',
                  'create_by'
                  )

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.fields['task'].required = True
        self.fields['project'].required = True
        self.fields['create_by'].required = True


class DateInput(forms.DateInput):
    input_type = 'date'


class EditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = fields = (
            'task_no',
            'task',
            'project',
            'status',
            'employee_code',
            'work_code_date',
            'employee_test',
            'work_test_date',
            'work_done_date',
            'description',
            'note',
        )
        widgets = {
            'work_code_date': DateInput(),
            'work_test_date': DateInput(),
            'work_done_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.fields['task'].required = True
        self.fields['project'].required = True


# class DetailForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = fields = (
#             'task_no',
#             'task',
#             'project',
#             # 'project_description',
#             'status',
#             'create_by',
#             'employee_code',
#             'work_code_date',
#             'employee_test',
#             'work_test_date',
#             'work_done_date',
#             'description',
#             'note',
#         )
