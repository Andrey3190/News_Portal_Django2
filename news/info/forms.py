from django import forms
from .models import News
from .models import Category
from django.contrib.auth.models import User



class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['name', 'category', 'description']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['category']


