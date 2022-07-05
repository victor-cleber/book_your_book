from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import User


def create(request):
    return HttpResponse('ola')


def home(request):
    if request.session.get('user'):
        username = User.objects.get(id = request.session['user']).name
        # object.filter retorna uma lista de usuario username = User.object.filter(id=request.session['user'](0).name)
        # object.get apenas um usuario q atenda a condicao
        return HttpResponse(f'ola {username}')
    else:
        return redirect('/auth/login/?status=2')
