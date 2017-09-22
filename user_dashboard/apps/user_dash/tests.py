# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

class FailTest(TestCase):

    def test_something_bad(self):
        self.assertEqual(1 + 1, 3)
