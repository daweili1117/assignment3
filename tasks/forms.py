from django import forms

from .models import Task


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


class EditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = fields = (
            'task',
            'project',
            'description',
            'note',
            'status',
            'create_by'
        )

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.fields['task'].required = True
        self.fields['project'].required = True
        self.fields['create_by'].required = True
