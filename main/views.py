from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubscriberForm


def index(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()
    return render(request, 'index.html', locals())


def resume(request):
    # return HttpResponse("<h1>PRICING</h1>")
    return render(request, 'resume.html')


def contact(request):
    # return HttpResponse("<h1>CONTACT</h1>")
    return render(request, 'contact.html')
