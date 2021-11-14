from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.hashers import make_password

# Create your tests here.


class UsersViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_lab(self):
        url = reverse('task')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_challenge(self):
        url = reverse('challenge')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_challengeX(self):
        url = reverse('challengeX')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
