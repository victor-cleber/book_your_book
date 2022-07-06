from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import User
from book.models import Books

def create(request):
    return HttpResponse('ola')


def home(request):
    if request.session.get('user'):
        user = User.objects.get(id=request.session['user'])
        # object.filter retorna uma lista de usuario username = User.object.filter(id=request.session['user'](0).name)
        # object.get apenas um usuario q atenda a condicao
        #return HttpResponse(f'ola {username}')

        #books = Books.objects.all()
        books = Books.objects.filter(user=user)
        return render(request, 'home.html', {'books': books})
    else:
        return redirect('/auth/login/?status=2')


def ver_livro(request, id):
    #return HttpResponse(id)
    #book = Books.objects.filter() =traz varios livros ou get traz este livro
    book = Books.objects.get(id=id)
    print(book)
    return render(request, 'ver_livro.html', {'book': book})
