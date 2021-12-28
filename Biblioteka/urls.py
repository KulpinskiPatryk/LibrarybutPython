from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("view_users/", views.view_users, name="view_users"),
    path("rent_book/<myuser>/", views.rent_book, name="rent_book"),
    path("view_borowed/", views.view_borowed, name="view_borowed"),
    #path("view_students/", views.view_students, name="view_students"),
    #path("issue_book/", views.issue_book, name="issue_book"),
    #path("view_issued_book/", views.view_issued_book, name="view_issued_book"),
    #path("student_issued_books/", views.student_issued_books, name="student_issued_books"),
    #path("profile/", views.profile, name="profile"),
    #path("edit_profile/", views.edit_profile, name="edit_profile"),

    #path("student_registration/", views.student_registration, name="student_registration"),
    #path("change_password/", views.change_password, name="change_password"),
    #path("student_login/", views.student_login, name="student_login"),
    path("Login/", views.Login, name="Login"),
    path("Logout/", views.Logout, name="Logout"),

    #path("delete_book/<int:myid>/", views.delete_book, name="delete_book"),
    path("delete_student/<myuser>/", views.delete_student, name="delete_student"),
    path("unrent/<myuser>/", views.unrent, name="unrent"),
]
