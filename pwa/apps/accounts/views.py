from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView
from . import forms


# Create your views here.
class SignUp(CreateView):
	form_class = forms.UserCreateForm
	success_url = reverse_lazy('home')
	template_name = 'home/registration.html'

















