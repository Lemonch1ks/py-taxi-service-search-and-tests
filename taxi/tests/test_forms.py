from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.forms import CarSearchForm, DriverSearchForm, ManufacturerSearchForm
from taxi.models import Manufacturer, Car


class TestSearch(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password",
            license_number="test_license_number"
        )

    def test_search_cars_by_model(self):
        honda = Manufacturer.objects.create(name="Honda", country="Japan")
        honda_civic = Car.objects.create(manufacturer=honda, model="Honda Civic")

        toyota = Manufacturer.objects.create(name="Toyota", country="Japan")
        toyota_carola = Car.objects.create(manufacturer=toyota, model="Toyota Carola")

        response = self.client.get(
            reverse("taxi:car-list"),
            {"car_model": "Corolla"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Toyota Corolla")
        self.assertNotContains(response, "Honda Civic")


    def test_search_drivers_by_username(self):
        test_data = {
            "username": "Test User1",
        }
        form = DriverSearchForm(data=test_data)
        self.assertEqual(form.is_valid(), True)

    def test_search_manufacturer_by_name(self):
        test_data = {
            "manufacturer_name": "Test Manufacturer1",
        }
        form = ManufacturerSearchForm(data=test_data)
        self.assertEqual(form.is_valid(), True)
