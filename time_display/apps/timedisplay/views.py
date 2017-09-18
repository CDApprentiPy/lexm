# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    time_now = gmtime()
    context = {
    "day": strftime("%Y-%m-%d", time_now),
    "time": strftime("%I:%M %p")
    }
    return render(request,'timedisplay/form.html', context)
