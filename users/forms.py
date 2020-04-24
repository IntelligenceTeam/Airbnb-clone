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


class SignUpForm(forms.Form):

    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_cf = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    # label없이 변수명을 바꿔서 해도 됨. 페이지에 변수명으로 나옴.

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("User already exists with that email")
        except models.User.DoesNotExist:
            return email

    def clean_password_cf(
        self,
    ):  # clean_password라고 하면 확인용 비밀번호랑 비교가 되질 않는다. 그래서 확인용 변수이름을 붙여준다.
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password_cf")  # 확인용 비밀번호 변수를 get 인자값으로 넣는다.
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password
