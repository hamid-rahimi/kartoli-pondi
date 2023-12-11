from django.urls import path
from login.views import login_page


app_name = "login"
urlpatterns = [
    path('', login_page, name="login_page")
]