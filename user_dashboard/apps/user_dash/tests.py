# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from .views import index

class HomePageTest(TestCase):
    def test_root_url_resolves(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>Home Page</title>', html)
        self.assertTrue(html.endswith('</html>\n'))
