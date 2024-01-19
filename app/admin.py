import django.contrib.admin

from django.contrib import admin
from django.forms import CheckboxSelectMultiple
# Register your models here.

from .models import *

class ForModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

admin.site.register(Question,ForModelAdmin)
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(LikeAnswer)
admin.site.register(LikeQuestion)