from django.test import TestCase
from app.admin import EmailFormSet
from app.models import Customer
from app.forms import CustomerForm
from ttools import t_info

# TODO: more comprehensive test cases; parallel functional tests

class AdminTests(TestCase):
    def setUp(self):
        t_info("TestCase AdminTests", 1)
        t_info(self._testMethodName + ": " + self._testMethodDoc, 3)

    def test_clean(self):
        """
        Test custom validation -- if admin attempting to delete all email
        addresses for current customer, does the correct validation error get
        raised?
        """
        pass
