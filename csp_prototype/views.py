
from django.shortcuts import render

def index(request):
    logo = "/assets/cspc.png"
    return render(request, 'home.html', {"logo": logo})

