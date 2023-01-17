#from django
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

#from Project
from .models import Task

class CustomerLoginView(LoginView):
    """ 
    name: CustomerLoginView
    descrption: class for login
    """
    template_name = "base/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('list')

class RegisterPage(FormView):
    """ 
    name:  RegisterPage
    descrption: class for Registrating
    """
    template_name = "base/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("list")

#to save the form and authenticate the user
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return  super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('list')
        return super(RegisterPage, self).get(*args, **kwargs)

# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    """ 
    name: TaskList
    descrption: This class permit the listing out the different tasks
    """
    model = Task
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"]= context['tasks'].filter(user=self.request.user)
        context['count']= context['tasks'].filter(complete=False).count()

#handle the search bar for items
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks']= context['tasks'].filter(title__icontains=search_input) #(title__startswith=search_input) this search for title that start with
        context['search_input'] = search_input
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    """ 
    name: TaskDetail
    descrption: This class give detail on a particular task
    """
    model = Task


class TaskCreate(LoginRequiredMixin, CreateView):
    """ 
    name: TaskCreate
    descrption: This class permit to create a task
    """
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy("list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy("list")

class TaskDelete(DeleteView):
    model = Task
    context_object_name = "tasks"
    success_url = reverse_lazy("list")

