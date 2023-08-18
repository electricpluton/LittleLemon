from django.test import TestCase
from restaurant.models import Menu 
from restaurant.serializers import MenuSerializer 
import json


class MenuViewTest(TestCase):
    
    
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Beef Curry", price=16.99, inventory=15)
        Menu.objects.create(title="Goat Curry", price=16.99, inventory=15)
        Menu.objects.create(title="Spaguetti Bolognaise", price=12.99, inventory=20)
        
        
    
    def test_getall(self):
        menu_items = Menu.objects.all()
        
        serializer = MenuSerializer(menu_items, many=True)
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(serializer.data, response)
        
        