from django.shortcuts import render
# Dans blog/views.py

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def story(request):
    return render(request, 'histoire.html')

def galerie(request):
    return render(request,'galerie.html')

def calendrier(request):
    return render(request, 'calendrier.html')
