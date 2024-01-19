import django.contrib.admin
from django.contrib import admin
from .models import Author,Book, BookInstance, Genre

from django.db import models
from django.forms import CheckboxSelectMultiple

class ForModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


# Register your models here.

admin.site.register(Author)
admin.site.register(Book, ForModelAdmin)
admin.site.register(BookInstance)
admin.site.register(Genre)