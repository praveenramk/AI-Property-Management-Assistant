# File: /ai-property-management-assistant/ai-property-management-assistant/backend/tests/test_properties.py

import unittest
from src.models.property import Property
from src.repositories.property_repository import PropertyRepository

class TestPropertyRepository(unittest.TestCase):

    def setUp(self):
        self.repository = PropertyRepository()

    def test_create_property(self):
        property_data = {
            'name': 'Test Property',
            'address': '123 Test St',
            'price': 1000
        }
        property_instance = self.repository.create(property_data)
        self.assertIsInstance(property_instance, Property)
        self.assertEqual(property_instance.name, property_data['name'])

    def test_get_property(self):
        property_data = {
            'name': 'Test Property',
            'address': '123 Test St',
            'price': 1000
        }
        property_instance = self.repository.create(property_data)
        fetched_property = self.repository.get(property_instance.id)
        self.assertEqual(fetched_property.name, property_instance.name)

    def test_update_property(self):
        property_data = {
            'name': 'Test Property',
            'address': '123 Test St',
            'price': 1000
        }
        property_instance = self.repository.create(property_data)
        updated_data = {
            'name': 'Updated Property',
            'address': '456 Updated St',
            'price': 1200
        }
        updated_property = self.repository.update(property_instance.id, updated_data)
        self.assertEqual(updated_property.name, updated_data['name'])

    def test_delete_property(self):
        property_data = {
            'name': 'Test Property',
            'address': '123 Test St',
            'price': 1000
        }
        property_instance = self.repository.create(property_data)
        self.repository.delete(property_instance.id)
        fetched_property = self.repository.get(property_instance.id)
        self.assertIsNone(fetched_property)

if __name__ == '__main__':
    unittest.main()