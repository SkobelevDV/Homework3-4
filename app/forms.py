from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



from .models import *

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'tags': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title



class SignUpForm(forms.Form):
    login = forms.CharField(label='Login', max_length=30, widget=forms.TextInput(attrs={'class': 'form-input'}))
    nickname = forms.CharField(label='nickname', max_length=30, widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', min_length=4, widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Repeat password', min_length=4, widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    photo = forms.ImageField(required=False, label='Avatar',
                             widget=forms.ClearableFileInput(attrs={'class': 'form-input'}))

    def clean(self):
        login = self.cleaned_data.get('login')
        password = self.cleaned_data.get('password1')

        if login and password:
            # можно выполнить здесь дополнительные проверки логина, если это необходимо
            pass

        return super().clean()
    def clean_password(self):
        data = self.cleaned_data['password']
        if data == 'wrongpass':
            raise ValidationError('Wrong password')
        return data

class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(min_length=4, widget = forms.PasswordInput)
    def clean_password(self):
        data = self.cleaned_data['password']
        if data == 'wrongpass':
            raise ValidationError('Wrong password')
        return data

class QuestionForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(min_length=4, widget = forms.Textarea)
    def clean_password(self):
        data = self.cleaned_data['password']
        if data == 'wrongpass':
            raise ValidationError('Wrong password')
        return




