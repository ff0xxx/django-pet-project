from django.test import TestCase
from django.urls import reverse
from goods.models import Products


class ModelObjectsTestCase(TestCase):
    fixtures = ['fixtures/goods/prod.json', 'fixtures/goods/cat.json']

    def setUp(self):
        pass

    def test_data_category7_page(self):
        queryset = Products.objects.filter(category='7').select_related('category')
        path = reverse('goods:index', args=('kuhnya',))
        response = self.client.get(path)
        self.assertQuerySetEqual(queryset[:3], response.context_data['goods'])

    def tearDown(self):
        pass
