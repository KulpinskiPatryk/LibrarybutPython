from django.shortcuts import redirect, render,HttpResponse
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.http import JsonResponse


def index(request):
    books = Books.objects.all()
    values = []
    for book in books:
        ask = Books.objects.filter(title=book.title).values('id')[0]['id']
        check = Borrowed.objects.filter(book=ask)
        check = len(check)
        values.append(check)

    print(values)
    print(len(books))
    if request.method == "POST":
        ask = request.POST['ask']
        print(ask)
        if ask is not None:
            books = Books.objects.filter(title=str(ask))
    return render(request, "index.html", {'books':books, 'values':values})


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def view_users(request):
    users = User_of_Library.objects.all()
    return render(request, "view_users.html", {'users':users})


@login_required()
@user_passes_test(lambda u: u.is_superuser)
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


def rent_book(request, myuser):
    asked = Books.objects.get(title=myuser)
    ask = Books.objects.filter(title=myuser).values('id')[0]['id']
    check = Borrowed.objects.filter(book=ask)
    if len(check) == 0:
        print(len(check))
        students = request.user
        borrow = Borrowed.objects.create(book=asked, user=students)
        borrow.save()
        return redirect("/")
    else:
        return redirect("/")


def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            redirect("/index/")


    return render(request, "Login.html")


def Logout(request):
    logout(request)
    return redirect("/")



