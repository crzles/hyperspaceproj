from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'stellarproj1/index.html')

def generic(request):
    return render(request, 'stellarproj1/generic.html')

def elements(request):
    return render(request, 'stellarproj1/elements.html')