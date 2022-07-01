from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'login.html')


def create(request):
    return render(request, 'create.html')


def validate_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    return HttpResponse(f"{email}{password}")
