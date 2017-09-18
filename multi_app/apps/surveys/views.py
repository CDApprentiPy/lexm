# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "This is for the /surveys route"
    return HttpResponse(response)
