from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Employee, Manager, Adminv,Leave



class EmployeeSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        employee = Employee.objects.create(user=user)
        employee.save()
        return user

class ManagerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        manager = Manager.objects.create(user=user)
        manager.save()
        return user

class AdminvSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_adminV = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        adminv = Adminv.objects.create(user=user)
        adminv.save()
        return user


class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ('start_date', 'end_date','application')

    @transaction.atomic
    def save(self,reciever):
        owner = reciever
        start_date= self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']
        application=self.cleaned_data['end_date']
        Request.objects.create(owner=owner, start_date=start_date, end_date=end_date, application=application)