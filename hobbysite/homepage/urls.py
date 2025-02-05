from django.urls import path

from .views import homepage_test, homepage, dashboard

app_name = "homepage"

urlpatterns = [
    path("home_test/", homepage_test, name="home_test"),
    path("home/", homepage, name="home"),
    path("home/dashboard", dashboard, name="dashboard")
]
