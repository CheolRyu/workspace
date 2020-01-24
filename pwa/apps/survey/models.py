from django.db import models
from django.utils.text import slugify
# Create your models here.
import misaka
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()


class Question(models.Model):
	question_text = models.TextField()
	def __str__(self):
		return self.question_text

class Option(models.Model):
	user_choice = models.IntegerField()
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class HighInsulin(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	user_choice = models.ForeignKey(Option, on_delete=models.CASCADE)

class LowThyroid(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	user_choice = models.ForeignKey(Option, on_delete=models.CASCADE)
class HighCortisol(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	user_choice = models.ForeignKey(Option, on_delete=models.CASCADE)
class LowCortisol(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	user_choice = models.ForeignKey(Option, on_delete=models.CASCADE)

class HighAndrogen(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	user_choice = models.ForeignKey(Option, on_delete=models.CASCADE)
class LowAndrogen(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	user_choice = models.ForeignKey(Option, on_delete=models.CASCADE)

class EstrogenPregnancy(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	user_choice = models.ForeignKey(Option, on_delete=models.CASCADE)
class EstrogenDominance(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	user_choice = models.ForeignKey(Option, on_delete=models.CASCADE)







