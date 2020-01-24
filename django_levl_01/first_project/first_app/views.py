from django.shortcuts import render
from first_app.models import AccessRecord, Topic, Webpage
# Create your views here.
def index(request):
	webpg_lists = AccessRecord.objects.order_by('date')
	date_dict = {'access_records': webpg_lists}
	return render(request, 'first_app/index.html', context=date_dict)