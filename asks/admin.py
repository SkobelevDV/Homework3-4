import django.contrib.admin
from django.contrib import admin

# Register your models here.
from .models import AskInstance, Ask, Tags, Answer
admin.site.register(AskInstance)
admin.site.register(Ask)
admin.site.register(Answer)
admin.site.register(Tags)