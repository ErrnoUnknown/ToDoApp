from django import forms
from todoapp.models import User


class RegisterForm(forms.Form):
    nickname = forms.CharField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        return nickname

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        return password

    def clean_password2(self):
        password = self.cleaned_data.get('password2')
        return password


class LoginForm(forms.Form):
    nickname = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        return nickname

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return password


class ListForm(forms.Form):
    subject = forms.CharField(max_length=100)
    contents = forms.CharField(widget=forms.PasswordInput)

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        return subject

    def clean_contents(self):
        contents = self.cleaned_data.get('contents')
        return contents