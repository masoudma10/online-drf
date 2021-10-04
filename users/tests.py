from django.test import TestCase
from rest_framework import status
from .models import User
from rest_framework.test import APITestCase
from django.urls import reverse


class RegisterTest(APITestCase):



    def test_register_success(self):
        url = reverse('users:register')
        response = self.client.post(url, data={
            'first_name':'alex',
            'last_name':'alexian',
            'email':'email@email.com',
            'password':'123456',
            'password2':'123456'
        })
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)