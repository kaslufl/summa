from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate
from django.db import IntegrityError


def login(request):
    if request.method == "POST":
        un = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(username=un, password=pw)
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard/")
        else:
            messages.error(request, "Ops! Dados inválidos.")
            return render(request, "index_login.html")
    else:
        return render(request, "index_login.html")


def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        pass1 = request.POST['pass']
        pass2 = request.POST['re_pass']

        if(pass1!=pass2 or pass1 == None or pass2 == None):
            messages.error(request, "Credenciais incorretas!")
            return render(request, 'index_signup.html')
        else:
            try:
                user = User.objects.create_user(username=username, first_name=fname, last_name=lname, password=pass1, email=email)
                user.save()
                messages.info(request, "Usuário cadastrado com sucesso!")
                return redirect('/')

            except ValueError:
                messages.error(request, "Invalid Data input!")
                return render(request, 'index_signup.html')

            except IntegrityError:
                messages.error(request, "Usuário já cadastrado.")
                return render(request, 'index_signup.html')

    else:
        return render(request, "index_signup.html")


def logout(request):
    auth.logout(request)
    return redirect("/")
