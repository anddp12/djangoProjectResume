from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("<h1>HOME</h1>")
    return render(request, 'index.html')


def resume(request):
    # return HttpResponse("<h1>PRICING</h1>")
    return render(request, 'resume.html')


def contact(request):
    # return HttpResponse("<h1>CONTACT</h1>")
    return render(request, 'contact.html')
