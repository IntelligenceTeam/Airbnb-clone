from django import forms
from django.contrib.auth.forms import UserCreationForm
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


class SignUpForm(UserCreationForm):
    class Meta:  # ModelForm을 쓰면 이렇게 Meta클래스로 작성.
        model = models.User
        fields = ("first_name", "last_name", "email")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data.get("email")
        user.set_password(self.cleaned_data.get("password1"))  # 비밀번호를 암호화 해주는 메소드
        if commit:
            user.save()
        return user
