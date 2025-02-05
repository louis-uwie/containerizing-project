from django.urls import path

from .views import UserCreateView, ProfileUpdateView

app_name = "user_management"

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="register"),
    path("profile/", ProfileUpdateView.as_view(), name="profile_update"),
]