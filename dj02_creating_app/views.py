from django.shortcuts import render

def index(request):
    data = {
        'caption': "DogDjango",
    }
    return render(request, 'dj02_creating_app/index.html', data)

def new(request):
    return render(request, 'dj02_creating_app/new.html')

def breeds(request):
    return render(request, 'dj02_creating_app/breeds.html')

def dachshund(request):
    return render(request, 'dj02_creating_app/dachshund.html')

def tibetan_mastiff(request):
    return render(request, 'dj02_creating_app/tibetan_mastiff.html')

def chow_chow(request):
    return render(request, 'dj02_creating_app/chow_chow.html')

def sharpei(request):
    return render(request, 'dj02_creating_app/sharpei.html')
