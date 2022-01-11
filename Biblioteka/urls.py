from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("view_users/", views.view_users, name="view_users"),
    path("rent_book/<myuser>/", views.rent_book, name="rent_book"),
    path("view_borowed/", views.view_borowed, name="view_borowed"),
    path("change_password/<myuser>/", views.change_password, name="change_password"),
    path("register/", views.Register, name="register"),
    path("Login/", views.Login, name="Login"),
    path("Logout/", views.Logout, name="Logout"),

    path("delete_student/<myuser>/", views.delete_student, name="delete_student"),
    path("unrent/<myuser> <mybook>/", views.unrent, name="unrent"),
]
