from django import forms
from AppRating.models import User

class UserForm(forms.ModelForm):

    username_error_messages = {'required':'The username is required!'}
    password_error_messages = {'required':'The password is required!'}

    username = forms.CharField(error_messages=username_error_messages)
    username.help_text = ''

    password = forms.CharField(widget=forms.PasswordInput(),error_messages=password_error_messages)

    class Meta:
        model = User
        fields = ('username', 'password')