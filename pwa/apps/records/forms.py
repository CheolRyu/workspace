from . import models 
from django import forms


class RecordForm(forms.ModelForm):
	class Meta:
		fields = ('title', 'sex', 'age', 'phone', 'surgery_history')
		model = models.Record
