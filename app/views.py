from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

from app.forms import LoginForm, RegisterForm

# Create your views here.

QUESTIONS = [
        {
            'id': i,
            'title': f'Questions {i}',
            'content': f'Long Lorem Ipsum {i}'
        } for i in range (100)
    ]

def paginate(objects, page, per_page=15):
    otn=int(len(objects))//per_page
    if int(page) > otn:
        page = str(otn)
    if int(page) <1 :
        page=str(1)
    #добавить проверку на большее количество страниц
    paginator = Paginator(objects, per_page)
    return paginator.page(page)

@login_required#(login_url = '/login', redirect_field_name = 'continue')
def index(request):
    page=request.GET.get('page',1) #http://127.0.0.1:8000/?page=2
    return render(request,'index.html', {'questions' : paginate(QUESTIONS,page) })
#HttpResponse("Hello, world!"))

def question(request, question_id):
    item = QUESTIONS [question_id]
    return render(request, 'question.html', {'question' : item})

def hot(request):
    page=request.GET.get('page',1) #http://127.0.0.1:8000/?page=2
    return render(request, 'hot.html', {'questions' : paginate(QUESTIONS,page) })

def tag(request):
    return render(request, 'tag.html')

@csrf_protect
def log_in(request):
    print(request.GET)
    print(request.POST)

    if request.method == "GET":
        login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        # username = request.POST["username"]
        # password = request.POST["password"]

        if login_form.is_valid():

            user = authenticate ( request, **login_form.cleaned_data ) # ** передача поштучно ранее было username = username, password = password
            print(user)
            if user is not None:
                login(request, user)
                print ('Seccessfully logged in')
                return redirect( request.GET.get('continue', '/')) #было ранее reverse('index')
            else:
                login_form.add_error(None, "Wrong password or user does not exist.")


    return render (request, 'login.html', context = {"form": login_form})

@csrf_protect
def signup(request):
    if request.method == "GET":
        user_form = RegisterForm()
    if request.method == "POST":
        user_form = RegisterForm(request.POST)


        if user_form.is_valid():

            user = user_form.save() # ** передача поштучно ранее было username = username, password = password

            if user:
                return redirect(reverse('index'))
            else:
                user_form.add_error(field=None,error="User saving error!")
    return render(request, 'signup.html', context={'form': user_form})


def ask(request):
    return render(request, 'ask.html')

def settings(request):
    return render(request, 'settings.html')

def logout(request):
    auth.logout(request)
    return redirect(reverse('login'))