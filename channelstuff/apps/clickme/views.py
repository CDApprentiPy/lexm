# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def main(request):
    context = {}
    return render(request, 'clickme/main.html', context)
