from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.http import Http404
from braces.views import SelectRelatedMixin
from . import models
# from . import forms
# Create your views here.
# 
class HomeView(LoginRequiredMixin, generic.ListView):
	temlate_name = 'results/index.html'
	context_object_name = 'result'

	def get_queryset(self):
		return models.SurveyResult.objects.all()