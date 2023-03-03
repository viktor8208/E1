from django.shortcuts import render


def index(request):
    return render(request, 'main.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')

