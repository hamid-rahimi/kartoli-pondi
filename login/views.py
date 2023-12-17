from django.shortcuts import render, redirect
from django.http import HttpResponse
from login.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.exceptions import ValidationError


def login_page(request):
    if request.method == "POST":
        login_form = LoginForm(data=request.POST)
        print(request.method)
        print(login_form.data)
        print(login_form.is_valid())
        if login_form.is_valid():
            user = login_form.cleaned_data
            print(user)
            username = user.get('username')
            password = user.get('password')
            print(username, password)
            u = authenticate(request, username=username, password=password)
            print('auth : ', u)
            if u is not None:
                # login
                login(request, u)
                return redirect('members:dashboard_page')
            else:
                # not login
                login_form.add_error('password',ValidationError("نام کاربری یا رمز ورود اشتباه"))
                # return redirect(f"{settings.LOGIN_URL}?next={request.path}")
                # raise ValidationError("نام کاربری یا رمز ورود اشتباه : %(value)s",code='Empty Field',
                #                       params={'value': "تست خطا یابی..."})
                print(login_form.errors.as_data())
    else:
        login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    return render(request, 'login/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('login:login_page')