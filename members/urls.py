from django.urls import path
from members.views import dashboard_page


app_name = 'members'
urlpatterns = [
    path('dashboard/', dashboard_page, name="dashboard_page")
]