from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        print("clean email")
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(username=email)
            return email
        except models.User.DoesNotExist:  # 해당 유저가 없을 경우
            raise forms.ValidationError("User does not Exist")

    def clean_password(self):
        print("clean password")
        return "lalalalala"
