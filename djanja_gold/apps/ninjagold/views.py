# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime

def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
    if not 'record' in request.session or request.session['record'] == None:
        request.session['record'] = []
    context = {
        "gold": request.session['gold'],
        "record": request.session['record'],
    }
    return render(request, "ninjagold/index.html", context)

def process(request):
    if request.method == 'POST':
        data = request.POST
        choice = data.get('choice')
        if choice == 'farm':
            change = random.randint(10,20)
        elif choice == 'cave':
            change = random.randint(5,10)
        elif choice == 'house':
            change = random.randint(5,10)
        elif choice == 'casino':
            change = random.randint(-50,50)
        else:
            print "choice not correct"
            change = 0
        gold = request.session['gold'] + change
        request.session['gold'] = gold
        newrec = {}
        newrec['choice'] = choice
        newrec['change'] = change
        newrec['time'] = datetime.now().strftime("%Y-%m-%d %I:%M %p")
        record = request.session['record']
        record.append(newrec)
        request.session['record'] = record
    return redirect("/")

def clear(request):
    request.session.clear()
    return redirect("/")
