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
from users.models import User as User2
from task.models import Challenge_tag as cht
from task.models import Lab_tag as lbt
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.


class UsersViewsTestCase(TestCase):

    def setUp(self):
        password = make_password('1234')
        cht.objects.create(
            Challenge_tag_ID='111', Challenge_tag_name='ch1')
        lbt.objects.create(
            Lab_tag_ID='222', Lab_name='lb1')
        User.objects.create(
            username='user1', password=password, email='user1@example.com')
        User.objects.create(
            username='', password=password, email='user2@example.com')
        User2.objects.create(User_ID=123456,
                             User_username='user1', User_password=password, User_email='user1@example.com')
        self.client = Client()

    def test_admin_dashboard(self):
        url = reverse('admin_dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_admin_add_tag(self):
        c = Client()
        response = c.post(reverse('admin_add_tag', kwargs={'have_message': 1}))
        self.assertEqual(response.status_code, 200)

    def test_admin_add_tag_p_a1_1(self):
        c = Client()
        response = c.post(
            reverse("admin_add_tag_p"), {'a1': "1", })
        self.assertEqual(response.status_code, 302)

    def test_admin_add_tag_p_a1_1_true(self):
        c = Client()
        response = c.post(
            reverse("admin_add_tag_p"), {'a1': "1", 'tag_name': 'ch1'})
        self.assertEqual(response.status_code, 302)

    def test_admin_add_tag_p_a1_2(self):
        c = Client()
        response = c.post(
            reverse("admin_add_tag_p"), {'a1': "2", })
        self.assertEqual(response.status_code, 302)

    def test_admin_add_tag_p_a1_2_true(self):
        c = Client()
        response = c.post(
            reverse("admin_add_tag_p"), {'a1': "2", 'tag_name': 'lb1'})
        self.assertEqual(response.status_code, 302)

    def test_admin_add_lessom_group(self):
        c = Client()
        response = c.post(reverse('admin_add_lesson_group',
                                  kwargs={'have_message': 1}))
        self.assertEqual(response.status_code, 200)

    # def test_admin_add_lesson_group_p(self):
    #    f = SimpleUploadedFile("file.jpg", b"file_content")
    #    c = Client()
    #    response = c.post(
    #        reverse('admin_add_lesson_group_p', {
    #            'group_name': '', 'description': '', 'pic': f}))
    #    self.assertEqual(response.status_code, 302)

    def test_admin_add_lesson(self):
        c = Client()
        response = c.post(reverse('admin_add_lesson',
                                  kwargs={'have_message': 1}), {'temp2': 1})
        self.assertEqual(response.status_code, 200)

    # def test_admin_add_lesson_p(self):
    #    f = SimpleUploadedFile("file.jpg", b"file_content")
    #    c = Client()
    #    response = c.post(
    #        reverse('admin_add_lesson_group_p', {
    #            'group_name': '', 'description': '', 'pic': f}))
    #    self.assertEqual(response.status_code, 302)

    def test_admin_add_lab(self):
        c = Client()
        response = c.post(reverse('admin_add_lab',
                                  kwargs={'have_message': 1}), {'temp2': 1})
        self.assertEqual(response.status_code, 200)

    # def test_admin_add_lab_p(self):
    #    f = SimpleUploadedFile("file.jpg", b"file_content")
    #    c = Client()
    #    response = c.post(
    #        reverse('admin_add_lesson_group_p', {
    #            'group_name': '', 'description': '', 'pic': f}))
    #    self.assertEqual(response.status_code, 302)

    def test_admin_add_challenge(self):
        c = Client()
        response = c.post(reverse('admin_add_challenge',
                                  kwargs={'have_message': 1}), {'temp2': 1})
        self.assertEqual(response.status_code, 200)

    # def test_add_challenge_p(self):
    #    f = SimpleUploadedFile("file.jpg", b"file_content")
    #    c = Client()
    #    response = c.post(
    #        reverse('admin_add_lesson_group_p', {
    #            'group_name': '', 'description': '', 'pic': f}))
    #    self.assertEqual(response.status_code, 302)

    def test_admin_add_testcase(self):
        c = Client()
        response = c.post(reverse('admin_add_testcase',
                                  kwargs={'have_message': 1}), {'temp2': 1})
        self.assertEqual(response.status_code, 200)

    def test_admin_add_testcase_p(self):
        c = Client()
        response = c.post(reverse('admin_add_testcase_p'), {'ch_id': 1})
        self.assertEqual(response.status_code, 200)

    # def test_add_testcase_pp(self):
    #    f = SimpleUploadedFile("file.jpg", b"file_content")
    #    c = Client()
    #    response = c.post(
    #        reverse('admin_add_lesson_group_p', {
    #            'group_name': '', 'description': '', 'pic': f}))
    #    self.assertEqual(response.status_code, 302)

