from django.urls import path

from . import views


urlpatterns = [
    path("", views.contact_list, name="contact_list"),
    path("contacts/add/", views.contact_add, name="contact_add"),
    path("contacts/<int:contact_id>/edit/", views.contact_edit, name="contact_edit"),
    path("contacts/<int:contact_id>/delete/", views.contact_delete, name="contact_delete"),
]
