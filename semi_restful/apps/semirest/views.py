# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import UserForm
from .models import User
from django.shortcuts import render, redirect

def index(request):
    return render(request, "semirest/index.html")

def new(request):
    form = UserForm()
    return render(request, "semirest/new.html", {"form":form})

def edit(request, id):
    user = User.objects.get(id=id)
    init = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
    }
    form = UserForm(initial=init)
    context = {
        "id": id,
        "form": form,
    }
    return render(request, "semirest/edit.html", context)

def show(request, id):
    if request.method == "POST":
        return update(request, id)
    user = User.objects.get(id=id)
    context = {
        "id": id,
        "fname": user.first_name,
        "lname": user.last_name,
        "email": user.email,
        "created_at": user.created_at,
    }
    return render(request, "semirest/show.html", context)

def create(request):
    post = request.POST
    fname = post.get('first_name')
    lname = post.get('last_name')
    mail = post.get('email')
    new_user = User.objects.create(first_name=fname, last_name=lname, email=mail)
    new_user.save()
    return redirect("/users/" + str(new_user.id))

def destroy(request):
    return redirect("/users/")

def update(request, id):
    post = request.POST
    fname = post.get('first_name')
    lname = post.get('last_name')
    mail = post.get('email')
    print "updating..."
    print fname, lname, mail
    update_user = User.objects.get(id=id)
    update_user.first_name = fname
    update_user.last_name = lname
    update_user.email = mail
    update_user.save()
    return redirect("/users/" + str(id))
