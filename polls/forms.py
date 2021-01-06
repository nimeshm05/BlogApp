from django.forms import ModelForm
from django import forms
from .models import Poll
from django.core.exceptions import ValidationError

class CreatePollForm(ModelForm):

    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three', 'category', 'category_confirm', 'username']
