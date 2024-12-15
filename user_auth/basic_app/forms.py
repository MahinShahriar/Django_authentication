from django import forms
from django.contrib.auth.models import User
from .models import ProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Enter your password please: ")

    class Meta:
        model = User
        fields = ('username','email','password')

class ProfileInfoForm(forms.ModelForm):

    class Meta:
        model = ProfileInfo
        fields = ('profile_pic','portfolio_site')
