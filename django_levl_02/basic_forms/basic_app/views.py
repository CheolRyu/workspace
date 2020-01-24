from django.shortcuts import render
from . import forms
from user.models import User

def index(request):
	return render(request, 'basic_app/index.html')



def form_name_view(request):
	form = forms.FormName()


	if request.method == 'POST':
		form = forms.FormName(request.POST)

		if form.is_valid():
			#do somthing with it
			print('validation success!')
			print("Name:" + form.cleaned_data['name'])
			print("Email:" + form.cleaned_data['email'])
			print("Text:" + form.cleaned_data['text'])

	return render(request, 'basic_app/form_page.html', {'form': form})
