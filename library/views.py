from django.http import HttpResponse
from django.shortcuts import render

from library.models import Author

# Create your views here.

def index(request):
    #authors = Author.objects.all()
    authors = Author.objects.alive()
    return HttpResponse(authors)