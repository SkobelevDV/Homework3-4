from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(min_length = 4, widget = forms.PasswordInput) #forms.TextArea)

    #устанавливаем библиотеку:  pip install django-bootstrap5

    def clean_password (self):
        data = self.cleaned_data ['password']
        if data == 'wrongpass':
            raise ValidationError ('Wrong password')
        return data

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)# если хотим изменить существующее поле
    password_check = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']
        #fields = "__all__"

    def clean(self):
        password = self.cleaned_data['password']
        password_check = self.cleaned_data['password_check']
        if password != password_check:
            raise ValidationError('Password do not match')

    def save(self, **kwargs):
        self.cleaned_data.pop('password_check')
        return User.objects.create_user(self.cleaned_data)