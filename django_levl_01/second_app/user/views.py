from django.shortcuts import render
from user.forms import NewUserForm


def index(request):
	return render(request, 'user/index.html')

def users(request):

	form = NewUserForm()

	if request.method == "POST":
		form = NewUserForm(request.POST)


		if form.is_valid():
			form.save(commit=True)
			return index(request)

		else:
			print('Error, Form invalid')
	return render(request, 'user/users.html', {'form': form})