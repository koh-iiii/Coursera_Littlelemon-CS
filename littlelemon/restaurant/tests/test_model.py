from django.test import TestCase
from restaurant.models import MenuItem

# Create your tests here.

class MenuItemTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="Burger", price=80, inventory=100)

    def test_create_item(self):
        item = MenuItem.objects.get(title="Burger")
        self.assertEqual(item.price, 80)
        self.assertEqual(item.inventory, 100)