from django import forms
from .models import Comment, User
from django.contrib.auth.forms import UserCreationForm



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {field: "" for field in fields}

    