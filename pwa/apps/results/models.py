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
from apps.survey.models import (Question, 
HighInsulin,
LowThyroid,
HighCortisol,
LowCortisol,
HighAndrogen,
LowAndrogen,
EstrogenDominance,
EstrogenPregnancy
)


# Create your models here.
class SurveyResult(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='survey_result')
	high_insulin_set = models.ForeignKey(HighInsulin, on_delete=models.CASCADE, related_name='high_insulin_sets')
	low_thyroid_set = models.ForeignKey(LowThyroid, on_delete=models.CASCADE, related_name='low_thyroid_sets')
	high_cortisol_set = models.ForeignKey(HighCortisol, on_delete=models.CASCADE, related_name='high_cortisol_sets')
	low_cortisol_set = models.ForeignKey(LowCortisol, on_delete=models.CASCADE, related_name='low_cortisol_sets')
	high_androgen_set = models.ForeignKey(HighAndrogen, on_delete=models.CASCADE, related_name='high_androgen_sets')
	low_androgen_set = models.ForeignKey(LowAndrogen, on_delete=models.CASCADE, related_name='low_androgen_sets')
	estrogen_dominance_set = models.ForeignKey(EstrogenDominance, on_delete=models.CASCADE, related_name='estrogen_dominance_sets')
	estrogen_pregnancy_set = models.ForeignKey(EstrogenPregnancy, on_delete=models.CASCADE, related_name='estrogen_pregnancy_sets')

class IndivisualValue(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question"), 
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='single_user')