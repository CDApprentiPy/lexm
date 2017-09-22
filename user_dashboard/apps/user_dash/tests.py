# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import resolve
from django.test import TestCase
from .views import index

# class FailTest(TestCase):
#
#     def test_something_bad(self):
#         self.assertEqual(1 + 1, 3)

class HomePageTest(TestCase):
    def test_root_url_resolves(self):
        found = resolve('/')
        self.assertEqual(found.func, index)
