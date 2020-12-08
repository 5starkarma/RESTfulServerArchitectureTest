from django.urls import reverse

from rest_framework.test import APITestCase


class TestSetup(APITestCase):

    def setUp(self):
        self.create_url = reverse('create-user')

        self.user_data = {
            'username': 'test_user',
            'password': 'test_password'
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
