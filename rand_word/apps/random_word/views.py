# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if not 'count' in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    context = {
        "attempt" : request.session['count'],
        "randword" : "not a word"
    }
    return render(request, "random_word/index.html", context)

def reset(request):
    request.session['count'] = 0
    return redirect('/')
