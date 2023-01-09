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


def say_hello(req):
    return HttpResponse("hello")


def index(request):
    path = request.path
    method = request.method
    content = ''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
'''.format(path, method)
    return HttpResponse(content)
