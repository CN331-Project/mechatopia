from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, response
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password


# Create your tests here.

class UsersViewsTestCase(TestCase):

    def test_learning(self):
        url = reverse('learning')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_learning_bak(self):
        url = reverse('learning_bak')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_articles_1(self):
        c = Client()
        response = c.post(reverse('articles', kwargs={'learning_id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_articles_2(self):
        c = Client()
        response = c.post(reverse('articles', kwargs={'learning_id': 2}))
        self.assertEqual(response.status_code, 200)

    def test_articles_3(self):
        c = Client()
        response = c.post(reverse('articles', kwargs={'learning_id': 3}))
        self.assertEqual(response.status_code, 200)

