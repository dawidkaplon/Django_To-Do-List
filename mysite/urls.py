from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.index, name="index"),
    path("list/create/", views.create, name="create"),
    path("list/<int:id>/", views.view, name="view"),
    path("list/view/", views.choose_list, name="choose_list")

]
