from django.shortcuts import render, redirect


def dashboard_page(request):
    if not request.user.is_authenticated:
        return redirect('login:login_page')
    return render(request,"members/dashboard.html")

