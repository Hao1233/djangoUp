from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm

from .models import Post, Comment


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['images', 'title', 'body', 'categories', 'public', 'private']
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
class ChangePassword(PasswordChangeForm):
    class Meta:
        model = User
        fields =  ['old_password', 'new_password1', 'new_password2']