from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus


class GetPagesTestCase(TestCase):
    def setUp(self):
        pass

    def test_about_page(self):
        path = reverse('clothing:about')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'clothing/about.html')
        self.assertEqual(response.context_data['title'], 'О сайте')

    def tearDown(self):
        pass
