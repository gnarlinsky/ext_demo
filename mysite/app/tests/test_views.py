from django.test import TestCase, LiveServerTestCase
from django.test.client import Client
from app.models import EndUser, EndUserEmail
from app.views import signup
from django.contrib.contenttypes.models import ContentType
from ttools import t_info

# TODO: additional tests

class ViewsTests(TestCase):
    def setUp(self):
        t_info("TestCase ViewsTests", 1)
        t_info(self._testMethodName + ": " + self._testMethodDoc, 3)

    def test_signup(self):
        """ Test signup view """
        #enduser = EndUser.objects.create(first_name='Lisa', last_name='Simpson')
        #self.assertEqual(unicode(enduser), 'Lisa Simpson')
        t_info('if  request.method == "POST"', 5)
        t_info('if not  request.method == "POST"', 5)
        t_info('if eu_form is valid', 5)
        t_info('if eu_form is not valid', 5)
