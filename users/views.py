from django.views import View
from django.shortcuts import render
from . import forms


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm(initial={"email": "capunet@naver.com"})
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)  # form을 정리해준 데이터
        return render(request, "users/login.html", {"form": form})
