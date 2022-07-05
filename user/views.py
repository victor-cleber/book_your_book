from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.shortcuts import redirect
from hashlib import sha256


def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})
    #return HttpResponse('login')


def create(request):
    #return HttpResponse('create')
    #return render(request, 'create.html')
    status = request.GET.get('status')
    return render(request, 'create.html', {'status': status})


def valida_cadastro(request):
    #return render(request, 'create.html')
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')

    #user = User(name=name, email=email, password=password)
    #user.save()
    #return HttpResponse(f"{name} {email} {password}")

    if len(name.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/create/?status=1')

    if len(password.strip()) < 8:
        return redirect('/auth/create/?status=2')

    email_already_exists = User.objects.filter(email=email)
    if len(email_already_exists) > 0:
        return redirect('/auth/create/?status=3')

    try:
        password = sha256(password.encode()).hexdigest()

        user = User(name=name,
                    email=email,
                    password=password)
        user.save()

        return redirect('/auth/create/?status=0')
    except Exception as e:
        print(e)
        return redirect('/auth/create/?status=4')


def valida_login(request):
    #return render(request, 'create.html')
    email = request.POST.get('email')
    password = request.POST.get('password')

    password = sha256(password.encode()).hexdigest()

    #local storage, session, cookie - armazenar o token
    #user = User(name=name, email=email, password=password)
    #user.save()
    #return HttpResponse(f"{name} {email} {password}")

    if len(email.strip()) == 0:
        return redirect('/auth/login/?status=1')

    if len(password.strip()) < 8:
        return redirect('/auth/login/?status=2')

    try:
        user = User.objects.filter(email=email).filter(password=password)
        # return redirect('/auth/login/?status=4')
        # return render(request, 'login.html', {'status': user})
        if len(user) == 0:
            return redirect('/auth/login/?status=3')
        elif len(user) == 1:
            # return redirect('/auth/login/?status=0')
            # request.session['user'] = user[0].id
            return redirect('/book/home')
        elif len(user > 1):
            raise Exception('mais de um usuario no bd')
    except Exception as e:
        print(e)
        return redirect('/auth/login/?status=4')
