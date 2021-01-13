from django.shortcuts import render

# Create your views here.

def Home (request):
    return render(request, 'home.html')

def Title(request):
    return render(request,'title.html')