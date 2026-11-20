from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("numbers/", views.numbers_view, name="numbers"),
    path("registration/", views.registration_view, name="registration"),
    path("programmer-day/", views.programmer_day_view, name="programmer_day"),
]
