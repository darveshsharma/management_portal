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
    print("1st line")
    form = LeaveForm(request.user, request.POST or None)
    print("1st line")
    if request.method == 'POST':
        print("1st line")
        if form.is_valid():
            print("1st line")
            print('Saved form')
            print("1st line")
            form.save(request.user)
            print("1st line")
            form =LeaveForm(request.user)
            print("1st line")
    context = {
        'form': form,
        'user': request.user,
    }
    print("1st line")
    return render(request, 'leave_form.html',context)