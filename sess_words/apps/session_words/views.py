# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.shortcuts import render, redirect

def main(request):
    print request.session['entries']
    context = {
        "entries": request.session['entries'],
    }
    return render(request, "session_words/index.html", context)

def addword(request):
    if request.method == 'POST':
        data = request.POST
        new_entry = {}
        new_entry['word'] = data.get('new_word')
        new_entry['color'] = data.get('color')
        print data.get('bigtext')
        if data.get('bigtext') == None:
            new_entry['big'] = ''
        else:
            new_entry['big'] = 'big'
        new_entry['time'] = datetime.datetime.now().strftime('%I:%M:%S%p on %B %d, %Y')
        if not 'entries' in request.session or not request.session['entries']:
            entries = []
        else:
            entries = request.session['entries']
        print entries
        entries.append(new_entry)
        request.session['entries'] = entries
    return redirect("/")

def clear(request):
    request.session['entries'] = []
    return redirect("/")
