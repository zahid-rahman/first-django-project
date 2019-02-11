from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

from blogapp.models import Post


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields =['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class UserPostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.Textarea()
    # author = forms.CharField(max_length=200)
    # exclude = ('author')
    # author_id = forms.CharField(max_length=30)
    # author_id = forms.CharField(max_length=30,widget=forms.HiddenInput())

    class Meta:
        model = Post
        fields=['title','content','author']
        # widget= {'author_id': forms.HiddenInput()}