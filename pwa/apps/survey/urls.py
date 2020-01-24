from django.urls import path
from . import views 


app_name = 'survey'

urlpatterns = [
	path('', views.IndexView.as_view(), name='home')
]