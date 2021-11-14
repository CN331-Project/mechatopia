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

    def test_home(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_progress(self):
        url = reverse('progress')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_setting(self):
        c = Client()
        response = c.get(reverse("setting"))
        self.assertEqual(response.status_code, 200)
