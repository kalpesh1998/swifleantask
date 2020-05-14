from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# login page content
class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

# Signup page content
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')
    city = forms.CharField(max_length=20)
    board = forms.CharField(max_length=20)
    grade=forms.IntegerField(max_value=12,min_value=1,help_text='Enter class 1-12')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2','city','board','grade')