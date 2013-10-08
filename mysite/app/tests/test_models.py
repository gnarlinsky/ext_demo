from django.test import TestCase, LiveServerTestCase
from django.test.client import Client
from app.models import EndUser, EndUserEmail
from django.contrib.contenttypes.models import ContentType
from ttools import t_info


class EndUserTests(TestCase):
    def setUp(self):
        t_info("TestCase EndUserTests", 1)
        t_info(self._testMethodName + ": " + self._testMethodDoc, 3)

    def test_unicode(self):
        """
        Test that custom __unicode__() method returns full name of enduser.
        """
        enduser = EndUser.objects.create(first_name='Lisa', last_name='Simpson')
        self.assertEqual(unicode(enduser), 'Lisa Simpson')

    def test_email(self):
        """
        Test that email() returns all email addresses associated with this enduser.
        """
        # create enduser and several emails
        enduser = EndUser.objects.create(first_name='Lisa', last_name='Simpson')
        EndUserEmail.objects.create(email='test1@email.com', enduser=enduser)
        EndUserEmail.objects.create(email='test2@email.com', enduser=enduser)
        EndUserEmail.objects.create(email='test3@email.com', enduser=enduser)
        self.assertEqual(enduser.emails(),
                         'test1@email.com, test2@email.com, test3@email.com')

class EndUserEmailTest(TestCase):
    def setUp(self):
        t_info("TestCase EndUserEmailTests", 1)
        t_info(self._testMethodName + ": " + self._testMethodDoc, 3)

    def test_unicode(self):
        """
        Test that custom __unicode__() method returns email address
        """
        enduser = EndUser.objects.create(first_name='Lisa', last_name='Simpson')
        enduser_email = EndUserEmail.objects.create(email='test@email.com',
                                                    enduser=enduser)
        self.assertEqual(unicode(enduser_email), 'test@email.com')
