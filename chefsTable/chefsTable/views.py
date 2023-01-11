from django.http import HttpResponse, HttpResponseNotFound


def handler404(req, exception):
    return HttpResponseNotFound("404 : page not found!")

def handler500(req):
    return HttpResponse("500 : internal server error!")

