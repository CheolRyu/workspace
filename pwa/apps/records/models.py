from django.db import models
from django.utils.text import slugify
# Create your models here.
import misaka
from phone_field import PhoneField
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()


class Record(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='records')
	title = models.CharField(max_length=225)
	sex = models.CharField(max_length=225)
	age = models.PositiveIntegerField()
	phone = PhoneField(blank=False, help_text='Contact phone number')
	created_at = models.DateTimeField(auto_now=True)
	surgery_history = models.TextField()
	surgery_history_html = models.TextField(editable=False)


	def __str__(self):
		return "User: {}, Title: {}, Sex: {}, ".format(self.user.username, self.title, self.sex)

	def save(self, *args, **kwargs):
		self.surgery_history_html = misaka.html(self.surgery_history)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('records:single', kwargs={'username':self.user.username,'pk':self.pk})

	class Meta:
		ordering = ['-created_at']
		unique_together = ['user', 'surgery_history']