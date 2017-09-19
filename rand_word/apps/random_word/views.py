# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    if not 'count' in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    randword = get_random_string(length=14)
    context = {
        "attempt" : request.session['count'],
        "randword" : randword,
    }
    return render(request, "random_word/index.html", context)

def reset(request):
    request.session['count'] = 0
    return redirect('/')
