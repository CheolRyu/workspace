from django.urls import path
from . import views


app_name='records'
urlpatterns = [
	path('', views.RecordList.as_view(), name='all'), 
	path('new/', views.CreateRecord.as_view(), name='create'),
	path("by/<username>/<int:pk>/",views.RecordDetail.as_view(),name="single"),
	path("delete/<int:pk>/",views.DeleteRecord.as_view(),name="delete"),
]