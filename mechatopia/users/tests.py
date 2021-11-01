from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your tests here.

class UsersViewsTestCase(TestCase):
    
    
    def setUp(self):
        password = make_password('1234')
        User.objects.create(username = 'user1' , password = password , email = 'user1@example.com')
        self.client = Client()
    
    
    def test_Welcome(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        
    def test_dashBoard(self):
        url = reverse('dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        
    def test_tem(self):
        url = reverse('tem')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        
    def test_signup(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        
    def test_login_view_successful(self):
        c = Client()
        user = User.objects.get(username = 'user1')
        response = c.post(reverse("login"), {'Username': 'user1', 'Password': '1234'})
        self.assertEqual(response.status_code, 302)


    def test_login_view_unsucessful(self):
        c = Client()
        user = User.objects.get(username = 'user1')
        response = c.post(reverse("login"), {'Username': 'user1', 'Password': '6666'})
        self.assertEqual(response.status_code, 302)
        

    def test_logout_view(self):
        c = Client()
        response = c.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)
        
        
    def test_account(self):
        pass