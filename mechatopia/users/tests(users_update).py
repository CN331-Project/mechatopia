rom django.test import TestCase, Client
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
from users.models import User as User2
from django.core.files.uploadedfile import SimpleUploadedFile
import tempfile


# Create your tests here.


class UsersViewsTestCase(TestCase):

    def setUp(self):
        password = make_password('1234')
        User.objects.create(
            username='user1', password=password, email='user1@example.com')
        User.objects.create(
            username='', password=password, email='user2@example.com')
        User2.objects.create(User_ID=123456,
                             User_username='user1', User_password=password, User_email='user1@example.com')
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
        user = User2.objects.get(User_username='user1')
        response = c.post(reverse("login"), {
                          'Username': 'user1', 'Password': '1234'})
        self.assertEqual(response.status_code, 200)

    def test_login_view_unsucessful(self):
        c = Client()
        user = User2.objects.get(User_username='user1')
        response = c.post(reverse("login"), {
                          'Username': 'user1', 'Password': '6666'})
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        c = Client()
        response = c.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)

    def test_check_login_notpass(self):
        c = Client()
        user = User.objects.get(email='user1@example.com')
        response = c.post(reverse("check_login"), {
                          'email': 'user3@example.com', 'password': '1234'})
        self.assertEqual(response.status_code, 302)

    def test_check_login_pass(self):
        c = Client()
        user = User.objects.get(email='user1@example.com')
        response = c.post(reverse("check_login"), {
                          'email': 'user1@example.com', 'password': '1234'})
        self.assertEqual(response.status_code, 302)

    def test_check_login_pass_UserIsNone(self):
        c = Client()
        response = c.post(reverse("check_login"), {
                          'email': 'user2@example.com', 'password': '5555'})
        self.assertEqual(response.status_code, 302)

    def test_signupform_notpass(self):
        c = Client()
        response = c.post(reverse("signupform"), {
                          'Username': 'user4', 'Email': 'user4@example.com',
                          'Password': '1234', 'Re-Password': '5555', 'bio': 'BOOM'})
        self.assertEqual(response.status_code, 302)

    def test_signupform_pass(self):
        c = Client()
        response = c.post(reverse("signupform"), {
                          'Username': 'user4', 'Email': 'user4@example.com',
                          'Password': '1234', 'Re-Password': '1234', 'bio': 'BOOM'})
        self.assertEqual(response.status_code, 302)

    def test_signupform_pass_username(self):
        c = Client()
        response = c.post(reverse("signupform"), {
                          'Username': 'user1', 'Email': 'user4@example.com',
                          'Password': '1234', 'Re-Password': '1234', 'bio': 'BOOM'})
        self.assertEqual(response.status_code, 302)

    def test_signupform_pass_password(self):
        c = Client()
        response = c.post(reverse("signupform"), {
                          'Username': 'user3', 'Email': '',
                          'Password': '1234', 'Re-Password': '1234', 'bio': 'BOOM'})
        self.assertEqual(response.status_code, 302)

    def test_signupform_pass_email(self):
        c = Client()
        response = c.post(reverse("signupform"), {
                          'Username': 'user3', 'Email': 'user1@example.com',
                          'Password': '1234', 'Re-Password': '1234', 'bio': 'BOOM'})
        self.assertEqual(response.status_code, 302)

    def test_signupform_pass_all(self):
        f = SimpleUploadedFile("file.jpg", b"file_content")
        c = Client()
        response = c.post(reverse("signupform"), {
            'Username': 'user3', 'Email': 'user3@example.com',
            'Password': '1234', 'Re-Password': '1234', 'bio': 'BOOM', 'pic': f})
        self.assertEqual(response.status_code, 302)
