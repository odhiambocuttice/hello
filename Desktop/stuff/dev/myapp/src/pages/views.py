from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_views(request, *args, **kwargs):
    # return HttpResponse("<h1>hello ME</h1>")
    return render(request, "home.html", {})
