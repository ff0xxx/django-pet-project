from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus


class RegisterUserTestCase(TestCase):
    def setUp(self):
        self.data = {
            'first_name': 'Gojo',
            'last_name': 'Satoru',
            'username': 'gojo',
            'email': 'gojo@gmail.com',
            'password1': '12345678Aa',
            'password2': '12345678Aa'
        }

    def test_user_registration_success(self):
        user_model = get_user_model()
        path = reverse('users:registration')
        response = self.client.post(path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        # после успешной регистрации пользователь перенаправляется
        self.assertRedirects(response, reverse('users:profile'))
        self.assertTrue(user_model.objects.filter(username=self.data['username']).exists())

    def tearDown(self):
        pass
