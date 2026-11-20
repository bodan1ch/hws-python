from django.urls import path, re_path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("news", views.news, name="news"),
    path("management", views.management, name="management"),
    path("facts", views.facts, name="facts"),
    path("contacts", views.contacts, name="contacts"),
    path("history/people", views.history_people, name="history_people"),
    path("history/photos", views.history_photos, name="history_photos"),
    path("history", views.history, name="history"),
    re_path(r"^news(?:/.*)?$", views.news),
    re_path(r"^management(?:/.*)?$", views.management),
    re_path(r"^facts(?:/.*)?$", views.facts),
    re_path(r"^contacts(?:/.*)?$", views.contacts),
    re_path(r"^history(?:/.*)?$", views.history),
]
