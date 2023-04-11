from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('created_time', 'last_update_time')
        fields = ('id', 'avatar', 'contact_number', 'password', 'salt', 'nickname', 'created_time', 'created_user', 'last_update_time', 'last_update_user', 'email')

class UserRegisterForm(UserCreationForm):
    contact_number = forms.CharField(max_length=15)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['nickname', 'contact_number', 'email', 'password1', 'password2']
