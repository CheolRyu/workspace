from django.urls import path
from . import views


app_name='shops'
urlpatterns = [
	path('', views.index, name='home')
]