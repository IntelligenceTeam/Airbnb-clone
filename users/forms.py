from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
                # add_error:특정 필드에만 에러메시지 나오게 함.
        except models.User.DoesNotExist:  # 해당 유저가 없을 경우
            self.add_error("email", forms.ValidationError("User does not exist"))
