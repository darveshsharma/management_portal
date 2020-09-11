from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from ..form import EmployeeSignUpForm,ManagerSignUpForm,AdminvSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from ..models import User

def register(request):
    return render(request, '../templates/register.html')

class adminv_register(CreateView):
    model = User
    form_class = AdminvSignUpForm
    template_name = '../templates/adminv_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

