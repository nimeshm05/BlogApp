from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    location = forms.CharField()

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
        return self.cleaned_data

    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'location']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    location = forms.CharField()

    class Meta:
        model = Profile
        fields = ['image', 'location']
