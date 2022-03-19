import json
from django.shortcuts import redirect, render, HttpResponse
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers


def searchBook(request):
    if request.method == "POST":
        search_str = json.loads(request.body).get("searchText")
        books = Books.objects.filter(title=search_str)
        print(books)
        data = books.values()
        array =[]
        for x in books.values():
            array.append(x)
        print(array)
        print(data)
        return JsonResponse(list(data), safe=False)


def index(request):
    books = Books.objects.all()
    values = []
    page = request.GET.get('page', 1)

    paginator = Paginator(books, 3)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    for book in books:
        ask = Books.objects.filter(title=book.title).values('id')[0]['id']
        check = Borrowed.objects.filter(book=ask)
        check = len(check)
        if check != 0:
            ask = Books.objects.filter(title=book.title).values('id')[0]['id']
            values.append(ask)

    for val in values:
        books = books.exclude(id=val)

    return render(request, "index.html", {'books': books, 'values': values})


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def view_users(request):
    users = User_of_Library.objects.all()
    return render(request, "view_users.html", {'users': users})


@login_required()
def view_borowed(request):
    borowed = Borrowed.objects.all()
    username = None
    flag = 0
    if request.user.is_superuser:
        flag = 1
    if flag == 0:
        if request.user.is_authenticated:
            username = request.user.username
            us = User.objects.filter(username=username).values('id')[0]['id']
            borowed = Borrowed.objects.filter(user=us)

    return render(request, "view_borowed.html", {'borowed': borowed})


def delete_student(request, myuser):
    username = User.objects.filter(username=myuser).values('id')[0]['id']
    asked = User_of_Library.objects.filter(user=username)
    asked.delete()
    return redirect("/view_users/")


def unrent(request, myuser, mybook):
    username = User.objects.filter(username=myuser).values('id')[0]['id']
    ask = Books.objects.filter(title=mybook).values('id')[0]['id']
    asked = Borrowed.objects.filter(book=ask, user=username)
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


def Register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Hasła się nie są identyczne')
            return render(request, "register.html")
        try:
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user_of_library = User_of_Library.objects.create(user=new_user)
            new_user.save()
            new_user_of_library.save()
            return render(request, "index.html")

        except:
            pass

    return render(request, "register.html")


def change_password(request, myuser):
    username = User.objects.filter(username=myuser).values('id')[0]['id']
    if request.method == "POST":
        new_password = request.POST['new_password']
        try:
            u = User.objects.get(id=username)
            u.set_password(new_password)
            u.save()
            return render(request, "index.html")
        except:
            pass
    return render(request, "change_password.html")
