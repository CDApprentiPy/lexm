# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import Login, Register, NewUser, EditUser, ChangePass, EditUserAdmin, EditDescription
from .models import User
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
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

def new_user(request):
    if 'id' in request.session:
        if User.objects.get(id=request.session['id']).user_level == 9:
            form = NewUser()
            context = {
            "title": "New User",
            "form": form,
            }
            return render(request, "user_dash/newuser.html", context)
        else:
            return redirect("/")
    else:
        return redirect("/")

def process(request):
    if request.method == "POST":
        post = request.POST
        form = Register(post)
        if form.is_valid():
            fname = post.get('first_name')
            lname = post.get('last_name')
            mail = post.get('email')
            if len(User.objects.filter(email=mail)) > 0:
                print "User already registered"
                return redirect('/signin')
            password = post.get('password')
            confirm = post.get('confirm')
            if password != confirm:
                print "Passwords do not match"
                return redirect('/register')
            hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            if len(User.objects.all()) == 0:
                level = 9
            else:
                level = 1
            print fname, lname, mail, password
            print hash
            user = User.objects.create(first_name=fname, last_name=lname, email=mail, hash=hash, user_level=level)
            request.session['id'] = user.id
            return redirect("/dashboard")
        else:
            context = {
                "title": "Register",
                "form": form,
            }
            return render(request, "user_dash/register.html", context)
    else:
        return redirect("/")

def login(request):
    if request.method == "POST":
        post = request.POST
        form = Login(request.POST)
        if form.is_valid():
            login = post.get('email')
            passwd = post.get('password')
            users = User.objects.filter(email=login)
            if len(users) > 1:
                print "double login"
                return redirect('/')
            elif len(users) < 1:
                print "no match"
                return redirect('/')
            user = users.first()
            if bcrypt.checkpw(passwd.encode('utf-8'), user.hash.encode('utf-8')):
                print "logged in as", user.id
                request.session['id'] = user.id
                return redirect("/dashboard")
            else:
                return redirect('/signin')
        else:
            context = {
                "title": "Signin Page",
                "form": form,
            }
            return render(request, "user_dash/signin.html", context)
    else:
        return redirect('/')

def dashboard(request):
    users = User.objects.all()
    context = {
        "users": users,
        "admin": False,
    }
    return render(request, "user_dash/dashboard.html", context)

def dash_admin(request):
    print request.session['id']
    if 'id' in request.session:
        if User.objects.get(id=request.session['id']).user_level == 9:
            print "ID is", request.session['id']
            users = User.objects.all()
            context = {
                "users": users,
                "admin": True,
            }
            return render(request, "user_dash/dashboard.html", context)
    return redirect('/dashboard')

def user_edit(request):
    if 'id' in request.session:
        user = User.objects.get(id=request.session['id'])
        mail = user.email
        fname = user.first_name
        lname = user.last_name
        desc = user.description
        form1 = EditUser(mail=mail, fname=fname, lname=lname)
        form2 = ChangePass()
        form3 = EditDescription(desc=desc)
        context = {
            "user": user,
            "form1": form1,
            "form2": form2,
            "form3": form3,
        }
        return render(request, "user_dash/edituser.html", context)
    return redirect('/')

def user_edit_admin(request, id):
    if 'id' in request.session:
        if User.objects.get(id=request.session['id']).user_level == 9:
            user = User.objects.get(id=id)
            mail = user.email
            fname = user.first_name
            lname = user.last_name
            level = user.user_level
            form1 = EditUserAdmin(mail=mail, fname=fname, lname=lname, level=level)
            form2 = ChangePass()
            context = {
                "form1": form1,
                "form2": form2,
                "user_id": id,
            }
            request.session['edit_id'] = id
            return render(request, "user_dash/edituser_admin.html", context)
    return redirect('/')

def update(request):
    if request.method != "POST":
        post = request.POST
        form = EditUser(post)
        if form.is_valid():
            mail = post.get('email')
            fname = post.get('first_name')
            lname = post.get('last_name')
            user = User.objects.get(id=request.session['id'])
            user.email = mail
            user.first_name = fname
            user.last_name = lname
            user.save()
            return redirect('/dashboard')
        else:
            redirect('/user_edit')
    else:
        return redirect("/")

def update_admin(request):
    if request.method != "POST":
        post = request.POST
        form = EditUserAdmin(post)
        if form.is_valid():
            mail = post.get('email')
            fname = post.get('first_name')
            lname = post.get('last_name')
            level = post.get('user_level')
            user = User.objects.get(id=request.session['edit_id'])
            user.email = mail
            user.first_name = fname
            user.last_name = lname
            user.user_level = level
            user.save()
            return redirect('/dashboard')
        else:
            return redirect('/user_edit_admin')
    else:
        return redirect("/")

def change_pass(request):
    if request.method != "POST":
        post = request.POST
        form = ChangePass(post)
        if form.is_valid():
            password = post.get('password')
            confirm = post.get('confirm')
            if password != confirm:
                print "Passwords do not match"
                return redirect('/register')
            if not 'id' in request.session:
                print "ID missing error"
                return redirect('/signin')
            user = User.objects.get(id=request.session['id'])
            hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user.hash = hash
            user.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect("/")

def edit_desc(request):
    if request.method != "POST":
        if not 'id' in request.session:
            print "ID missing error"
            return redirect('/signin')
        post = request.POST
        form = EditDescription(post)
        if form.is_valid():
            desc = post.get('description')
            user = User.objects.get(id=request.session['id'])
            user.description = desc
            user.save()
            return redirect('/dashboard')
        else:
            return redirect('/')
    else:
        return redirect("/")

def user_delete(request):
    pass

def show_user(request, id):
    try:
        user = User.objects.get(id=id)
    except ObjectDoesNotExist:
        not_there = True
        user = None
    else:
        not_there = False
    context = {
        "id": id,
        "user": user,
        "no_user": not_there
    }
    return render(request, "user_dash/showuser.html", context)
