from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpRequest


def home(req):
    return HttpResponse("Hello World!")


def menu_by_id(req:HttpRequest, menu_id):
    print(req.body)
    return HttpResponse("ID IS " + str(menu_id))
