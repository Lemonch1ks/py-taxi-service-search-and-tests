from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

import taxi
from taxi.forms import CarSearchForm, DriverSearchForm, ManufacturerSearchForm


class TestSearch(TestCase):

    def test_search_cars_by_model(self):
        test_data = {
            "car_model": "Test Model1",
        }
        form = CarSearchForm(data=test_data)
        self.assertEqual(form.is_valid(), True)

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


class TestLoginRequired(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin123"
        )
        self.client.force_login(self.admin_user)

    def test_car_list_view(self):
        url = reverse("taxi:car-list")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)



