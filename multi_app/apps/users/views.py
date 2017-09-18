# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request, type):
    print type
    if type == 'users':
        response = "placeholder to later display all the list of users"
        return HttpResponse(response)
    elif type == 'register' or type == 'new':
        response = "placeholder for users to create a new user record"
        return HttpResponse(response)
    elif type == 'login':
        response = "placeholder for users to login"
        return HttpResponse(response)
