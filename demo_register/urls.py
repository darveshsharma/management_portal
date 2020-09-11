"""demo_register URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from accounts.views import  adminv,manager,employee,common

"""
urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', common.register, name='register'),
    path('accounts/register/manager/', manager.manager_register.as_view(), name='manager_register'),
    path('accounts/register/employee/', employee.employee_register.as_view(), name='employee_register'),
    path('accounts/register/employee/', adminv.adminv_register.as_view(), name='adminv_register'),
    path('login/',common.login_request, name='login'),
    path('logout/',common.logout_view, name='logout'),
]