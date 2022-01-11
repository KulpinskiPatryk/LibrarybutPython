from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone
from datetime import datetime,timedelta


class Author(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name) + " " + str(self.surname)



class Genre(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return str(self.name)


class Books(models.Model):
    title = models.CharField(max_length=200)
    pages = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['author']

    def __str__(self):
        return str(self.title)


def date_return():
    return datetime.today() + timedelta(days=14)


class Borrowed(models.Model):
    date_of_borrow = models.DateField(auto_now=True)
    date_to_return = models.DateField(default=date_return)
    book = models.ForeignKey(Books, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.book) + " " + str(self.user)


def date_doom():
    return datetime.today() + timedelta(days=90)


class User_of_Library(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_of_start = models.DateField(auto_now=True)
    date_of_end = models.DateField(default=date_doom)


    def __str__(self):
        return str(self.user)

# Create your models here.
