# flake8: noqa
from django.contrib.auth.models import User
from django.contrib.auth.forms import (UserCreationForm,
                                       UserChangeForm,
                                       SetPasswordForm)
from .models import Text
from django import forms


class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ('user', 'text', 'predictions', 'hate', 'not_hate',)


class ChangePasswordForm(SetPasswordForm):
    """Change the user password"""
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm New Password'


class UpdateUserForm(UserChangeForm):
    password = None  # Exclude the password field
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), required=False)
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''


# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
#     first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
#     last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
#     username = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'user name'}))
#     password1 = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'passwrd'}))
#     password2 = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'reenter your password'}))

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address'})
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'})
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'})
    )
    username = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'})
    )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'})
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Re-enter Password'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
