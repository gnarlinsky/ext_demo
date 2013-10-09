from django.test import TestCase, LiveServerTestCase
from django.test.client import Client
from app.models import Customer, CustomerEmail
from django.contrib.contenttypes.models import ContentType
from ttools import t_info


class CustomerTests(TestCase):
    def setUp(self):
        t_info("TestCase CustomerTests", 1)
        t_info(self._testMethodName + ": " + self._testMethodDoc, 3)

    def test_unicode(self):
        """
        Test that custom __unicode__() method returns full name of customer.
        """
        customer = Customer.objects.create(first_name='Lisa', last_name='Simpson')
        self.assertEqual(unicode(customer), 'Lisa Simpson')

    def test_email(self):
        """
        Test that email() returns all email addresses associated with this customer.
        """
        # create customer and several emails
        customer = Customer.objects.create(first_name='Lisa', last_name='Simpson')
        CustomerEmail.objects.create(email='test1@email.com', customer=customer)
        CustomerEmail.objects.create(email='test2@email.com', customer=customer)
        CustomerEmail.objects.create(email='test3@email.com', customer=customer)
        self.assertEqual(customer.emails(),
                         'test1@email.com, test2@email.com, test3@email.com')

class CustomerEmailTest(TestCase):
    def setUp(self):
        t_info("TestCase CustomerEmailTests", 1)
        t_info(self._testMethodName + ": " + self._testMethodDoc, 3)

    def test_unicode(self):
        """
        Test that custom __unicode__() method returns email address
        """
        customer = Customer.objects.create(first_name='Lisa', last_name='Simpson')
        customer_email = CustomerEmail.objects.create(email='test@email.com',
                                                    customer=customer)
        self.assertEqual(unicode(customer_email), 'test@email.com')
