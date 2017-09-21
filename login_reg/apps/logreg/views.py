# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import Register, Login
from .models import User
from django.shortcuts import render, redirect
import bcrypt

def index(request):
    r_form = Register()
    l_form = Login()
    context = {
        "r_form": r_form,
        "l_form": l_form,
    }
    return render(request, "logreg/index.html", context)

def register(request):
    if request.method != "POST":
        return redirect("/")
    post = request.POST
    fname = post.get('first_name')
    lname = post.get('last_name')
    mail = post.get('email')
    password = post.get('password')
    confirm = post.get('confirm')
    if password != confirm:
        print "Passwords do not match"
        return redirect('/')
    hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    print fname, lname, mail, password
    print hash
    User.objects.create(first_name=fname, last_name=lname, email=mail, hash=hash)
    return redirect("/success")

def login(request):
    if request.method != "POST":
        return redirect("/")
    post = request.POST
    login = post.get('email')
    passwd = post.get('password')
    users = User.objects.filter(email=login)
    if len(users) > 1:
        print "double login"
        return redirect('/')
    elif len(users) < 1:
        print "no match"
        return redirect('/')
    user = User.objects.first()
    if bcrypt.checkpw(passwd.encode('utf-8'), user.hash.encode('utf-8')):
        return redirect("/success")
    else:
        return redirect('/')

def success(request):
    return render(request, "logreg/success.html")
