from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from task.models import Challenge, Challenge_test_case, Challenge_tag
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.


class UsersViewsTestCase(TestCase):

    def setUp(self):
        Challenge.objects.create(Challenge_ID=1)
        self.client = Client()

    def test_lab(self):
        url = reverse('lab')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_challenge(self):
        url = reverse('challenge')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_simple_upload_post(self):
        f = SimpleUploadedFile("file.txt", b"file_content")
        c = Client()
        response = c.post(
            reverse('simple_upload', kwargs={'challenge_id': 1}), {'mycode': f})
        self.assertEqual(response.status_code, 200)

    def test_simple_upload(self):
        c = Client()
        response = c.get(
            reverse('simple_upload', kwargs={'challenge_id': 1}))
        self.assertEqual(response.status_code, 302)

    def test_simple_upcode_post(self):
        c = Client()
        response = c.post(
            reverse('simple_upcode', kwargs={'challenge_id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_simple_upcode(self):
        c = Client()
        response = c.get(
            reverse('simple_upcode', kwargs={'challenge_id': 1}))
        self.assertEqual(response.status_code, 302)

    def test_problem_1(self):
        c = Client()
        response = c.post(reverse('problem', kwargs={'challenge_id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_problem_2(self):
        c = Client()
        response = c.post(reverse('problem', kwargs={'challenge_id': 2}))
        self.assertEqual(response.status_code, 200)

    def test_problem_3(self):
        c = Client()
        response = c.post(reverse('problem', kwargs={'challenge_id': 3}))
        self.assertEqual(response.status_code, 200)

