from django.urls import path,include
from .views import  adminv,manager,employee,common
urlpatterns=[
     path('', common.home, name='home'),
     path('employee/', include(([
           path('leave_form', employee.EmployeeCreateLeave, name='leave_form'),
     ], 'accounts'), namespace='employee')),
]

""" path('register/',views.register, name='register'),
     path('employee_register/',views.employee_register.as_view(), name='employee_register'),
     path('manager_register/',views.manager_register.as_view(), name='manager_register'),
     path('adminv_register/',views.adminv_register.as_view(), name='adminv_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
"""     
