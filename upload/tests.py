# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import SimpleTestCase
from . import views
from django.urls import reverse, resolve

# Create your tests here.


class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home)


    def test_upload_url_resolves(self):
        url = reverse('upload')
        self.assertEqual(resolve(url).func, views.upload)


    def test_viewImage_url_resolves(self):
        url = reverse('viewImage', args=[1])
        self.assertEqual(resolve(url).func, views.viewImage)