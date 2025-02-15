from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm (UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User # The model our form interacts with, creatinf our form off of it
        fields = ['username', 'email', 'password1', 'password2'] # the fields in our form and the order
