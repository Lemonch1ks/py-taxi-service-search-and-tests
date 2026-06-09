from django.test import TestCase


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
