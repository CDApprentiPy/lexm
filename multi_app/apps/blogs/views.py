# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/blogs')

def show(request, id):
    response = "placeholder to display blog " + str(id)
    return HttpResponse(response)

def edit(request, id):
    response = "placeholder to edit blog " + str(id)
    return HttpResponse(response)

def destroy(request, id):
    response = "placeholder to delete/destroy blog " + str(id)
    return HttpResponse(response)
