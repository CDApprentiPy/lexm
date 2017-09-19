# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def dojo(request):
    response = "Nothing here"
    return HttpResponse(response)
