from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from .models import Task, Project
from django.urls import reverse
from crispy_forms.layout import Button, Submit
from crispy_forms.bootstrap import FormActions
from django.urls import reverse_lazy
from .forms import CreateForm, EditForm


class TaskListView(LoginRequiredMixin, ListView):
    template_name = 'tasks.html'
    models = Task

    def get(self, request):
        tasks = Task.objects.all()
        return render(request, self.template_name, {'tasks': tasks})


class TaskNewView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasknew.html'
    form_class = CreateForm
    login_url = 'login'
    FormActions(
        Submit('save', 'Save changes'),
        Button('cancel', 'Cancel')
    )

    def get_success_url(self):
        return reverse('taskslist')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'taskupdate.html'
    form_class = EditForm
    login_url = 'login'


    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('taskslist')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'taskdelete.html'
    success_url = reverse_lazy('taskslist')

