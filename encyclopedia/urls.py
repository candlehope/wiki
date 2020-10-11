from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:page>", views.entry, name="entry"),
    path("wiki", views.search, name="search"),
    path("results", views.search, name="search")
]
