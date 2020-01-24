from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Thyroid)
admin.site.register(Insulin)
admin.site.register(Low_Cortisal)
admin.site.register(High_Cortisal)
admin.site.register(Low_Androgen)
admin.site.register(High_Androgen)
admin.site.register(Estrogen_Progenence)
admin.site.register(Estrogen_Dominence)