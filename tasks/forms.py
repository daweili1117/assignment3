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

#
# class Editform(forms.ModelForm):
#     class Meta:
#         model = Work_order
#         fields = fields = ('description','building_id', 'apt_id','status','request_by', 'phone',  'worker', 'time', 'cost', 'note')
#
#     def __init__(self, *args, **kwargs):
#         super(Editform, self).__init__(*args, **kwargs)
#        # self.fields['description'].widget.attrs['readonly'] = True
#        # self.fields['phone'].widget.attrs['readonly'] = True
#         self.fields['building_id'].widget.attrs['disabled'] = True
#         self.fields['apt_id'].widget.attrs['disabled'] = True
#         #self.fields['request_by'].widget.attrs['readonly'] = True