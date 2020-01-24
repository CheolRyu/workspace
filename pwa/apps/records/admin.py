from django.contrib import admin
from . import models 
# Register your models here.
# 
class RecordListInline(admin.TabularInline):
	model = models.Record
admin.site.register(models.Record)



