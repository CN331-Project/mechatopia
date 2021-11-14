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

    def setUp(self):
        password = make_password('1234')
        User.objects.create(
            username='user1', password=password, email='user1@example.com')
        User.objects.create(
            username='user2', password=password, email='user2@example.com')
        #User.objects.create(username = 'user3' , firstnamed = 'pannawit' , secondname = 'sangvorn' , email = 'user3@example.com' , password = password)
        self.client = Client()

    def test_welcome(self):
        url = reverse('welcome')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_login_view_successful(self):
        c = Client()
        user = User.objects.get(username='user1')
        response = c.post(reverse("login"), {
                          'Username': 'user1', 'Password': '1234'})
        self.assertEqual(response.status_code, 302)

    def test_login_view_unsucessful(self):
        c = Client()
        user = User.objects.get(username='user1')
        response = c.post(reverse("login"), {
                          'Username': 'user1', 'Password': '6666'})
        self.assertEqual(response.status_code, 302)

    def test_logout_view(self):
        c = Client()
        response = c.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)

    def test_account_username(self):
        c = Client()
        user = User.objects.get(username='user2')
        response = c.post(reverse("signupform"), {
                          'Username': 'user2', 'Firstname': 'Pannawit',
                          'Secondname': 'Sangvorn', 'Email': 'user2@example.com',
                          'Password': '1234', 'Re-Password': '1234'})
        self.assertEqual(response.status_code, 302)

    def test_account_email(self):
        c = Client()
        user = User.objects.get(username='user2')
        response = c.post(reverse("signupform"), {
                          'Username': 'user3', 'Firstname': 'Pannawit',
                          'Secondname': 'Sangvorn', 'Email': 'user2@example.com',
                          'Password': '1234', 'Re-Password': '1234'})
        self.assertEqual(response.status_code, 302)

    def test_account_pass(self):
        c = Client()
        user = User.objects.get(username='user2')
        response = c.post(reverse("signupform"), {
                          'Username': 'user3', 'Firstname': 'Pannawit',
                          'Secondname': 'Sangvorn', 'Email': 'user3@example.com',
                          'Password': '1234', 'Re-Password': '1234'})
        self.assertEqual(response.status_code, 200)

    def test_account_notpass(self):
        c = Client()
        user = User.objects.get(username='user2')
        response = c.post(reverse("signupform"), {
                          'Username': 'user3', 'Firstname': 'Pannawit',
                          'Secondname': 'Sangvorn', 'Email': 'user3@example.com',
                          'Password': '1234', 'Re-Password': '6666'})
        self.assertEqual(response.status_code, 302)

    def test_setting(self):
        c = Client()
        response = c.get(reverse("setting"))
        self.assertEqual(response.status_code, 200)

    def test_nonEditprofile(self):
        c = Client()
        response = c.post(reverse("editprofile"), {
                          'faculty': '', 'major': ''})
        self.assertEqual(response.status_code, 302)

    def test_editprofile(self):
        c = Client()
        response = c.post(reverse("editprofile"), {
                          'faculty': 'TU', 'major': 'COM'})
        self.assertEqual(response.status_code, 302)
