from django.http import HttpResponse,HttpResponseNotFound


def handler404(req,exception):
    return HttpResponseNotFound("404 : page not found!")
