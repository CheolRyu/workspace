from django.conf.urls import url
from user import views


urlpatterns = [
	url(r'^$', views.users, name='users'), 
]