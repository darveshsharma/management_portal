from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from ..form import EmployeeSignUpForm,ManagerSignUpForm,AdminvSignUpForm,LeaveForm
from django.contrib.auth.forms import AuthenticationForm
from ..models import User,Leave

class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def EmployeeCreateLeave(request):
    form = LeaveForm(request.user, request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print('Saved form')
            form.save(request.user)
            form =LeaveForm(request.user)
    context = {
        'form': form,
        'user': request.user,
    }
    return render(request, 'leave_form.html',context)