from django.views.generic import ListView


from .models import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.views.generic.edit import FormView
from .models import Task, Project
from django.urls import reverse
from crispy_forms.layout import Button, Submit
from crispy_forms.bootstrap import FormActions
from django.http import HttpRequest
from .forms import CreateForm


class TaskListView(LoginRequiredMixin,ListView):
    template_name = 'tasks.html'
    models = Task

    def get(self, request):
        tasks = Task.objects.all()
        return render(request, self.template_name, {'tasks': tasks})


class TaskNewView(LoginRequiredMixin, CreateView):
    models = Task
    template_name = 'tasknew.html'
    form_class = CreateForm
    login_url = 'login'
    FormActions(
        Submit('save', 'Save changes'),
        Button('cancel', 'Cancel')
    )

    def get_success_url(self):
        return reverse('taskslist')
