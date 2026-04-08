from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'proj1/index.html')

def generic(request):
    return render(request, 'proj1/generic.html')

def elements(request):
    return render(request, 'proj1/elements.html')