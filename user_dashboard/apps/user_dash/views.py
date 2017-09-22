# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    context = {
        "title": "Home Page",
    }
    return render(request, "user_dash/index.html", context)
