from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.views import MenuItem
from restaurant.serializers import MenuSerializer


# Create your tests here.

class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="Burger", price=80, inventory=100)
        MenuItem.objects.create(title="Pizza", price=120, inventory=50)
        MenuItem.objects.create(title="Salad", price=50, inventory=70)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        items = MenuItem.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)