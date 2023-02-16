# -*- coding: utf-8 -*-
import django.views.generic.edit
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.urls import path, reverse_lazy

app_name = 'custom_auth'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('change_password/', auth_views.PasswordChangeView.as_view() ),
    #path('change_password/', django.core ),
    path('gigi/', django.views.generic.edit.CreateView.as_view(form_class=UserCreationForm, template_name='registration/login.html', success_url=reverse_lazy("custom_auth:login"))),



]
