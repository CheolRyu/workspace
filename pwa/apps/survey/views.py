from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.http import Http404
# from braces.views import SelectRelatedMixin
# from .models import Record
# from . import forms


class IndexView(LoginRequiredMixin, generic.TemplateView):
	template_name = 'survey/index.html'