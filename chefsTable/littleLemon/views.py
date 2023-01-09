from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest


def home(req):
    return HttpResponse("Hello World!")


def about(req):
    return HttpResponse("<h1>About</h1>")


def menu_by_id(req: HttpRequest, menu_id):
    print(req.body)
    return HttpResponse("ID IS " + str(menu_id))


def new_page(req):
    return HttpResponse("welcome to little lemon restaurant. week 3 of django web frameword coursera course!")
