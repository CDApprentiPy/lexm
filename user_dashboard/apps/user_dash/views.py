# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import Login, Register
from .models import User
from django.shortcuts import render, redirect
import bcrypt

def index(request):
    context = {
        "title": "Home Page",
    }
    return render(request, "user_dash/index.html", context)

def signin(request):
    form = Login()
    context = {
        "title": "Signin Page",
        "form": form,
    }
    return render(request, "user_dash/signin.html", context)

def register(request):
    form = Register()
    context = {
        "title": "Register",
        "form": form,
    }
    return render(request, "user_dash/register.html", context)

def process(request):
    if request.method != "POST":
        return redirect("/")
    post = request.POST
    fname = post.get('first_name')
    lname = post.get('last_name')
    mail = post.get('email')
    if len(User.objects.filter(email=mail)) > 0:
        print "User already registered"
        return redirect('/')
    password = post.get('password')
    confirm = post.get('confirm')
    if password != confirm:
        print "Passwords do not match"
        return redirect('/')
    hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    if len(User.objects.all()) == 0:
        level = 9
    else:
        level = 1
    print fname, lname, mail, password
    print hash
    User.objects.create(first_name=fname, last_name=lname, email=mail, hash=hash, user_level=level)
    return redirect("/")
