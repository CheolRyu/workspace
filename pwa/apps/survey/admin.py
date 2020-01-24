from django.contrib import admin
from .models import *
# Register your models here.

class QuestionInline(admin.TabularInline):
	model = Question
admin.site.register(Question)


class OptionInline(admin.TabularInline):
	model = Option
admin.site.register(Option)

class HighInsulinInline(admin.TabularInline):
	model = HighInsulin
admin.site.register(HighInsulin)

class LowThyroidInline(admin.TabularInline):
	model = LowThyroid
admin.site.register(LowThyroid)

class HighAndrogenInline(admin.TabularInline):
	model = HighAndrogen
admin.site.register(HighAndrogen)

class LowAndrogenInline(admin.TabularInline):
	model = LowAndrogen
admin.site.register(LowAndrogen)

class HighCortisolInline(admin.TabularInline):
	model = HighCortisol
admin.site.register(HighCortisol)

class LowCortisolInline(admin.TabularInline):
	model = LowCortisol
admin.site.register(LowCortisol)

class EstrogenPregnancyInline(admin.TabularInline):
	model = EstrogenPregnancy
admin.site.register(EstrogenPregnancy)

class EstrogenDominanceInline(admin.TabularInline):
	model = EstrogenDominance
admin.site.register(EstrogenDominance)
