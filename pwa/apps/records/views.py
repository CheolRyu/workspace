from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.http import Http404
from braces.views import SelectRelatedMixin
from .models import Record
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
class RecordList(LoginRequiredMixin, generic.ListView):
	template_name='records/index.html'
	model = Record
	context_object_name = 'user_record'
	def get_queryset(self):
		return Record.objects.filter(user=self.request.user)

class RecordDetail(LoginRequiredMixin, generic.DetailView):
	model = Record
	template_name = 'records/record_detail.html'
	context_object_name = 'user_record'
	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(user__username__iexact=self.kwargs.get("username"))

class CreateRecord(LoginRequiredMixin, generic.CreateView, SelectRelatedMixin):
	fields = ('title', 'sex', 'age', 'phone', 'surgery_history')
	form = forms.RecordForm()
	model = Record

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return super().form_valid(form)

class DeleteRecord(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
	model = Record
	success_url = reverse_lazy('records:all')

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(user_id=self.request.user.id)

	def delete(self, *args, **kwargs):
		messages.success(self.request, 'Record has been removed.')
		return super().delete(*args, **kwargs)
















