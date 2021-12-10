from django.shortcuts import redirect, render,HttpResponse
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


def index(request):
    books = Books.objects.all()
    if request.method == "POST":
        ask = request.POST['ask']
        print(ask)
        if ask is not None:
            books = Books.objects.filter(title=str(ask))
    return render(request, "index.html", {'books':books})


def view_users(request):
    users = User_of_Library.objects.all()
    return render(request, "view_users.html", {'users':users})


def view_borowed(request):
    borowed = Borrowed.objects.all()
    if request.method == "POST":
        ask = request.POST['ask']
        asked = Books.objects.filter(title=ask).values('id')[0]['id']
        print(asked)
        print(ask)
        if asked > 0:
            borowed = Borrowed.objects.filter(book=asked)
    return render(request, "view_borowed.html", {'borowed':borowed})


def delete_student(request,myuser):
    students = User.objects.filter(username=myuser).values('id')[0]['id']
    asked = User_of_Library.objects.filter(user=students)
    asked.delete()
    return redirect("/view_users/")


def unrent(request,myuser):
    students = User.objects.filter(username=myuser).values('id')[0]['id']
    asked = Borrowed.objects.filter(user=students)
    asked.delete()
    return redirect("/view_borowed/")
