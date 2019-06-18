from django import forms
from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth import get_user_model
User = get_user_model()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )